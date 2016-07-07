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

#def DeterminerCount(TweetArray):
	#generalDeterminers = ["the", "a", "an", "another", "no" , "'s", "my", "our", "their", "her"
	#				, "his", "its", "each", "this", "that"]
	#neutralDeterminers = ["certain", "there exist", "some of", "some"]
	#absoluteDeterminers = ["any", "all", "every"]


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

