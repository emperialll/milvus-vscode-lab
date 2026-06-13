from pymilvus import __version__
from milvus_client import get_milvus_client


def main() -> None:
    print(f"PyMilvus version: {__version__}")

    client = get_milvus_client()

    databases = client.list_databases()

    print("Connected to Milvus successfully.")
    print("Available databases:", databases)


if __name__ == "__main__":
    main()
