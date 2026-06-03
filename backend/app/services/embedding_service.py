from sentence_transformers import SentenceTransformer
import sys

model = None


def get_model():
    """
    Load model only when needed.
    Prevents Render from consuming memory during startup.
    """
    global model

    if model is None:
        try:
            print("⏳ Loading embedding model...", file=sys.stderr)

            model = SentenceTransformer("all-MiniLM-L6-v2")

            print("✓ Embedding model loaded successfully", file=sys.stderr)

        except Exception as e:
            print(f"✗ Error loading embedding model: {e}", file=sys.stderr)
            raise

    return model


def generate_embedding(text):
    """Generate embedding for a single text"""

    try:
        embedding_model = get_model()

        embedding = embedding_model.encode(
            text,
            show_progress_bar=False
        )

        return embedding.tolist()

    except Exception as e:
        print(f"✗ Error generating embedding: {e}", file=sys.stderr)
        raise


def generate_embeddings_batch(texts, batch_size=32):
    """Generate embeddings for multiple texts"""

    try:
        embedding_model = get_model()

        embeddings = embedding_model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=False
        )

        return embeddings.tolist()

    except Exception as e:
        print(f"✗ Error generating batch embeddings: {e}", file=sys.stderr)
        raise


def create_query_embedding(query):
    """Generate embedding for a user query"""

    try:
        embedding_model = get_model()

        embedding = embedding_model.encode(
            query,
            show_progress_bar=False
        )

        return embedding.tolist()

    except Exception as e:
        print(f"✗ Error generating query embedding: {e}", file=sys.stderr)
        raise