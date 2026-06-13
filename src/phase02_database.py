from pymilvus import MilvusClient

from config import DATABASE_NAME, MILVUS_URI


def main() -> None:
    client = MilvusClient(uri=MILVUS_URI)

    databases = client.list_databases()
    print("Databases before:", databases)

    if DATABASE_NAME not in databases:
        client.create_database(db_name=DATABASE_NAME)
        print(f"Database created: {DATABASE_NAME}")
    else:
        print(f"Database already exists: {DATABASE_NAME}")

    client.using_database(DATABASE_NAME)
    print(f"Now using database: {DATABASE_NAME}")

    print("Databases after:", client.list_databases())


if __name__ == "__main__":
    main()
