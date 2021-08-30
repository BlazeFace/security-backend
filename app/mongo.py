import certifi
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://python:6LCF2Nqg7am5hGqi@futureofsecurity.oxjap.mongodb.net/future-content?retryWrites=true&w=majority",
    tlsCAFile=certifi.where())
db = client["future-content"]
col = db["content"]

# Creates Page on MongoDB
def create_page(cont_id):
    item = {"_id": cont_id, "content": "Basic"}
    col.insert_one(item)


def get_page(cont_id):
    q = {"_id": cont_id}
    return col.find_one(q)

