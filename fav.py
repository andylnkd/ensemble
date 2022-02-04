from auth import api
import time
import os
from pymongo import MongoClient
import tweepy

CLUSTER = os.getenv('CLUSTER')

def main():

    tags = open('tags.txt', 'r')
    fav(tags.read())

def DBstorage(data):
    
    #Access the cluster
    client = MongoClient(CLUSTER)

    #Set the DB
    db = client.nftrater

    #Insert the data in the collection
    db.favoriteTweets.insert_one(data)

def fav(tags):
    search = tags
    nmbrtws = 500
    sleepTime = 172.8
 
    for tweet in tweepy.Cursor(api.search_tweets, q = search, result_type = "recent").items(nmbrtws):
        try:
            if not tweet.favorited:
                print('Marked as fav')
                tweet.favorite()
                #Creates the twitter url
                url = "twitter.com/" + tweet.user.screen_name + "/status/" + str(tweet.id)
                #Puts up the data in a dictionary
                data = {"_id": tweet.id, "user": tweet.user.screen_name, "text": tweet.text, "url": url}
                #Adds it to the DB
                DBstorage(data)
                time.sleep(sleepTime)
        except:
                print('Error')

main()