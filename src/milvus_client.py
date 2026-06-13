from pymilvus import MilvusClient

from config import MILVUS_URI


def get_milvus_client() -> MilvusClient:
    return MilvusClient(uri=MILVUS_URI)
