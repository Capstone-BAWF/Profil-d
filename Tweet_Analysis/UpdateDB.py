import sys
import csv
import datetime
import AnalysisAPI

def main(argv):
	candidateList = [{"twitter": "realDonaldTrump", "csvName": "donny.csv"},
					 {"twitter": "hillaryclinton", "csvName": "hillary.csv"},
					 {"twitter": "berniesanders", "csvName": "bernie.csv"}]
	candidateArr = []
	
	for candidate in candidateList:
		csvFile = open("Tweet_Analysis/" + candidate['csvName'], "wb")
		AnalysisAPI.pullTweets(candidateArr, candidate['twitter'])
		AnalysisAPI.writeToFile(csvFile, candidateArr)
		csvFile.close()

if __name__ == "__main__":
	main(sys.argv[1:])
