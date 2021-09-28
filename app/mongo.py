import certifi
import pymongo
import os

client = ''

if os.getenv("RUN_ENV") == "PROD":
    password = os.getenv("MONGO_PASSWORD")
    connection = "mongodb+srv://python:{}@futureofsecurity.oxjap.mongodb.net/future-content?retryWrites=true&w" \
             "=majority".format(password)
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

# Add devices_list 
def add_device(device, url):
    col.update(
        { "_id": "device_list"},
        {
            "$push": {
                "title": device,
                "url": url
            }
        }    
        ,{ upsert: true }
    )
