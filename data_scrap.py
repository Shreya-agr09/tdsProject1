import requests
import json
from bs4 import BeautifulSoup
from google.api_core.exceptions import ResourceExhausted
import os,time
from markdownify import markdownify as md
from google import genai
from urllib.parse import urlunparse
from urllib.parse import urlencode
from dotenv import load_dotenv
load_dotenv()

with open('cookies.txt', 'r') as file:
    cookie = file.read().strip()

with open('filtered_topics.json', 'r') as file:
    data = json.load(file)

# Ensure directory exists
os.makedirs("discourse_threads", exist_ok=True)

def get_image_description(image_path, retries=3, delay=5):
    """Get a description of the image using Google GenAI with retry on 503."""
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    my_file = client.files.upload(file=image_path)

    for attempt in range(1, retries + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[my_file, "Describe the content of this image in detail, focusing on any text, objects, or relevant features that could help answer questions about it."],
            )
            return response.text.strip()

        except Exception as e:
            error_msg = str(e)
            if "503" in error_msg or "overloaded" in error_msg:
                print(f"⚠️ Gemini model busy (attempt {attempt}/{retries}). Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2  # exponential backoff
            else:
                print(f"❌ Unexpected error: {e}")
                break

    return "⚠️ Could not get description due to model unavailability."

# Sample post from the JSON response (as you showed)
def html_to_markdown(thread, filename):
    for post in thread:
        # 1. Base Discourse domain
        base_url = "https://discourse.onlinedegree.iitm.ac.in"

        # 2. Convert cooked HTML to markdown
        markdown_text = md(post["cooked"], strip=["a", "img"]).strip()  # removes <a> hrefs to avoid noisy internal links

        # 3. Extract image description and URLs
        soup = BeautifulSoup(post["cooked"], "html.parser")
        
        image_markdowns = []
        for img_tag in soup.find_all("img"):
            try:
                    src_url = img_tag.get("src")
                    full_image_url = requests.compat.urljoin(base_url, src_url)

                    # Download image
                    img_response = requests.get(full_image_url)
                    img_response.raise_for_status()

                    temp_path = "temp_image.png"
                    with open(temp_path, "wb") as f:
                        f.write(img_response.content)

                    # Get Gemini-generated description
                    image_desc = get_image_description(temp_path)
                    image_markdowns.append(f" {image_desc}")

                    # Remove temporary file
                    os.remove(temp_path)

            except Exception as e:
                    print(f"❌ Error processing image: {e}")
                    continue

        # 4. Get full post URL
        full_post_url = requests.compat.urljoin(base_url, post["post_url"])

        # 5. Final markdown block
        image_block = "\n".join(image_markdowns)
        
        final_md = (
                f"{markdown_text}\n"
                f"{image_block.strip()}\n"
                f"Post URL: [{full_post_url}]({full_post_url})\n"
                f"---\n")
        
        with open(filename, "a", encoding="utf-8") as f:
            f.write(final_md)
        # with open("discourse_posts.md", "a", encoding="utf-8") as f:
        #     f.write(final_md)
            # f.write("\n\n---\n\n")

for i, title in data.items():
    page = 0
    all_posts = []
    while True:
        # Build the URL for the current page
        path = f"/t/{title}/{i}.json"
        query = urlencode({"page": page})
        full_url = urlunparse(("https", "discourse.onlinedegree.iitm.ac.in", path, "", query, ""))

        # Send request
        response = requests.get(
            full_url,
            headers={
                'cookie': cookie,
                'User-Agent': 'Mozilla/5.0'})
        # If response is not 200, stop
        if response.status_code != 200:
            break

        # Otherwise, process or print the URL
        print(f"✅ Page {page}: {full_url}")
        posts = response.json().get("post_stream", {}).get("posts", [])
        all_posts.extend(posts)
        # Save intermediate results every page (in case of crash)
        with open(f"discourse_threads/temp_{i}.json", "a", encoding="utf-8") as f:
            json.dump(all_posts, f, ensure_ascii=False, indent=2)

        page += 1
        time.sleep(3)

    if all_posts:
        # Normalize file name
        # safe_title = title.replace("/", "_").replace(" ", "_")
        filename = f"discourse_threads/{i}_{title}.md"
        thread_url = f"https://discourse.onlinedegree.iitm.ac.in/t/{title}/{i}"

        # Start new file with URL
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Thread URL: [{thread_url}]({thread_url})\n\n")

        # Write all post content
        html_to_markdown(all_posts, filename)
        print(f"✅ Markdown file saved: {filename}")
        # ✅ Delete the temp file now that everything is done
        temp_path = f"discourse_threads/temp_{i}.json"
        if os.path.exists(temp_path):
            os.remove(temp_path)

        
        # Increment page
        page += 1

