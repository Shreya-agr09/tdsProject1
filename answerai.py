import os
import re
import time
import base64
import tempfile
import requests
import numpy as np
from typing import Optional, List
from dotenv import load_dotenv
from google import genai
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from openai import OpenAI as OpenAIClient
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)
print("🔐 Using token:", os.getenv("AIPIPE_TOKEN"))


# OpenAI embedding client (via AI Pipe)
# Embedding client for AI Pipe
from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("AIPIPE_TOKEN"),
    base_url="https://aipipe.org/openai/v1"  # AI Pipe for embeddings
)
# FastAPI app
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Input model
class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None
    link: Optional[str] = None


# Rate limiter for embedding
class RateLimiter:
    def __init__(self, requests_per_minute=60, requests_per_second=2):
        self.requests_per_minute = requests_per_minute
        self.requests_per_second = requests_per_second
        self.request_times = []
        self.last_request_time = 0

    def wait_if_needed(self):
        now = time.time()
        if (delta := now - self.last_request_time) < (1.0 / self.requests_per_second):
            time.sleep((1.0 / self.requests_per_second) - delta)
        self.request_times = [t for t in self.request_times if now - t < 60]
        if len(self.request_times) >= self.requests_per_minute:
            time.sleep(60 - (now - self.request_times[0]))
        self.request_times.append(time.time())
        self.last_request_time = time.time()

rate_limiter = RateLimiter(requests_per_minute=5, requests_per_second=2)

def is_base64_image(data: str) -> bool:
    if not data or not isinstance(data, str):
        return False
    if data.startswith("data:image"):
        data = data.split(",", 1)[-1]
    return bool(re.fullmatch(r'[A-Za-z0-9+/=]{100,}', data.strip()))

def is_http_image_url(data: str) -> bool:
    return data.lower().startswith(("http://", "https://")) and data.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))

def get_embedding(text: str, max_retries: int = 3) -> List[float]:
    for attempt in range(max_retries):
        try:
            rate_limiter.wait_if_needed()
            response = client.embeddings.create(
                model="text-embedding-3-small",
                input=text
            )
            if not response or not response.data:
                raise ValueError("Embedding API returned empty or null response.")
            return response.data[0].embedding
        except Exception as e:
            if attempt == max_retries - 1:
                raise Exception(f"Max retries exceeded: {e}")
            time.sleep(2 ** attempt)
    # print("🔍 Raw embedding response:", response)

def get_image_description(image_path):
    """Get a description of the image using Google GenAI."""
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    my_file = client.files.upload(file= image_path)
    # with open(os.path.join('pdsaiitm.github.io', image_path), 'rb') as img_file:
    #     image_data = img_file.read()
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[my_file, """You are an assistant specialized in analyzing educational images. Extract and clearly present all meaningful content from the image, including:

        Questions or problem statements — transcribe them fully and accurately.

        Code snippets — preserve correct formatting, indentation, and syntax.

        Mathematical expressions or formulas — retain symbols and structure precisely.

        Diagrams or visual processes — describe what the diagram shows, including labeled parts, arrows, steps, and the overall process it illustrates.

        Ignore non-informative background elements, watermarks, or decorations."""],
    )
    return response.text

def load_embeddings():
    data = np.load("embeddings3.npz", allow_pickle=True)
    return data["chunks"], data["embeddings"]

def generate_llm_response(question: str, context: str):
    from openai import OpenAI
    import os

    client = OpenAI(
        api_key=os.getenv("AIPIPE_TOKEN"),
        base_url="https://aipipe.org/openrouter/v1"
    )
    system_prompt = """> You are a precise assistant answering questions from educational content.
> Use ONLY the given context to answer. Do not invent or assume anything.
> - Keep answers short and focused (max 4–5 sentences).
> - Use **Markdown** formatting.
> - Include both the **thread URL** and the **specific post URL(s)** if available.
> - Use bullet points or code blocks as needed for clarity.
> - If multiple sources are relevant, cite all of them clearly.
> ⚠️ If context is insufficient to answer, respond exactly with:
Sorry to say but I don't know.Maybe you can try asking someone else.
"""
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
        ],
        temperature=0,
        max_tokens=400,
        top_p=0.95
        # top_k=20
    )
    if not response or not hasattr(response, "choices") or not response.choices:
        raise ValueError("ChatCompletion API returned empty or null response.")
    return response.choices[0].message.content

def extract_answer_and_links(raw_response: str):
    answer_lines = []
    links = []

    seen_urls = set()

    for line in raw_response.splitlines():
        line = line.strip()

        # Match all markdown-style links
        for match in re.findall(r'\[([^\]]+)\]\((https?://[^\)]+)\)', line):
            label, url = match
            if url not in seen_urls:
                links.append({"url": url, "text": label})
                seen_urls.add(url)

        # Remove links from the text line
        line = re.sub(r'\[([^\]]+)\]\((https?://[^\)]+)\)', '', line).strip()

        if line:
            answer_lines.append(line)

    answer_text = " ".join(answer_lines).strip()
    return {
        "answer": answer_text,
        "links": links
    }
def answer(question: str, image: Optional[str] = None, link: Optional[str] = None):
    chunks, embeddings = load_embeddings()

    # 📸 Process image (if any)
    if image:
        try:
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                if is_base64_image(image):
                    tmp.write(base64.b64decode(image))
                elif is_http_image_url(image):
                    tmp.write(requests.get(image).content)
                else:
                    raise ValueError("Invalid image format")
                image_desc = get_image_description(tmp.name)
                question += " " + image_desc
        except Exception as e:
            print(f"⚠️ Failed to process image: {e}")
            question += " [Image description unavailable]"

    # 💡 Get embedding for the question
    q_embed = get_embedding(question)

    candidate_chunks, candidate_embeddings = [], []
    thread_url, course_anchor = None, None

    # 🔍 Discourse filtering
    if link and "discourse.onlinedegree.iitm.ac.in" in link:
        match = re.match(r"(https://discourse\.onlinedegree\.iitm\.ac\.in/t/[^/]+/\d+)", link)
        if match:
            thread_url = match.group(1)
            print(f"📎 Matched Discourse thread: {thread_url}")
            filtered = [(chunk, emb) for chunk, emb in zip(chunks, embeddings) if thread_url in chunk]
            if filtered:
                candidate_chunks, candidate_embeddings = zip(*filtered)
                candidate_chunks, candidate_embeddings = list(candidate_chunks), list(candidate_embeddings)
            else:
                print("⚠️ No matching Discourse chunks found.")

    # 🔍 Course content filtering
    elif link and "tds.s-anand.net/#/" in link:
        course_anchor = link.split("/")[-1].strip().lower()
        print(f"📚 Matched course content section: {course_anchor}")
        filtered = [
            (chunk, emb) for chunk, emb in zip(chunks, embeddings)
            if re.search(rf"^##\s+.*{re.escape(course_anchor)}", chunk, re.IGNORECASE | re.MULTILINE)
        ]
        if filtered:
            candidate_chunks, candidate_embeddings = zip(*filtered)
            candidate_chunks, candidate_embeddings = list(candidate_chunks), list(candidate_embeddings)
        else:
            print("⚠️ No matching course section found.")

    # 🔁 Fallback to full dataset if nothing filtered
    if not candidate_chunks:
        candidate_chunks = chunks
        candidate_embeddings = embeddings

    candidate_embeddings = np.array(candidate_embeddings)
    similarities = np.dot(candidate_embeddings, q_embed) / (
        np.linalg.norm(candidate_embeddings, axis=1) * np.linalg.norm(q_embed)
    )

    top_indices = np.argsort(similarities)[-8:][::-1]
    top_chunks = [candidate_chunks[i] for i in top_indices]
    context = "\n".join(top_chunks)

    # 💬 Call LLM
    raw_response = generate_llm_response(question, context)
    result = extract_answer_and_links(raw_response)

    # ⛔ Skip all link injection if the model gave "Sorry to say..."
    if result["answer"].strip().lower().startswith("sorry to say but i don't know"):
        print("⚠️ Model expressed uncertainty — no link injection performed.")
        return result

    # ✅ Inject Discourse thread link (if actually used in context)
    if thread_url and any(thread_url in chunk for chunk in top_chunks):
        existing_urls = [l["url"] for l in result.get("links", [])]
        if thread_url not in existing_urls:
            result["links"].append({
                "url": thread_url,
                "text": "Discourse Thread"
            })
            if thread_url not in result["answer"]:
                result["answer"] += f"\n\n📎 [View related discussion]({thread_url})"

    # ✅ Inject course link based on section header
    for chunk in top_chunks:
        section_match = re.search(r"^##\s+(.+)$", chunk, re.MULTILINE)
        if section_match:
            section_title = section_match.group(1).strip()
            anchor_text = section_title.split(':', 1)[1].strip() if ':' in section_title else section_title
            anchor = anchor_text.lower().replace(' ', '-')
            default_page_link = f"https://tds.s-anand.net/#/{anchor}"

            if default_page_link not in [l["url"] for l in result.get("links", [])]:
                result["links"].append({
                    "url": default_page_link,
                    "text": section_title
                })
                if default_page_link not in result["answer"]:
                    result["answer"] += f"\n\n📚 For more: {default_page_link}"
            break  # Only first matching section

    print("\n📤 Final returned result:", result)
    return result

@app.get("/")
async def serve_ui():
    return FileResponse("static/index.html")

@app.post("/api")
async def api_answer(request: QuestionRequest):
    try:
        return answer(request.question, request.image,request.link)
    except Exception as e:
        return {
        "answer": f"❌ Error: {str(e)}",
        "links": [],
        "error": str(e)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
