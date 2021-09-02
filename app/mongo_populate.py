import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client["future-content"]
col = db["content"]


item = {"_id":"test-content","device":"iphone","goal":"privacy","issue":"none","content":{"title":"Turn Off Location","sub-title":"Any Thing","diff":"easy","para":"Hello world"}}
col.insert_one(item)