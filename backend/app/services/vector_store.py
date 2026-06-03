import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

stored_chunks = []


def store_embeddings(chunks, embeddings):

    global stored_chunks

    embeddings = np.array(embeddings).astype("float32")

    index.add(embeddings)

    stored_chunks.extend(chunks)


def search_similar_chunks(query_embedding, top_k=5):

    available_chunks = len(stored_chunks)

    top_k = min(top_k, available_chunks)

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        if idx < len(stored_chunks):
            results.append(stored_chunks[idx])

    return results