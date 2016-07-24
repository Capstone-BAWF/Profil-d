import sys
import csv
from math import log
from pymongo import MongoClient 
import AnalysisAPI

def Main():

	myDictionary = {}
	myArray = ["This", "That", "This", "My", "Something"]

	AnalysisAPI.WordAnalysis(myDictionary, len(myArray), myArray)

	print myDictionary



Main()