from pymilvus import DataType, MilvusClient
from pymilvus import model as milvus_model

from config import COLLECTION_NAME
from milvus_client import get_milvus_client


def get_embedding_dimension() -> int:
    embedding_model = milvus_model.DefaultEmbeddingFunction()
    test_embedding = embedding_model.encode_queries(["This is a test"])[0]

    return len(test_embedding)


def main() -> None:
    client = get_milvus_client()

    embedding_dimension = get_embedding_dimension()
    print(f"Detected embedding dimension: {embedding_dimension}")

    if client.has_collection(collection_name=COLLECTION_NAME):
        print(f"Collection already exists: {COLLECTION_NAME}")
        print(client.describe_collection(collection_name=COLLECTION_NAME))
        return

    schema = MilvusClient.create_schema(
        auto_id=False,
        enable_dynamic_field=False,
    )

    schema.add_field(
        field_name="course_id",
        datatype=DataType.INT64,
        is_primary=True,
    )

    schema.add_field(
        field_name="title",
        datatype=DataType.VARCHAR,
        max_length=256,
    )

    schema.add_field(
        field_name="description",
        datatype=DataType.VARCHAR,
        max_length=2048,
    )

    schema.add_field(
        field_name="description_embedding",
        datatype=DataType.FLOAT_VECTOR,
        dim=embedding_dimension,
    )

    client.create_collection(
        collection_name=COLLECTION_NAME,
        schema=schema,
    )

    print(f"Collection created: {COLLECTION_NAME}")
    print(client.describe_collection(collection_name=COLLECTION_NAME))


if __name__ == "__main__":
    main()
