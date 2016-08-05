import sys
import csv
from pymongo import MongoClient
import AnalysisAPI


#client = MongoClient('mongodb://local_host')
"""
	Notes: The number of tweets taken from the user must be compared with 
	an equal (or close to equal) number of tweets from the candidate. Or else
	the number will be skewed. 
"""

def Main():

	
	twitterHandle = sys.argv[1]
	politicalCandidate = sys.argv[2]
	politicalCandidate += ".csv"
	userTweets = []
	csvFile = open("user.csv", "wb")

	
	AnalysisAPI.pullTweets(userTweets, twitterHandle)
	AnalysisAPI.writeToFile(csvFile, userTweets)
	csvFile.close()
	
	userDictionary ={}
	userArray = []

	candidateDictionary = AnalysisAPI.parseCSV_Dictionary(politicalCandidate)

	candidateArray = AnalysisAPI.parseCSV_Vector(politicalCandidate)

	userArray = AnalysisAPI.parseCSV_Vector("user.csv")

	userDictionary = AnalysisAPI.createUserDictionary(candidateDictionary, candidateArray, userArray)

	#userArray = AnalysisAPI.parseCSV_Vector("donny.csv")

	#userDictionary = AnalysisAPI.createUserDictionary(candidateDictionary, candidateArray, userArray)

	AnalysisAPI.WordAnalysis(userDictionary, len(userArray), userArray)

	similarity = AnalysisAPI.cosineSimilarity(AnalysisAPI.vectorDotProduct(candidateArray, candidateDictionary, userDictionary), AnalysisAPI.vectorNorm(candidateArray, candidateDictionary), AnalysisAPI.vectorNorm(candidateArray, userDictionary))
	print similarity
	print round(similarity * 100, 2)

	return round(similarity * 100, 2)


Main()
