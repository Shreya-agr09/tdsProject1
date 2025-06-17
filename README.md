# 🧠 EduQBot – Intelligent Q&A System for Educational Platforms

EduQBot is a smart backend system that automatically answers student questions from an educational platform using advanced AI models like OpenAI and Google GenAI. It uses text or image inputs (e.g., screenshots of questions or diagrams), retrieves relevant course material and forum context, and generates precise, context-based answers using state-of-the-art LLMs.

---

## 🚀 Features

- 🔍 **Semantic Search**  
  Finds relevant parts of course material using vector similarity over embedded content.

- 🧠 **AI Answer Generation**  
  Produces accurate, context-aware answers using OpenAI GPT or Gemini models.

- 🖼️ **Image-Based Question Input**  
  Extracts questions from uploaded screenshots that may contain text or code.

- 📚 **Course + Forum Context Integration**  
  Uses both the course site (e.g., TDS) and discussion forums for comprehensive context.

- ⚡ **FastAPI Backend**  
  Clean and fast API endpoint to accept user questions and return answers.

- 🧾 **Embedding Workflow**  
  Embeds raw course text into vectors and uses them for context retrieval (RAG-style).

---

## ⚙️ Tech Stack

| Layer       | Technologies Used                          |
|-------------|---------------------------------------------|
| 🧠 AI Models | OpenAI GPT, Google GenAI (Gemini)           |
| 💬 Backend  | FastAPI, Pydantic, Uvicorn                  |
| 💾 Storage  | `.txt` for chunks, `.npz` for embeddings     |
| 🛠 Utilities | dotenv, base64, tempfile, NumPy, tqdm, etc. |

---

## 🧠 AI Capabilities

- **Text and Screenshot Input**  
  Users can input questions as text or image. The system extracts the question from the image internally and processes it like text.

- **Embedding-Based Retrieval**  
  Course and forum content are split into chunks and embedded using OpenAI models. Relevant chunks are retrieved using cosine similarity.

- **Answer Generation from Context**  
  Retrieved content is fed into an LLM to generate a precise answer using a system prompt that restricts the response to known information only.

---

## 📂 Project Structure

```
project/
├── main.py                  # FastAPI app with /answer endpoint
├── embed_utils.py          # Functions to embed and search context
├── generate_embeddings.py  # Script to embed chunk3.txt into embeddingz3.npz
├── chunk3.txt              # Raw course + forum content (chunked)
├── embeddingz3.npz         # Precomputed vector embeddings
├── .env                    # API keys and config
└── requirements.txt
```

---

## 🧪 Setup and Run Locally

### 1. Clone the Project

```bash
git clone https://github.com/yourusername/eduqbot
cd eduqbot
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_genai_key
AIPIPE_TOKEN=your_aipipe_key_if_applicable
```

### 4. Generate Embeddings (Optional, if not using `embeddingz3.npz`)

```bash
python generate_embeddings.py
```

### 5. Run the API

```bash
uvicorn main:app --reload
```

---

## 📤 API Usage

### Endpoint:  
`POST /answer`

### Payloads:

**Text-based question:**

```json
{
  "question": "What is the difference between Pandas and NumPy?",
  "image": null
}
```

**Image-based question (base64 or URL):**

```json
{
  "question": null,
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
}
```

### Response:

```json
{
  "answer": "Pandas provides high-level data structures like DataFrames..."
}
```

---

## 📷 Screenshots / Demo

> _Coming soon..._  
You can add sample curl commands, Postman screenshots, or frontend previews here.

---

## 🧠 Future Enhancements

- Add web-based UI with upload and chat features  
- Admin interface to update course content  
- Integration with live forums and quizzes  
- Caching or performance optimization  

---

## 📜 License

MIT License – use freely for academic, educational, and personal projects.

---

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) – GPT and Embedding APIs  
- [Google GenAI](https://ai.google/) – Gemini model for LLM tasks  
- [IIT Madras Online Degree](https://onlinedegree.iitm.ac.in/) – Source of TDS content  
- All contributors and testers involved

---