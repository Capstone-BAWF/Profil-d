import sys

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

