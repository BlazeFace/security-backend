import certifi
import pymongo
import os

client = ''

if os.getenv("RUN_ENV") != "PROD":
    username = "python"
    password = os.getenv("MONGO_PASSWORD")
    if type(password) is None:
        pass_file = open("/etc/secrets/password", "r")
        password = pass_file.read()
        pass_file.close()
        user_file = open("/etc/secrets/username", "r")
        username = user_file.read()
        user_file.close()
    connection = "mongodb+srv://{}:{}@futureofsecurity.oxjap.mongodb.net/future-content?retryWrites=true&w" \
             "=majority".format(username, password)
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
