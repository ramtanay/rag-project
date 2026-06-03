from fastembed import TextEmbedding
import sys

model = None


def get_model():
    global model

    if model is None:
        print("Loading FastEmbed model...", file=sys.stderr)

        model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )

        print("FastEmbed model loaded!", file=sys.stderr)

    return model


def generate_embedding(text):
    embedding_model = get_model()

    embedding = list(embedding_model.embed([text]))[0]

    return embedding.tolist()


def generate_embeddings_batch(texts, batch_size=32):
    embedding_model = get_model()

    embeddings = list(embedding_model.embed(texts))

    return [emb.tolist() for emb in embeddings]


def create_query_embedding(query):
    embedding_model = get_model()

    embedding = list(embedding_model.embed([query]))[0]

    return embedding.tolist()