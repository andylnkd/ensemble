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
    
    cluster = MongoClient('mongodb+srv://admin:<ensemblemongodb>@jan2022testdb.mmli1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = cluster['nftrater']
    collection = db['retweets']

    collection.insert_one(data)

def rt(tags):
    
    #Store the tags in a variable
    search = tags
    #Set a number of tweets to search
    nmbrtws = 1000
    #Sleep time between to retweets
    sleepTime = 90

    #Search the tweets with the keywords from the query
    for tweet in tweepy.Cursor(api.search_tweets, q = search, result_type = "recent").items(nmbrtws):
        try:
            if not tweet.retweeted:
                print('Retweeted')
                tweet.retweet()
                time.sleep(sleepTime)
                data = {'_id': tweet.id, 'user': tweet.screen_user, }
                DBstorage(data)
        except:
            print('Error')

main()