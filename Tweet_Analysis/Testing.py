#import os
import sys
import csv
#import time
#import tweepy
#from pymongo import MongoClient 

"""
-	Compute tf-idf using tf and df as separate tweets instead of separate documents
-	Filter out all the non-important words
-	Compare two cvs's to each other. Say Hillary to Bernie and try to see how similar they are
-	Group together all the stemmed words
"""

def main():

	csvfile = open('hillary.csv', 'r')

	reader = csv.DictReader(csvfile, fieldnames = ("name", "time", "tweets"))

	Tweet = ""

	wordsDictionary = {}
	wordsArray = []

	for row in reader:
		#print(', '.join(str(row)))
		#print(row['name'], row['time'], row['tweet'])
		#TweetName = str("").join(str(row['name']))
		#TweetTime = str("").join(str(row['time']))
		TweetTweet = str("").join(str(row['tweets']))

		#print TweetName
		#print TweetTime
		#print TweetTweet

		Tweet = TweetTweet
		tweetArray = Tweet.split()
		tweetSize = len(tweetArray)


		WordAnalysis(wordsDictionary, tweetSize, tweetArray)

	for keys in wordsDictionary:
		wordsArray.append(keys)

	copyDict = wordsDictionary.copy()

	wordsArray = sortArray(wordsArray, copyDict)



	#print wordsDictionary;
	#print "The most used word is: " + str(highestTerm(wordsDictionary)) + ", at: " + str(wordsDictionary[highestTerm(wordsDictionary)])
	print "The number of unique words used was: " + str(len(wordsDictionary))
	print "The number of unique words in our array is: " + str(len(wordsArray))

	print wordsArray[0]
	print wordsArray[149]
	print checkTerm(wordsArray[149], wordsDictionary)

	print "The 20 most used words were: "
	mostUsed(20, wordsArray, wordsDictionary)
	print "After filtering the 20 most used words were: "
	#print len(wordsArray)
	stopWordsFilter(wordsArray)
	#print len(wordsArray)
	mostUsed(20, wordsArray, wordsDictionary)

	csvfile.close()

	#print(reader)

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


def termDocWeight(termFrequencyInDoc, totalTermsInDoc, termFreqInCorpus, totalDocs):
	tf = termFrequencyInDoc.toDouble / totalTermsInDoc 
	docFreq = totalDocs.toDouble / termFreqInCorpus 
	idf = math.log(docFreq)
	return tf*idf

def stopWordsFilter(termArray):
	stopWordList = "a about above after again against all am an and any are aren't as at be because been before being below between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves out over own same shan't she she'd she'll she's should shouldn't so some such than that that's the their theirs them themselves then there there's these they they'd they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself yourselves"
	stopWords = []
	stopWords = stopWordList.split()
	toRemove = []
	#print(len(stopWords))
	for term in termArray:
		for wordz in stopWords:
			if(term == wordz):
				#print term 
				#print wordz
				toRemove.append(term)

	for objects in toRemove:
		termArray.remove(objects)

"""  
import edu.stanford.nlp.pipeline._
import edu.stanford.nlp.ling.CoreAnnotations._

def createNLPPipeline(): StanfordCoreNLP = {
	val props = new Properties()
	props.put("annotators", "tokenize, ssplit, pos, lemma") new StanfordCoreNLP(props)
}

def isOnlyLetters(str: String): Boolean = { 

	str.forall(c => Character.isLetter(c))

}

def plainTextToLemmas(text: String, stopWords: Set[String], pipeline: StanfordCoreNLP): Seq[String] = {
	val doc = new Annotation(text) pipeline.annotate(doc)
	val lemmas = new ArrayBuffer[String]()
	val sentences = doc.get(classOf[SentencesAnnotation]) 
	for (sentence <- sentences; token <- sentence.get(classOf[TokensAnnotation])): 
		val lemma = token.get(classOf[LemmaAnnotation])
		if (lemma.length > 2 && !stopWords.contains(lemma) && isOnlyLetters(lemma)):
        	lemmas += lemma.toLowerCase
 	return lemmas
}

val stopWords = sc.broadcast(
scala.io.Source.fromFile("stopwords.txt).getLines().toSet).value
val lemmatized: RDD[Seq[String]] = plainText.mapPartitions(it => { val pipeline = createNLPPipeline()
it.map { case(title, contents) =>
        plainTextToLemmas(contents, stopWords, pipeline)
      }
})
"""

#def DeterminerCount(TweetArray):
	#generalDeterminers = ["the", "a", "an", "another", "no" , "'s", "my", "our", "their", "her"
	#				, "his", "its", "each", "this", "that"]
	#neutralDeterminers = ["certain", "there exist", "some of", "some"]
	#absoluteDeterminers = ["any", "all", "every"]


main()

