from groq import Groq
import os

from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(question, retrieved_chunks):

    context = "\n".join(retrieved_chunks)

    context = context[:2000]

    prompt = f"""
    You are a helpful AI assistant.

    Answer the question ONLY using the provided context.

    If the answer is not present in the context, say:
    "I could not find that information in the document."

    Context:
    {context}

    Question:
    {question}

    Provide a clean and detailed answer.
    """

    try:

        chat_completion = client.chat.completions.create(

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            model="llama-3.1-8b-instant"
        )

        return chat_completion.choices[0].message.content

    except Exception as e:

        return f"Groq API Error: {str(e)}"

def check_answer(question, answer):

    prompt = f"""
    You are a helpful AI assistant.

    Check if the answer correctly answers the question.

    Question:
    {question}

    Answer:
    {answer}

    If the answer is correct, say "Correct". Otherwise, say "Incorrect".
    """

    try:

        chat_completion = client.chat.completions.create(

            messages=[
            {
                "role": "system",
                "content": "You are a helpful AI study assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
            ],
            model="llama-3.1-8b-instant",
            temperature=0.3
        )

        return chat_completion.choices[0].message.content.strip()

    except Exception as e:

        return f"Groq API Error: {str(e)}"