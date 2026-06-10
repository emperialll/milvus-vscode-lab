from pymilvus import connections

CONNECTION_ID = "learn"

connections.connect(
    alias=CONNECTION_ID,
    host="127.0.0.1",
    port="19530",
)

print("Connected!")
