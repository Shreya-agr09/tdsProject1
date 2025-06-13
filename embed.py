# import openai
import time, os, json
import numpy as np
from typing import List
from pathlib import Path
from tqdm import tqdm  # Progress Bar
from dotenv import load_dotenv

load_dotenv()

# Set AI Pipe config
from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("AIPIPE_TOKEN"),
    base_url="https://aipipe.org/openai/v1"  # AI Pipe for embeddings
)

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

def chunk_text(text, chunk_size=600, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# 👇 Main processing

# Collect all markdown files
dirs = ['course_content', 'discourse_threads']
files = []
for directory in dirs:
    files.extend(Path(directory).rglob("*.md"))

file_chunks = {}
all_chunks = []
all_embeddings = []
total_chunks = 0

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    file_chunks[file_path] = chunks
    all_chunks.extend(chunks)
    total_chunks += len(chunks)

print(f"\u2705 Chunking complete: {total_chunks} total chunks from {len(files)} files.")

# with open("chunks.txt", "w", encoding="utf-8") as f:
#     for chunk in all_chunks:
#         f.write(chunk + "-------" + "\n")

# with tqdm(total=total_chunks, desc="\ud83d\udd0d Processing embeddings") as pbar:
#     for file_path, chunks in file_chunks.items():
#         for chunk in chunks:
#             try:
#                 embedding = get_embedding(chunk)
#                 all_embeddings.append(embedding)
#             except Exception as e:
#                 print(f"\u26a0\ufe0f Error embedding chunk from {file_path}: {e}")
#             pbar.update(1)

# np.savez("embeddings.npz", chunks=all_chunks, embeddings=all_embeddings)

# with open("file_chunks.json", "w", encoding="utf-8") as f:
#     json.dump({str(k): v for k, v in file_chunks.items()}, f, ensure_ascii=False, indent=4)
