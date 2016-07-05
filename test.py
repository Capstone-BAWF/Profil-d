import os
import sys
import time
import tweepy
from pymongo import MongoClient 

client = MongoClient()
db = client.test

reload(sys)
sys.setdefaultencoding('utf-8')

consumer_token = '9VvsBn2c4Q5wBSoA3MsBZLbFp'
consumer_secret = 'bVPdCJWsjw6Q75UO6FqSPYLJottjbj0Q4kkO46PjyLhlbqp9Il'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

api = tweepy.API(auth)

#api.search returns the most recent 15 tweets for the search criteria
#results = api.search(q="crepes")

'''
api.user_timeline by default give the 20 most recent tweets of the user
that registered the api. add a username to search so we dont pull Will's tweets
'''
#results = api.user_timeline(screen_name="realDonaldTrump")

#this would print out 15 if using default search function
#print len(results)

#this prints out the handle, username, and post date of the tweet selected
def print_tweet(tweet):
    print "@%s - %s (%s)" % (tweet.user.screen_name, tweet.user.name, tweet.created_at)
    print tweet.text

#tweet=results[1]
#print_tweet(tweet)

#change the value in items to choose the number of tweets to retrieve for this request
clinton = []
for tweet in tweepy.Cursor(api.user_timeline, screen_name="HillaryClinton").items(1000):
    clinton.append(tweet)
    
bernie = []
for tweet in tweepy.Cursor(api.user_timeline, screen_name="BernieSanders").items(1000):
    bernie.append(tweet)
    
trump = []
for tweet in tweepy.Cursor(api.user_timeline, screen_name="realDonaldTrump").items(1000):
    trump.append(tweet)

#print len(results)

hilfile = open("hillary.csv","wb")
hilfile.write("name,time,tweets\n")
for tweet in clinton:
    hilfile.write(tweet.user.name + ',' + str(tweet.created_at) + ',' + tweet.text +'\n')
hilfile.close()

bernfile = open("bernie.csv","wb")
bernfile.write("name,time,tweets\n")
for tweet in bernie:
    bernfile.write(tweet.user.name + ',' + str(tweet.created_at) + ',' + tweet.text +'\n')
bernfile.close()    
    
trumpfile = open("donny.csv","wb")
trumpfile.write("name,time,tweets\n")
for tweet in trump:
    trumpfile.write(tweet.user.name + ',' + str(tweet.created_at) + ',' + tweet.text +'\n')
trumpfile.close()
#    print(word.text)

