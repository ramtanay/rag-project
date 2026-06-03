from sentence_transformers import SentenceTransformer
import sys

try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✓ Embedding model loaded successfully", file=sys.stderr)
except Exception as e:
    print(f"✗ Error loading embedding model: {e}", file=sys.stderr)
    raise

def generate_embedding(text):
    """Generate embedding for a single text"""
    try:
        embedding = model.encode(text, show_progress_bar=False)
        return embedding.tolist()
    except Exception as e:
        print(f"✗ Error generating embedding: {e}", file=sys.stderr)
        raise

def generate_embeddings_batch(texts, batch_size=32):
    """Generate embeddings for multiple texts in batches for better performance"""
    try:
        embeddings = model.encode(texts, batch_size=batch_size, show_progress_bar=True)
        return [emb.tolist() for emb in embeddings]
    except Exception as e:
        print(f"✗ Error generating batch embeddings: {e}", file=sys.stderr)
        raise

def create_query_embedding(query):
    """Generate embedding for a query"""
    try:
        embedding = model.encode(query, show_progress_bar=False)
        return embedding.tolist()
    except Exception as e:
        print(f"✗ Error generating query embedding: {e}", file=sys.stderr)
        raise