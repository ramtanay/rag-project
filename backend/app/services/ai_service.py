from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def rewrite_query(question: str):
    try:
        supervisor_prompt = f"""
You are a Query Supervisor for a RAG system.

Your task is to improve user queries before retrieval.

Rules:

1. Understand the user's intent.
2. Rewrite vague queries into clear searchable queries.
3. Preserve the original intent.
4. Do not add unrelated information.
5. Return ONLY the improved query.
6. If the query is already clear, return it unchanged.

Examples:

summary
→ Provide a concise summary of the document.

skills
→ What skills are mentioned in the document?

projects
→ What projects are described in the document?

education
→ What educational background is mentioned in the document?

User Question:
{question}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a query rewriting assistant."
                },
                {
                    "role": "user",
                    "content": supervisor_prompt
                }
            ],
            temperature=0
        )

        improved_query = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        print(f"\nOriginal Query: {question}")
        print(f"Improved Query: {improved_query}")

        return improved_query
    except Exception as e:
        print(f"Supervisor Error: {e}")
        return question


def generate_answer(question, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)

    # Limit context size
    context = context[:6000]

    try:
        worker_prompt = f"""
You are an intelligent Retrieval-Augmented Generation (RAG) assistant.

IMPORTANT RULES

1. Use ONLY the provided context.

2. Never invent facts.

3. If the answer cannot be found in the context, respond:

"The provided documents do not contain enough information to answer this question."

4. Do not use external knowledge.

5. Treat the retrieved context as the source of truth.

6. Use clean Markdown formatting.

7. Prefer:

- Headings
- Bullet points
- Numbered lists
- Tables (when useful)

8. Correct obvious OCR and PDF extraction mistakes when confidence is high.

Examples:

- Java Script → JavaScript
- Git Hub → GitHub
- Num Py → NumPy
- Lang Chain → LangChain
- Fast API → FastAPI
- Ramtan AY → Ramtanay
- Ramtana Y → Ramtanay

9. Preserve original meaning.

10. Never guess corrections if uncertain.

11. When describing a person:

- Prefer using the person's name.
- Avoid excessive pronouns.
- Do not assume gender.

12. For summaries:

- Focus on important information.
- Remove repetition.
- Keep concise.

13. Answer exactly what the user asks.

14. Do not provide unrelated information.

15. Combine information from multiple chunks when appropriate.

16. Clearly state when context is insufficient.

Context:
{context}

Question:
{question}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You answer questions strictly "
                        "from the provided document context."
                    )
                },
                {
                    "role": "user",
                    "content": worker_prompt
                }
            ],
            temperature=0.2
        )

        return (
            response
            .choices[0]
            .message
            .content
        )
    except Exception as e:
        return f"Groq API Error: {str(e)}"

