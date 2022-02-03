from pydoc import cli
from typing import Collection
from auth import api
import time
import tweepy
import pymongo
from pymongo import MongoClient

def main():

    #Read the tags from a txt file
    tags = open('tags.txt', 'r')
    rt(tags.read())

def DBstorage(data):
    
    cluster = "mongodb+srv://admin:T3oSvzK0RvMsZdDK@cluster0.mmli1.mongodb.net/sample_airbnb?retryWrites=true&w=majority"

    client = MongoClient(cluster)

    db = client.sample_airbnb

    print(db.list_collection_names())



def rt(tags):
    
    #Store the tags in a variable
    search = tags
    #Set a number of tweets to search
    nmbrtws = 3
    #Sleep time between to retweets
    sleepTime = 30

    #Search the tweets with the keywords from the query
    for tweet in tweepy.Cursor(api.search_tweets, q = search, result_type = "recent").items(nmbrtws):
        try:
            if not tweet.retweeted:
                print('Retweeted')
                #tweet.retweet()
                # id = tweet.id
                # username = tweet.user.screen_name
                data = {"_id": tweet.id, "user": tweet.user.screen_name}
                DBstorage(data)
                #print(data)
                #time.sleep(sleepTime)
        except:
            print('Error')

main()