import sys
import csv
from math import log
from pymongo import MongoClient 
import AnalysisAPI


#client = MongoClient('mongodb://local_host')



def Main():

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



Main()