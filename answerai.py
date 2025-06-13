import argparse
import base64
import json
import numpy as np
import os,requests
import tempfile
import re
from pathlib import Path
from fastapi import FastAPI,Request
from pydantic import BaseModel
import httpx
from google import genai
from google.genai.types import GenerateContentConfig, HttpOptions
import time
from typing import Optional,List
import re
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("AIPIPE_TOKEN"),
    base_url="https://aipipe.org/openai/v1"  # AI Pipe for embeddings
)
def is_base64_image(data: str) -> bool:
    if not data or not isinstance(data, str):
        return False
    if data.startswith("data:image"):
        data = data.split(",", 1)[-1]
    return bool(re.fullmatch(r'[A-Za-z0-9+/=]{100,}', data.strip()))

def is_http_image_url(data: str) -> bool:
    return isinstance(data, str) and data.startswith(("http://", "https://")) and data.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))

class RateLimiter:
    def __init__(self, requests_per_minute=60, requests_per_second=2):
        self.requests_per_minute = requests_per_minute
        self.requests_per_second = requests_per_second
        self.request_times = []
        self.last_request_time = 0

    def wait_if_needed(self):
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < (1.0 / self.requests_per_second):
            time.sleep((1.0 / self.requests_per_second) - time_since_last)

        self.request_times = [t for t in self.request_times if current_time - t < 60]

        if len(self.request_times) >= self.requests_per_minute:
            time.sleep(60 - (current_time - self.request_times[0]))
            current_time = time.time()
            self.request_times = [t for t in self.request_times if current_time - t < 60]

        self.request_times.append(current_time)
        self.last_request_time = current_time

rate_limiter = RateLimiter(requests_per_minute=5, requests_per_second=2)

def get_embedding(text: str, max_retries: int = 3) -> List[float]:
    for attempt in range(max_retries):
        try:
            rate_limiter.wait_if_needed()
            response = client.embeddings.create(
                model="text-embedding-3-small",
                input=text
            )
            return response.data[0].embedding

        except Exception as e:
            if "rate limit" in str(e).lower() or "quota" in str(e).lower():
                wait_time = 2 ** attempt
                print(f"Rate limit hit, waiting {wait_time} seconds...")
                time.sleep(wait_time)
            elif attempt == max_retries - 1:
                print(f"Failed after {max_retries} attempts: {e}")
                raise
            else:
                print(f"Attempt {attempt + 1} failed: {e}, retrying...")
                time.sleep(1)

    raise Exception("Max retries exceeded")

def get_image_description(image_path):
    """Get a description of the image using Google GenAI."""
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    my_file = client.files.upload(file= image_path)
    # with open(os.path.join('pdsaiitm.github.io', image_path), 'rb') as img_file:
    #     image_data = img_file.read()
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[my_file, "Describe the content of this image in detail, focusing on any text, objects, or relevant features that could help answer questions about it."],
    )
    return response.text

def load_embeddings():
    """Load chunks and embeddings from npz file"""
    data = np.load("embeddings.npz", allow_pickle=True)
    return data["chunks"], data["embeddings"]

def generate_llm_respose(question: str, context: str):
    """Generate a response from the LLM using the question and context."""
    from openai import OpenAI
    import os

    client = OpenAI(
        api_key=os.getenv("AIPIPE_TOKEN"),
        base_url="https://aipipe.org/openrouter/v1"
    )
    # use system prompt to instruct the model to answer based on the context
    system_prompt = """> You are a precise and helpful assistant answering questions from educational content.

> Use ONLY the given context to answer. Do not invent or assume anything.

> Format:
> - Keep answers short and focused (max 4–5 sentences).
> - Use **Markdown** formatting.
> - Include both the **thread URL** and the **specific post URL(s)** if available.
> - Use bullet points or code blocks as needed for clarity.
> - If multiple sources are relevant, cite all of them clearly.

> ⚠️ If context is insufficient to answer, respond exactly with:
> 
> ```
> Sorry to say but I don't know.Maybe you can try asking someone else.
> ```
"""
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # or "openai/gpt-4"
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
            ],
            temperature=0.5,
            max_tokens=512,
            top_p=0.95
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"❌ LLM generation failed: {e}")
        return "Sorry to say but I don't know.Maybe you can try asking someone else."

def answer(question: str, image: Optional[str] = None):
    # Load the API key from the environment variable
    loaded_chunks, loaded_embeddings = load_embeddings()
    if image:
        try:
            if is_base64_image(image):
                # Handle base64
                image_data_uri = f"data:image/jpeg;base64,{image}"
                image_description = get_image_description(image_data_uri)
                question += f" {image_description}"
            elif is_http_image_url(image):
                # Handle HTTP image URL
                response = requests.get(image)
                response.raise_for_status()

                # Save to a temp file
                with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                    tmp.write(response.content)
                    tmp_path = tmp.name

                # Get description
                image_description = get_image_description(tmp_path)
                question += f" {image_description}"
        except Exception as e:
            print(f"⚠️ Failed to process image: {e}")
            question += " [Image description unavailable]"
    # Get the embedding for the question
    question_embedding = get_embedding(question)
    # Calculate cosine similarity
    similarities = np.dot(loaded_embeddings, question_embedding) / (
        np.linalg.norm(loaded_embeddings, axis=1) * np.linalg.norm(question_embedding)
    )
    # Get the index of the 10 most similar chunks
    top_indices = np.argsort(similarities)[-10:][::-1]
    # Get the top chunks
    top_chunks = [loaded_chunks[i] for i in top_indices]

    response  = generate_llm_respose(question, "\n".join(top_chunks))
    return {
        "question": question,
        "response": response,
        "top_chunks": top_chunks
    }

@app.post("/api")
async def api_answer(request: QuestionRequest):
    print("Type of request:", type(request))
    print("Request content:", request)
    # try : 
    #     data = await request.json()
    #     print(data)
    #     return answer(data.get("question"),data.get("image"))
    # except Exception as e:
    #     return {"error": str(e)}
    try:
        # Since `request` is a Pydantic model, you can access its fields directly
        question = request.question
        image = request.image

        # `answer()` is sync, so call it directly without `await`
        return answer(question, image)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8000)
  # Default port for FastAPI
    # main()