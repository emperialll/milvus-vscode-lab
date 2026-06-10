from pymilvus import connections

connections.add_connection(
    learn={
        "host": "localhost",
        "port": "19530",
        "username":"",
        "password": ""
    }
)

CONNECTION_ID ="learn"
connections.connect(CONNECTION_ID)


def main():
    pass

if __name__ == "__main__":
    main()
