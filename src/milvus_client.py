from pymilvus import MilvusClient

from config import MILVUS_URI, DATABASE_NAME


def get_milvus_client(db_name: str = DATABASE_NAME) -> MilvusClient:
    return MilvusClient(
        uri=MILVUS_URI,
        db_name=db_name,
    )
