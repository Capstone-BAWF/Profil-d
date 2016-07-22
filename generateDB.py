import os
import sys
import time
import tweepy
from pymongo import MongoClient 

client = MongoClient()
db = client.tweetLibrary
collection = db.Tweets

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
def add_tweets(arr, name):
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=name).items(10):
        arr.append(tweet)

clinton = []
add_tweets(clinton,"HillaryClinton")

'''
bernie = []
add_tweets(bernie,"BernieSanders")

trump = []
add_tweets(trump,"realDonaldTrump")
'''

def write_to_file(openfile,arr):
    openfile.write("name,time,tweets\n")
    for tweet in arr:
        openfile.write(tweet.user.name + ',' + str(tweet.created_at) + ',' + tweet.text.replace(',','',20).replace('\n',' ',20).replace('.','',20) +'\n')

hilfile = open("hillary.csv","wb")
write_to_file(hilfile,clinton)
hilfile.close()

'''
bernfile = open("csvs/bernie.csv","wb")
write_to_file(bernfile,bernie)
bernfile.close()

trumpfile = open("csvs/donny.csv","wb")
write_to_file(trumpfile,trump)
trumpfile.close()
#    print(word.text)
'''
