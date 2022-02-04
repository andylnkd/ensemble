import imp
from auth import api
import tweepy
import os
import time
import pymongo
from pymongo import MongoClient

CLUSTER = os.getenv('CLUESTER')

def main():

    #Read the tags from a txt file
    tags = open('tags.txt', 'r')
    rt(tags.read())

def DBstorage(data):
    
    #Access the cluster
    client = MongoClient(CLUSTER)

    #Set the DB
    db = client.nftrater

    #Insert the data in the collection
    db.retweets.insert_one(data)

def rt(tags):
    
    #Store the tags in a variable
    search = tags
    #Set a number of tweets to search
    nmbrtws = 200
    #Sleep time between to retweets
    sleepTime = 432

    #Search the tweets with the keywords from the query
    for tweet in tweepy.Cursor(api.search_tweets, q = search, result_type = "recent").items(nmbrtws):
        try:
            if not tweet.retweeted:
                print('Retweeted')
                tweet.retweet()
                #Creates the twitter url
                url = "twitter.com/" + tweet.user.screen_name + "/status/" + str(tweet.id)
                #Puts up the data in a dictionary
                data = {"_id": tweet.id, "user": tweet.user.screen_name, "text": tweet.text, "url": url}
                #Send the data to the DB
                DBstorage(data)
                time.sleep(sleepTime)
        except:
            print('Error')

main()