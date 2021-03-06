import sys
import csv
import datetime
from pymongo import MongoClient
import AnalysisAPI

client = MongoClient('mongodb://william:lemons@ds023475.mlab.com:23475/profild')

"""
	Notes: The number of tweets taken from the user must be compared with 
	an equal (or close to equal) number of tweets from the candidate. Or else
	the number will be skewed. 

	USAGE: python Candidates.py User_Twitter_Handle Political_Candidate_First_Name

	dictionary = {c^username/hillary: 45.01}

	LEFT TO DO:

	- Make "CACHE" script to recognize the regular expression for repetition to prevent
	overloading the twitter API.

	- Single tweet analysis.


"""

def Main():

	#arr = []
	#twitterHandle = sys.argv[1]
	#csvFile = open("bernie.csv", "wb")
	#AnalysisAPI.pullTweets(arr, twitterHandle)
	#AnalysisAPI.writeToFile(csvFile, arr)

	twitterHandle = sys.argv[1]
	politicalCandidate = "Tweet_Analysis/" + sys.argv[2] + ".csv"
	userTweets = []
	csvFile = open("Tweet_Analysis/user.csv", "wb")

	try:
		AnalysisAPI.pullTweets(userTweets, twitterHandle)
	except:
		print "Error: USER NOT FOUND!"
		return 0

	AnalysisAPI.writeToFile(csvFile, userTweets)
	csvFile.close()
	
	userDictionary ={}
	userArray = []

	candidateDictionary = AnalysisAPI.parseCSV_Dictionary(politicalCandidate)

	candidateArray = AnalysisAPI.parseCSV_Vector(politicalCandidate)

	userArray = AnalysisAPI.parseCSV_Vector("Tweet_Analysis/user.csv")

	userDictionary = AnalysisAPI.createUserDictionary(candidateDictionary, candidateArray, userArray)

	#userArray = AnalysisAPI.parseCSV_Vector("donny.csv")

	#userDictionary = AnalysisAPI.createUserDictionary(candidateDictionary, candidateArray, userArray)

	AnalysisAPI.WordAnalysis(userDictionary, len(userArray), userArray)

	similarity = AnalysisAPI.cosineSimilarity(AnalysisAPI.vectorDotProduct(candidateArray, candidateDictionary, userDictionary), AnalysisAPI.vectorNorm(candidateArray, candidateDictionary), AnalysisAPI.vectorNorm(candidateArray, userDictionary))
	#print similarity

	print round(similarity * 100, 2)
	similarity = round(similarity * 100, 2)
	#return round(similarity * 100, 2)

	timestamp = datetime.datetime.now()
	db = client.profild
	dbkey = "c^" + sys.argv[1] + "/" + sys.argv[2]
	result = db.results.insert_one({
				"key": dbkey, 
				"percentage": similarity,
				"candidate": sys.argv[2], 
				"user": sys.argv[1], 
				"dateAdded": timestamp
			  })
	
	print("Task completed.")

Main()
