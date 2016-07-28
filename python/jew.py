import sys
from pymongo import MongoClient

def main(argv):
	client = MongoClient('mongodb://localhost:27017/newDb')

	db = client.newDb
	collection = db.testCollection

	testMessage = sys.argv[1] + ' is gay!'
	test = {"message" : testMessage }

	print sys.argv[1]

	test_id = collection.insert_one(test).inserted_id

if __name__ == "__main__":
	main(sys.argv[1])
