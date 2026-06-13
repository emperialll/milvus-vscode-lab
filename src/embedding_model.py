from pymilvus import model as milvus_model


def get_embedding_model():
    return milvus_model.DefaultEmbeddingFunction()


def embed_documents(texts: list[str]) -> list[list[float]]:
    embedding_model = get_embedding_model()
    embeddings = embedding_model.encode_documents(texts)

    return [embedding.tolist() for embedding in embeddings]
