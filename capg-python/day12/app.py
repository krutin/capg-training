from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')

db = client['cmr']

collection = db['books']

def read():
    print("doc in collections")
    for doc in collection.find():
        print(doc)

read()
        

def create():
    data = {
        "name": "Charlie",
        "age": 28,
        "city": "Chennai",
        "email": "charlie@example.com",
        "isActive": True  # Use True instead of 'true'
    }
    result = collection.insert_one(data)
    print(result)
# create()

