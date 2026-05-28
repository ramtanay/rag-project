from fastapi import APIRouter

from app.services.embedding_service import create_query_embedding
from app.services.vector_store import search_similar_chunks
from app.services.ai_service import generate_answer
from app.utils.text_cleaner import clean_text

router = APIRouter()

@router.post("/ask")
async def ask_question(question: str):
    question = clean_text(question)

    query_embedding = create_query_embedding(question)

    retrieved_chunks = search_similar_chunks(query_embedding)

    answer = generate_answer(question, retrieved_chunks)

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": retrieved_chunks
    }