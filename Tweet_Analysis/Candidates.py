import sys
import csv
import math
from pymongo import MongoClient
import AnalysisAPI


#client = MongoClient('mongodb://local_host')

"""
	[:To Do:]

	- Create proper term vectors
	- Dot product between vectors
	- Vector norm calculation 
	- Implement the formula for cosine similarity 
		arccos^-1 [ ( dot-product of vector a and vector b ) / sqrt( vector_normA * vector_normB ) ]
	- Implement the analysis of the directive similarity of vectors 

"""



def Main():

	#cos_sin = 0.8215838362577491

	#first = 9.0
	#second = 120.0

	#third = first/math.sqrt(second)

	#print math.acos(cos_sin)
	#print math.degrees(math.acos(third))

	"""
	twitterHandle = sys.argv[1]
	userTweets = []
	csvFile = open("user.csv", "wb")

	AnalysisAPI.pullTweets(userTweets, twitterHandle)
	AnalysisAPI.writeToFile(csvFile, userTweets)
	csvFile.close()

	userDictionary ={}
	userArray = []

	print "_______________________________________________________\n   USER:"

	userDictionary = AnalysisAPI.parseCSV_Dictionary("user.csv")
	#userArray = AnalysisAPI.createArray(userDictionary)
	userArray = AnalysisAPI.parseCSV_Vector("user.csv")

	print userArray
	print AnalysisAPI.checkTerm("jump", userDictionary)

	#AnalysisAPI.mostUsed(20, userArray, userDictionary)
	"""

	hillaryDictionary = AnalysisAPI.parseCSV_Dictionary("hillary_2.csv")

	hillaryArray = AnalysisAPI.parseCSV_Vector("hillary_2.csv")

	userArray = AnalysisAPI.parseCSV_Vector("user.csv")

	userDictionary = AnalysisAPI.createUserDictionary(hillaryDictionary, hillaryArray, userArray)

	AnalysisAPI.WordAnalysis(userDictionary, len(userArray), userArray)

	#print AnalysisAPI.vectorDotProduct(hillaryArray, hillaryDictionary, userDictionary)

	VectorA = ["julie", "loves", "me", "more", "than", "linda", "jane", "likes"]
	DictA = {"julie":1, "loves":2, "me":2, "more":1, "than":1, "linda":1, "jane":0, "likes":0}
	DictB = {"julie":1, "loves":1, "me":2, "more":1, "than":1, "linda":0, "jane":1, "likes":1}

	print AnalysisAPI.vectorDotProduct(VectorA, DictA, DictB)
	print AnalysisAPI.vectorNorm(VectorA, DictA)
	print AnalysisAPI.vectorNorm(VectorA, DictB)
	something = AnalysisAPI.cosineSimilarity(AnalysisAPI.vectorDotProduct(VectorA, DictA, DictB), AnalysisAPI.vectorNorm(VectorA, DictA), AnalysisAPI.vectorNorm(VectorA, DictB))
	print something
	print math.degrees(math.cos(something))

	print "_______________________________________________________"

	print AnalysisAPI.vectorDotProduct(hillaryArray, hillaryDictionary, userDictionary)
	print AnalysisAPI.vectorNorm(hillaryArray, hillaryDictionary)
	print AnalysisAPI.vectorNorm(hillaryArray, userDictionary)
	variable = AnalysisAPI.cosineSimilarity(AnalysisAPI.vectorDotProduct(hillaryArray, hillaryDictionary, userDictionary), AnalysisAPI.vectorNorm(hillaryArray, hillaryDictionary), AnalysisAPI.vectorNorm(hillaryArray, userDictionary))
	print variable
	print math.degrees(math.cos(variable))

	"""
	hillaryDictionary = {}
	hillaryArray = []

	print " HILLARY: "

	#commandLine = str(sys.argv[1])

	hillaryDictionary = AnalysisAPI.parseCSV("hillary.csv")

	hillaryArray = AnalysisAPI.createArray(hillaryDictionary)

	AnalysisAPI.mostUsed(20, hillaryArray, hillaryDictionary)

	
	print "_______________________________________________________"
	print " BERNIE: "

	bernieDictionary = {}
	bernieArray = []

	bernieDictionary = AnalysisAPI.parseCSV("bernie.csv")

	bernieArray = AnalysisAPI.createArray(bernieDictionary)

	AnalysisAPI.mostUsed(20, bernieArray, bernieDictionary)

	
	print "_______________________________________________________"
	print " DONALD DUCK: "

	donnyDictionary = {}
	donnyArray = []

	donnyDictionary = AnalysisAPI.parseCSV("donny.csv")

	donnyArray = AnalysisAPI.createArray(donnyDictionary)

	AnalysisAPI.mostUsed(20, donnyArray, donnyDictionary)
	"""


Main()