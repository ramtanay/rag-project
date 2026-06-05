import faiss
import numpy as np

dimension = 384

# Global vector store
index = faiss.IndexFlatL2(dimension)
stored_chunks = []


def reset_vector_store():
    """
    Clear previous document data.
    Call this before storing a new PDF.
    """
    global index
    global stored_chunks

    index = faiss.IndexFlatL2(dimension)
    stored_chunks = []

    print("✓ Vector store reset")


def store_embeddings(chunks, embeddings):
    """
    Store embeddings for the latest uploaded document.
    Previous document data is removed.
    """
    global index
    global stored_chunks

    # Reset old document
    reset_vector_store()

    embeddings = np.array(embeddings).astype("float32")

    index.add(embeddings)
    stored_chunks.extend(chunks)

    print(f"✓ Stored {len(chunks)} chunks")
    print(f"✓ Total chunks in store: {len(stored_chunks)}")


def search_similar_chunks(query_embedding, top_k=5):
    """
    Retrieve the most relevant chunks.
    """

    if len(stored_chunks) == 0:
        return []

    top_k = min(top_k, len(stored_chunks))

    query_embedding = np.array(
        [query_embedding],
        dtype=np.float32
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:
        if 0 <= idx < len(stored_chunks):
            results.append(stored_chunks[idx])

    return results