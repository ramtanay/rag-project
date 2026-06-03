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

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []
    seen = set()

    for idx in indices[0]:

        if idx < len(stored_chunks):

            chunk = stored_chunks[idx]

            if chunk not in seen:
                results.append(chunk)
                seen.add(chunk)

    return results