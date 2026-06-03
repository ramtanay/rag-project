from fastapi import APIRouter, Query

from app.services.embedding_service import create_query_embedding
from app.services.vector_store import search_similar_chunks
from app.services.ai_service import generate_answer
from app.utils.text_cleaner import clean_text

router = APIRouter()

@router.post("/ask")
async def ask_question(question: str = Query(...)):
    print(f"📝 Received question: {question}")
    
    # Validate question is not empty
    if not question or not question.strip():
        raise ValueError("Question cannot be empty")
    
    # Clean question
    question = clean_text(question)
    print(f"✓ Question cleaned: {question}")

    # Create embedding for question
    query_embedding = create_query_embedding(question)
    print(f"✓ Query embedding created: {len(query_embedding)} dimensions")

    # Search for similar chunks
    retrieved_chunks = search_similar_chunks(query_embedding)
    print(f"✓ Retrieved {len(retrieved_chunks)} chunks")
    
    # If no chunks found, return helpful message
    if not retrieved_chunks:
        print("⚠️ No chunks found in FAISS index")
        return {
            "question": question,
            "answer": "No relevant information found in the uploaded documents. Please upload a document and try again.",
            "retrieved_chunks": []
        }

    # Generate answer using LLM
    print(f"✓ Generating answer with LLM...")
    answer = generate_answer(question, retrieved_chunks)
    print(f"✓ Answer generated")

    response = {
        "question": question,
        "answer": answer,
        "retrieved_chunks": retrieved_chunks
    }
    print(f"✓ Query complete")
    
    return response