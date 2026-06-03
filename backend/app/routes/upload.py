from fastapi import APIRouter, UploadFile, File
import shutil
from app.services.chunk_service import chunk_text
from app.services.pdf_service import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.embedding_service import generate_embeddings_batch
from app.services.vector_store import store_embeddings


router = APIRouter()


@router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save file
        file_location = f"uploads/{file.filename}"
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
        
        if len(chunks) == 0:
            raise ValueError("No chunks created from PDF. Document may be empty.")
        
        # Generate embeddings in batches for better performance
        print(f"⏳ Generating embeddings for {len(chunks)} chunks (this may take a minute)...")
        try:
            embeddings = generate_embeddings_batch(chunks, batch_size=32)
            print(f"✓ Embeddings generated: {len(embeddings)} embeddings")
        except Exception as e:
            print(f"✗ Embedding generation failed: {str(e)}")
            raise
        
        # Store in FAISS
        print(f"⏳ Storing embeddings in FAISS...")
        try:
            store_embeddings(chunks, embeddings)
            print(f"✓ Embeddings stored in FAISS")
        except Exception as e:
            print(f"✗ Error storing embeddings: {str(e)}")
            raise
        
        response = {
            "filename": file.filename,
            "total_chunks": len(chunks),
            "embedding_dimension": len(embeddings[0]),
            "message": "Embeddings stored in FAISS successfully"
        }
        print(f"✓ Upload complete: {response}")
        
        return response
        
    except Exception as e:
        print(f"✗ Upload error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise


