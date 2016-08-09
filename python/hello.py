import sys
from pymongo import MongoClient

def main(argv):
	
	client = MongoClient('mongodb://localhost:27017/newDb')
	db = client.newDb
	collection = db.results

	testMessage = 1240
	test = {"percentage" : testMessage }

	print sys.argv[1]

	test_id = collection.insert_one(test).inserted_id
	
	print("Function ran.")

if __name__ == "__main__":
	main(sys.argv[1])
