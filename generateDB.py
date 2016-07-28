import csv
import json
import os
import pandas as pd
import sys
import time
import tweepy
from pymongo import MongoClient 

client = MongoClient()
db = client.tweetLibrary

collection_B = db.collection_bern
collection_D = db.collection_donny
collection_H = db.collection_hill

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

#this prints out the handle, username, and post date of the tweet selected
def print_tweet(tweet):
    print "@%s - %s (%s)" % (tweet.user.screen_name, tweet.user.name, tweet.created_at)
    print tweet.text

#lesvivants
def get_user_tweets(arr):
    if(len(sys.argv) > 1):
        username = str(sys.argv[1])
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=username).items(10):
            arr.append(tweet)

#change the value in items to choose the number of tweets to retrieve for this request
def add_tweets(arr, name):
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=name).items(10):
        arr.append(tweet)

clinton = []
add_tweets(clinton,"HillaryClinton")

bernie = []
add_tweets(bernie,"BernieSanders")

trump = []
add_tweets(trump,"realDonaldTrump")

#writing array of tweets to file
def write_to_file(openfile,arr):
    openfile.write("name,time,tweets\n")
    for tweet in arr:
        openfile.write(tweet.user.name + ',' + \
        str(tweet.created_at) + ',' + tweet.text.replace(',',' ',20).replace('\n',' ',20).replace('.',' ',20).replace('-',' ',20) +'\n')

hilfile = open("csvs/hillary.csv","r+")
write_to_file(hilfile,clinton)

bernfile = open("csvs/bernie.csv","r+")
write_to_file(bernfile,bernie)

trumpfile = open("csvs/donny.csv","r+")
write_to_file(trumpfile,trump)

#csv to json
data_B = pd.read_csv(bernfile, quoting=csv.QUOTE_NONE)
data_D = pd.read_csv(hilfile, quoting=csv.QUOTE_NONE)
data_H = pd.read_csv(trumpfile, quoting=csv.QUOTE_NONE)

data_Bjson = json.loads(data_B.to_json(orient = 'records'))
data_Djson = json.loads(data_D.to_json(orient = 'records'))
data_Hjson = json.loads(data_H.to_json(orient = 'records'))

#insert jsons into mongoDB collections
collection_B.insert(data_Bjson)
collection_D.insert(data_Djson)
collection_H.insert(data_Hjson)
