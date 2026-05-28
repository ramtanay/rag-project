# 🚀 AI Study Assistant Backend

<div align="center">

### 🧠 AI-Powered RAG Backend using FastAPI, FAISS & Groq

Upload PDFs, perform semantic search, and generate AI-powered answers using Retrieval-Augmented Generation (RAG).

<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/FAISS-VectorDB-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python">

</div>

---

# ✨ Features

✅ PDF Upload & Processing  
✅ Text Extraction from PDFs  
✅ NLP Text Cleaning & Preprocessing  
✅ Smart Text Chunking  
✅ Semantic Embedding Generation  
✅ FAISS Vector Database Integration  
✅ AI-Powered Question Answering  
✅ Semantic Search & Retrieval  
✅ FastAPI REST API Backend  
✅ Retrieval-Augmented Generation (RAG)

---

# 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Backend** | FastAPI, Python |
| **AI / NLP** | Sentence Transformers, FAISS |
| **LLM Provider** | Groq API (Llama 3.1) |
| **PDF Processing** | PyPDF |
| **Utilities** | NumPy, python-dotenv |

---

# 🧠 RAG Pipeline Architecture

```text
                ┌──────────────────┐
                │   Upload PDF     │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │  Extract Text    │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │   Clean Text     │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │   Chunk Text     │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ Generate Embeds  │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ Store in FAISS   │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ User Question    │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ Semantic Search  │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ Groq LLM Answer  │
                └──────────────────┘
```

---

# 📂 Project Structure

```text
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── upload.py
│   │   └── query.py
│   │
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── chunk_service.py
│   │   ├── embedding_service.py
│   │   ├── pdf_service.py
│   │   └── vector_store.py
│   │
│   └── utils/
│       └── text_cleaner.py
│
├── uploads/
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-study-assistant-backend.git

cd ai-study-assistant-backend
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### ▶️ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

👉 https://console.groq.com

---

# ▶️ Run The Server

```bash
uvicorn app.main:app --reload
```

---

# 🌐 API Documentation

After starting the server:

| Service | URL |
|---|---|
| Backend Server | http://127.0.0.1:8000 |
| Swagger Docs | http://127.0.0.1:8000/docs |

---

# 📄 API Endpoints

## 📤 Upload PDF

```http
POST /upload
```

Uploads and processes PDF documents.

---

## ❓ Ask Questions

```http
POST /ask
```

Ask questions based on uploaded documents.

### Example Query

```text
What skills does Ramtanay have?
```

---

# 🧠 Example Workflow

### 1️⃣ Upload Resume PDF

↓

### 2️⃣ Extract & Clean Text

↓

### 3️⃣ Chunk Document into Smaller Pieces

↓

### 4️⃣ Generate Semantic Embeddings

↓

### 5️⃣ Store Embeddings in FAISS

↓

### 6️⃣ User Asks Question

↓

### 7️⃣ Retrieve Most Relevant Chunks

↓

### 8️⃣ Groq LLM Generates Final Answer

---

# 🚀 Future Improvements

- 🔒 Authentication System
- 💾 Persistent FAISS Storage
- 🌐 React Frontend
- 📚 Multi-PDF Support
- 💬 Chat History
- ⚡ Streaming Responses
- 📌 Source Citations
- 🧠 LangChain Integration
- ☁️ Cloud Deployment

---

# 📚 Key Concepts Learned

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Embeddings & Vector Databases
- NLP Preprocessing
- Prompt Engineering
- FastAPI Backend Development
- AI API Integration
- Semantic Retrieval Systems

---

# 👨‍💻 Author

## Ramtanay Chakraborty

💡 AI/ML & Backend Developer  
🚀 Passionate about AI systems, semantic search, and scalable backend architectures.

### 🔗 Connect With Me

- GitHub: https://github.com/ramtanay

---

# ⭐ Support

If you liked this project, consider giving it a ⭐ on GitHub!

---

<div align="center">

### 🚀 Built with FastAPI, FAISS & Groq AI

</div>
