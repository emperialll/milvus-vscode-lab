from milvus_client import get_milvus_client

DATABASE_NAME = "course_db"


def main() -> None:
    client = get_milvus_client()

    databases = client.list_databases()
    print("Databases before:", databases)

    if DATABASE_NAME not in databases:
        client.create_database(db_name=DATABASE_NAME)
        print(f"Database created: {DATABASE_NAME}")
    else:
        print(f"Database already exists: {DATABASE_NAME}")

    client.use_database(DATABASE_NAME)
    print(f"Now using database: {DATABASE_NAME}")

    databases = client.list_databases()
    print("Databases after:", databases)


if __name__ == "__main__":
    main()
