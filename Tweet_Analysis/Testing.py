#import os
import sys
import csv
#import time
#import tweepy
#from pymongo import MongoClient 

def main():
	Tweet = ""
	while Tweet == "" or len(Tweet) > 150:
		Tweet = raw_input("You should totally enter a tweet brah: ")
	print(Tweet)
	if len(Tweet) > 150:
		print("Sorry that's not a tweet!")

	words = {}

	twitters = Tweet.split()
	tweetSize = len(twitters)

	print ("The size of the array is: " + str(tweetSize))
	print(twitters)
	print (len(Tweet))

	print ("The number of times each word was used: ")
	WordAnalysis(words, tweetSize, twitters)
	print ("The word that appeared the most was: " + WordCount(words))


	"""for index in twitters:
	print(index)"""



def WordAnalysis(SemanticDictionary, Size, TweetArray):
	for i in range(Size):
		if(SemanticDictionary.has_key(TweetArray[i])):
			SemanticDictionary[TweetArray[i]] += 1
		else: 
			SemanticDictionary[TweetArray[i]] = 1
	print SemanticDictionary

def WordCount(SemanticDictionary):
	tempLargest = 1
	tempString = "All equally used"
	for i in SemanticDictionary:
		if SemanticDictionary[i] > tempLargest:
			tempLargest = SemanticDictionary[i]
			tempString = i
	return tempString

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

