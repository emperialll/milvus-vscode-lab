from pymilvus import MilvusClient, __version__


MILVUS_URI = "http://127.0.0.1:19530"


def main() -> None:
    print(f"PyMilvus version: {__version__}")

    client = MilvusClient(uri=MILVUS_URI)

    databases = client.list_databases()

    print("Connected to Milvus successfully.")
    print("Available databases:", databases)


if __name__ == "__main__":
    main()
