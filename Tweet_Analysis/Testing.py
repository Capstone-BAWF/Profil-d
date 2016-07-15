#import os
import sys
import csv
#import time
#import tweepy
#from pymongo import MongoClient 

def main():

	csvfile = open('hillary_2.csv', 'r')

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

	csvfile.close()

	#print(reader)

def WordAnalysis(SemanticDictionary, Size, TweetArray):
	for i in range(Size):
		if(SemanticDictionary.has_key(TweetArray[i].lower())):
			SemanticDictionary[TweetArray[i].lower()] += 1
		else: 
			SemanticDictionary[TweetArray[i].lower()] = 1

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

