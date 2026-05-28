from fastapi import APIRouter, UploadFile, File
import shutil
from app.services.chunk_service import chunk_text
from app.services.pdf_service import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.embedding_service import generate_embedding
from app.services.vector_store import store_embeddings , search_similar_chunks


router = APIRouter()


@router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    extracted_text = extract_text_from_pdf(file_location)
    cleaned_text = clean_text(extracted_text)
    chunks = chunk_text(cleaned_text)
    embeddings = [generate_embedding(chunk) for chunk in chunks]
    store_embeddings(chunks, embeddings)
    return {
    "filename": file.filename,
    "total_chunks": len(chunks),
    "embedding_dimension": len(embeddings[0]),
    "message": "Embeddings stored in FAISS successfully"
    }
