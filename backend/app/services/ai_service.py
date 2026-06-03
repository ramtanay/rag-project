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
    Format the answer using:
    - headings
    - bullet points
    - short paragraphs

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

        Answer ONLY from the provided context.
        if the provided context have the answers for the question, say "Yes" and generate the answer, otherwise say "No related context found" .

        Format the answer using:
        - headings
        - bullet points
        - short paragraphs

        Context:
        {context}

        Question:
        {question}
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