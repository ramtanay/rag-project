from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.chunk_service import chunk_text
from app.services.pdf_service import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.embedding_service import generate_embeddings_batch
from app.services.vector_store import store_embeddings

router = APIRouter()

UPLOAD_DIR = "uploads"


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Create uploads folder if it doesn't exist
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # Save uploaded file
        file_location = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"✓ File saved: {file_location}")

        # Extract text from PDF
        extracted_text = extract_text_from_pdf(file_location)
        print(f"✓ Text extracted: {len(extracted_text)} characters")

        # Clean text
        cleaned_text = clean_text(extracted_text)
        print(f"✓ Text cleaned: {len(cleaned_text)} characters")

        # Split into chunks
        chunks = chunk_text(cleaned_text)
        print(f"✓ Text chunked: {len(chunks)} chunks")

        if not chunks:
            raise ValueError(
                "No chunks created from PDF. Document may be empty."
            )

        # Generate embeddings
        print(
            f"⏳ Generating embeddings for {len(chunks)} chunks..."
        )

        embeddings = generate_embeddings_batch(
            chunks,
            batch_size=32
        )

        print(
            f"✓ Embeddings generated: {len(embeddings)} embeddings"
        )

        # Store embeddings in FAISS
        print("⏳ Storing embeddings in FAISS...")

        store_embeddings(
            chunks,
            embeddings
        )

        print("✓ Embeddings stored in FAISS")

        response = {
            "filename": file.filename,
            "total_chunks": len(chunks),
            "embedding_dimension": len(embeddings[0]),
            "message": "Embeddings stored in FAISS successfully"
        }

        print(f"✓ Upload complete: {response}")

        # Optional cleanup (recommended on Render)
        try:
            os.remove(file_location)
            print(f"✓ Deleted temporary file: {file_location}")
        except Exception as cleanup_error:
            print(
                f"⚠ Could not delete file: {cleanup_error}"
            )

        return response

    except Exception as e:
        print(f"✗ Upload error: {str(e)}")

        import traceback
        traceback.print_exc()

        raise