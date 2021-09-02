import certifi
import pymongo
import os

client = ''
if os.getenv("RUN_ENV") == "PROD":
    connection = "mongodb+srv://python:{password}@futureofsecurity.oxjap.mongodb.net/future-content?retryWrites=true&w" \
             "=majority "
    password = os.getenv("MONGO_PASSWORD")
    connection.format(password=password)
    client = pymongo.MongoClient(
        connection,
        tlsCAFile=certifi.where())

else:
    client = pymongo.MongoClient('localhost', 27017)

db = client["future-content"]
col = db["content"]


# Creates Page on MongoDB
def create_page(cont_id):
    item = {"_id": cont_id, "content": "Basic"}
    col.insert_one(item)


# Retrieves Page
def get_page(cont_id):
    q = {"_id": cont_id}
    return col.find_one(q)
