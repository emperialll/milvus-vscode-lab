from pymilvus import db
from connection import CONNECTION_ID

DB_NAME = "course_db"

current_dbs = db.list_database(using=CONNECTION_ID)
print("Current databases:", current_dbs)

if DB_NAME not in current_dbs:
    print("Creating database:", DB_NAME)
    db.create_database(DB_NAME, using=CONNECTION_ID)

db.using_database(DB_NAME, using=CONNECTION_ID)

print("Using database:", DB_NAME)
