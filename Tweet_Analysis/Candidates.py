import sys
import csv
from math import log
from pymongo import MongoClient 
import AnalysisAPI

def Main():

	myDictionary = {}
	myArray = []

	#AnalysisAPI.WordAnalysis(myDictionary, len(myArray), myArray)

	myDictionary = AnalysisAPI.parseCSV("hillary.csv")

	myArray = AnalysisAPI.createArray(myDictionary)

	#print myDictionary
	print myArray


Main()