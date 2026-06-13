import csv
from pathlib import Path

from config import COLLECTION_NAME
from embedding_model import embed_documents
from milvus_client import get_milvus_client


DATA_FILE = Path("data/course-descriptions.csv")


def load_course_rows() -> list[dict]:
    courses = []

    with DATA_FILE.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            courses.append(
                {
                    "course_id": int(row["Course ID"]),
                    "title": row["Title"],
                    "description": row["Description"],
                }
            )

    return courses


def prepare_entities(courses: list[dict]) -> list[dict]:
    descriptions = [course["description"] for course in courses]
    embeddings = embed_documents(descriptions)

    entities = []

    for course, embedding in zip(courses, embeddings):
        entities.append(
            {
                "course_id": course["course_id"],
                "title": course["title"],
                "description": course["description"],
                "description_embedding": embedding,
            }
        )

    return entities


def main() -> None:
    client = get_milvus_client()

    courses = load_course_rows()
    entities = prepare_entities(courses)

    result = client.insert(
        collection_name=COLLECTION_NAME,
        data=entities,
    )

    print("Insert result:", result)

    stats = client.get_collection_stats(collection_name=COLLECTION_NAME)
    print("Collection stats:", stats)


if __name__ == "__main__":
    main()
