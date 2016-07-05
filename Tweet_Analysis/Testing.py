import sys

def TweetAnalysis(SemanticDictionary, Size, TweetArray):
	for i in range(Size):
		if(SemanticDictionary.has_key(TweetArray[i])):
			SemanticDictionary[TweetArray[i]] += 1
		else: 
			SemanticDictionary[TweetArray[i]] = 1
	print SemanticDictionary


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
TweetAnalysis(words, tweetSize, twitters)

"""for index in twitters:
	print(index)"""

