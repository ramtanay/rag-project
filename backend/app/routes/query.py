from fastapi import APIRouter, Query, HTTPException

from app.services.embedding_service import create_query_embedding
from app.services.vector_store import search_similar_chunks
from app.services.ai_service import (
    rewrite_query,
    generate_answer
)
from app.utils.text_cleaner import clean_text

router = APIRouter()


@router.post("/ask")
async def ask_question(question: str = Query(...)):

    print(f"\n📝 Received question: {question}")

    try:

        # =========================
        # VALIDATION
        # =========================

        if not question or not question.strip():
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )

        # =========================
        # CLEAN QUESTION
        # =========================

        question = clean_text(question)

        print(f"✓ Cleaned question: {question}")

        # =========================
        # SUPERVISOR
        # =========================

        improved_query = rewrite_query(question)

        print(
            f"✓ Improved query: "
            f"{improved_query}"
        )

        # =========================
        # EMBEDDING
        # =========================

        query_embedding = create_query_embedding(
            improved_query
        )

        print(
            f"✓ Query embedding created: "
            f"{len(query_embedding)} dimensions"
        )

        # =========================
        # RETRIEVAL
        # =========================

        retrieved_chunks = search_similar_chunks(
            query_embedding,
            top_k=5
        )

        print(
            f"✓ Retrieved "
            f"{len(retrieved_chunks)} chunks"
        )

        # =========================
        # NO RESULTS
        # =========================

        if not retrieved_chunks:

            return {
                "question": question,
                "improved_query": improved_query,
                "answer": (
                    "No relevant information "
                    "was found in the uploaded "
                    "documents."
                ),
                "retrieved_chunks": []
            }

        # =========================
        # WORKER
        # =========================

        print("⏳ Generating answer...")

        answer = generate_answer(
            question,
            retrieved_chunks
        )

        print("✓ Answer generated")

        # =========================
        # RESPONSE
        # =========================

        response = {
            "question": question,
            "improved_query": improved_query,
            "answer": answer,
            "retrieved_chunks": retrieved_chunks
        }

        print("✓ Query complete")

        return response

    except HTTPException:
        raise

    except Exception as e:

        print(f"✗ Query error: {e}")

        return {
            "question": question,
            "answer": f"Error: {str(e)}",
            "retrieved_chunks": []
        }