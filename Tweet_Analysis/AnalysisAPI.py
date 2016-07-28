import sys
import csv
import tweepy
from math import log

__author__ = "Brandon Troche"
__copyright__ = "Copyright 2016, Profil-d"
__credits__ = ["Brandon Troche", "William Wu", 
               "Ada Chen", "Fabio Francios", "Felix Grezes"]
__maintainer__ = "Brandon Troche"
__email__ = "bttroche@gmail.com"

reload(sys)
sys.setdefaultencoding('utf-8')


"""
-	Compare two cvs's to each other. Say Hillary to Bernie and try to see how similar they are
-	Overall percentage for comparisons
-	Show buzz words/topics that you share with a candidate
-   bigrams and trigram
-   cosine similarity
"""

def parseCSV(nameOfCSV):
	csvfile = open(nameOfCSV, 'r')
	reader = csv.DictReader(csvfile, fieldnames = ("name", "time", "tweets"))

	Tweet = ""
	wordsDictionary = {}

	for row in reader:
		TweetTweet = str("").join(str(row['tweets']))

		Tweet = TweetTweet
		tweetArray = Tweet.split()
		tweetSize = len(tweetArray)


		WordAnalysis(wordsDictionary, tweetSize, tweetArray)

	csvfile.close()

	return wordsDictionary

def createArray(SemanticDictionary):
	wordsArray = []

	for keys in SemanticDictionary:
		wordsArray.append(keys)

	copyDict = SemanticDictionary.copy()

	wordsArray = sortArray(wordsArray, copyDict)

	stopWordsFilter(wordsArray)


	return wordsArray



def WordAnalysis(SemanticDictionary, Size, TweetArray):
	for i in range(Size):
		if(SemanticDictionary.has_key(TweetArray[i].lower())):
			SemanticDictionary[TweetArray[i].lower()] += 1
		else: 
			SemanticDictionary[TweetArray[i].lower()] = 1

def mostUsed(numberOfMostUsed, termArray, SemanticDictionary):
	for terms in range(numberOfMostUsed):
		print "The term '%s' appeared '%s' times." % (termArray[len(termArray) - terms - 1], checkTerm(termArray[len(termArray) - terms - 1], SemanticDictionary))

def checkTerm(Term, SemanticDictionary):
	return SemanticDictionary[Term]

def highestTerm(SemanticDictionary):
	tempLargest = 0
	tempString = "All equally used"
	for i in SemanticDictionary:
		if SemanticDictionary[i] > tempLargest:
			tempLargest = SemanticDictionary[i]
			tempString = i
	del SemanticDictionary[tempString]
	return tempString

def sortArray(termArray, SemanticDictionary):
	sortedArray = []
	for objs in termArray:
		sortedArray.insert(0, highestTerm(SemanticDictionary))
	return sortedArray

def pullTweets(arr, name):
	consumer_token = '9VvsBn2c4Q5wBSoA3MsBZLbFp'
	consumer_secret = 'bVPdCJWsjw6Q75UO6FqSPYLJottjbj0Q4kkO46PjyLhlbqp9Il'
	auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
	api = tweepy.API(auth)

	for tweet in tweepy.Cursor(api.user_timeline, screen_name=name).items(10):
		arr.append(tweet)

def writeToFile(openfile,arr):
    openfile.write("name,time,tweets\n")
    for tweet in arr:
        openfile.write(tweet.user.name + ',' + \
        str(tweet.created_at) + ',' + tweet.text.replace(',','',20).replace('\n',' ',20).replace('.','',20).replace('-',' ',20) +'\n')

def termDocWeight(termFrequencyInDoc, totalTermsInDoc, termFreqInCorpus, totalDocs):
	tf = float(termFrequencyInDoc) / float(totalTermsInDoc) 
	docFreq = totalDocs / termFreqInCorpus 
	idf = log(docFreq)

	return tf*idf

def stopWordsFilter(termArray):
	stopWordList = "a about above after again against all am an and any are \
	aren't as at be because been before being below between both but by can't \
	cannot could couldn't did didn't do does doesn't doing don't down during each \
	few for from further had hadn't has hasn't have haven't having he he'd he'll he's\
	 her here here's hers herself him himself his how how's i i'd i'll i'm i've if in \
	 into is isn't it it's its itself let's me more most mustn't my myself no nor not of \
	 off on once only or other ought our ours ourselves out over own same shan't she she'd \
	 she'll she's should shouldn't so some such than that that's the their theirs them \
	 themselves then there there's these they they'd they'll they're they've this those \
	 through to too under until up very was wasn't we we'd we'll we're we've were weren't \
	 what what's when when's where where's which while who who's whom why why's with won't \
	 would wouldn't you you'd you'll you're you've your yours yourself yourselves just can de la"

	stopWords = []
	stopWords = stopWordList.split()
	toRemove = []
	for term in termArray:
		for wordz in stopWords:
			if(term == wordz):
				toRemove.append(term)

	for objects in toRemove:
		termArray.remove(objects)

def stemming(termArray):
	return 0
