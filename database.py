from pymilvus import db
from main import CONNECTION_ID

current_dbs = db.list_database(using=CONNECTION_ID)
print("Current databases: ", current_dbs)

DB_NAME = "course_db"

if DB_NAME not in current_dbs:
    print("Creating database: ", DB_NAME)
    wiki_db = db.create_database(DB_NAME, using=CONNECTION_ID)

db.using_database(DB_NAME, using=CONNECTION_ID)
