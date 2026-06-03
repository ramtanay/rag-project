# 🚀 AI Study Assistant

<div align="center">

### 🧠 AI-Powered RAG Application using FastAPI, FAISS & Groq

Upload PDFs, perform semantic search, and generate AI-powered answers using Retrieval-Augmented Generation (RAG).

**Complete Full-Stack Solution: Backend API + Web Frontend**

<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/FAISS-VectorDB-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Vanilla%20JavaScript-Frontend-yellow?style=for-the-badge&logo=javascript">
<img src="https://img.shields.io/badge/HTML5%2FCSS3-UI-orange?style=for-the-badge">

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
ai-study-assistant/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── upload.py
│   │   │   └── query.py
│   │   ├── services/
│   │   │   ├── ai_service.py
│   │   │   ├── chunk_service.py
│   │   │   ├── embedding_service.py
│   │   │   ├── pdf_service.py
│   │   │   └── vector_store.py
│   │   └── utils/
│   │       └── text_cleaner.py
│   ├── uploads/
│   ├── requirements.txt
│   ├── .env
│   ├── .gitignore
│   └── README.md
│
├── frontend/
│   ├── index.html       # Main HTML structure
│   ├── styles.css       # Responsive CSS styling
│   ├── app.js           # Application logic & state
│   ├── ui.js            # DOM manipulation
│   ├── api.js           # Backend communication
│   └── README.md        # Frontend documentation
│
└── README.md            # This file 
```

---

# ⚙️ Installation & Setup

## Backend Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/ramtanay/rag-project.git
cd rag-project
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
cd backend
pip install -r requirements.txt
```

---

## 4️⃣ Set Environment Variables

Create a `.env` file inside the backend directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from: https://console.groq.com

---

## 5️⃣ Run Backend Server

```bash
cd backend
uvicorn app.main:app --reload
```

Backend will run at `http://127.0.0.1:8000`

---

## 6️⃣ Open Frontend in Browser

In a **new terminal**, navigate to project and open frontend:

```bash
# Option A: Direct open
open frontend/index.html

# Option B: Local server
python -m http.server 8080 --directory frontend
# Visit: http://localhost:8080
```

---

# 🌐 Frontend

A clean, simple web interface built with **vanilla HTML, CSS, and JavaScript** (no frameworks).

## Frontend Features

✅ Upload PDFs via file picker or drag-drop  
✅ Ask questions about uploaded documents  
✅ Display AI-generated answers with source material  
✅ Real-time status feedback and loading indicators  
✅ Responsive design (desktop & mobile)  
✅ Session state tracking  
✅ Simple, readable code  

## Quick Start - Frontend

### Option 1: Direct Open
```bash
open frontend/index.html
```

### Option 2: Local Server (Recommended)
```bash
python -m http.server 8080 --directory frontend
# Visit: http://localhost:8080
```

**Make sure backend is running first!** (See Backend Setup below)

## Frontend Files

| File | Purpose |
|------|---------|
| `index.html` | Semantic HTML structure |
| `styles.css` | Responsive CSS styling (~350 lines) |
| `app.js` | Application logic & state management |
| `ui.js` | DOM manipulation & rendering |
| `api.js` | Backend API communication |
| `README.md` | Frontend documentation |

**Total: ~1000 lines of code, zero external dependencies**

---

# 🔗 How Backend & Frontend Work Together

```
Browser (Frontend)
    ↓
User uploads PDF or asks question
    ↓
Frontend sends HTTP request to Backend
    ↓
Backend processes and sends JSON response
    ↓
Frontend displays results to user
```

---

# 🌐 API Documentation & Endpoints

After starting the backend server:

| Service | URL |
|---|---|
| Backend Server | http://127.0.0.1:8000 |
| Swagger Docs | http://127.0.0.1:8000/docs |
| Frontend | http://localhost:8080 (if using local server) |

---

## 📤 Upload PDF

```http
POST /upload
```

**Request:** Send PDF file as multipart/form-data

**Response:**
```json
{
  "filename": "example.pdf",
  "total_chunks": 45,
  "embedding_dimension": 384,
  "message": "Embeddings stored in FAISS successfully"
}
```

**Frontend Usage:** Drag-drop or use file picker in upload section

---

## ❓ Ask Questions

```http
POST /ask
```

**Request:** `POST /ask?question=your_question`

**Response:**
```json
{
  "question": "What are the main topics?",
  "answer": "The main topics are...",
  "retrieved_chunks": ["excerpt1", "excerpt2", ...]
}
```

**Frontend Usage:** Type question in input field and press Enter or click Ask button

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

## Backend
- 🔒 Authentication & User Accounts
- 💾 Persistent FAISS Storage
- 📚 Multi-PDF Management
- 💬 Chat History
- ⚡ Streaming Responses
- 📌 Source Citations
- 🧠 LangChain Integration
- ☁️ Cloud Deployment

## Frontend
- ✅ Multiple simultaneous uploads
- ✅ Chat history persistence
- ✅ Export answers to file
- ✅ Dark mode theme
- ✅ Keyboard shortcuts
- ✅ Voice input support

---

# 📚 Key Concepts & Technologies

## Backend
- Retrieval-Augmented Generation (RAG)
- Semantic Search & Embeddings
- Vector Databases (FAISS)
- NLP Preprocessing & Text Chunking
- Prompt Engineering
- FastAPI Development
- AI API Integration

## Frontend
- Vanilla JavaScript (No frameworks)
- Responsive Web Design
- State Management
- API Integration via Fetch
- DOM Manipulation
- Event Handling
- Form Validation

---

# 👨‍💻 Author & Project Info

## Ramtanay Chakraborty

💡 AI/ML & Backend Developer  
🚀 Passionate about AI systems, semantic search, and scalable architectures.

### 🔗 Connect With Me

- GitHub: https://github.com/ramtanay

---

## Project Info

**Full-Stack Application:**
- Backend: FastAPI + Python (RAG system)
- Frontend: Vanilla HTML/CSS/JavaScript (Web UI)
- AI: Groq LLM + Sentence Transformers + FAISS

**Documentation:**
- `README.md` - This file (overview & setup)
- `backend/README.md` - Backend documentation
- `frontend/README.md` - Frontend documentation
- `FRONTEND_INTEGRATION.md` - Integration guide

---

# ⭐ Getting Help & Support

## Quick Reference

- **Backend Issues?** → See `backend/README.md`
- **Frontend Issues?** → See `frontend/README.md`
- **Integration Problems?** → See `FRONTEND_INTEGRATION.md`
- **API Questions?** → Visit `http://localhost:8000/docs` (Swagger UI)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Backend unreachable" | Make sure backend is running on port 8000 |
| Frontend won't load | Check that `frontend/` files are in project root |
| PDF upload fails | Ensure backend has write access to `backend/uploads/` |
| No answers returned | Check that PDF was processed (check chunk count) |

---

# ⭐ Support

If you liked this project, consider giving it a ⭐ on GitHub!

---

<div align="center">

### 🚀 Full-Stack AI Study Assistant
### FastAPI Backend | Vanilla Frontend | Groq LLM

**[Backend README](./backend/README.md) | [Frontend README](./frontend/README.md) | [Integration Guide](./FRONTEND_INTEGRATION.md)**

</div>
