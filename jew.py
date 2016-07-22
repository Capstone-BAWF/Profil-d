import sys
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.newDb
collection = db.testCollection

test = {"message" : "You're a jew!" }

test_id = collection.insert_one(test).inserted_id

