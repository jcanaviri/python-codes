from pymongo import MongoClient


uri = "mongodb://localhost:27017"

client = MongoClient(uri)

db = client["test_db"]

collection = db.test_collection

collection.insert_one({"hello": "word"})

print(collection.find_one())
