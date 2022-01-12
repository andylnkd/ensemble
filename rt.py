from auth import api
import time
import tweepy

def main():

    #Read the tags from a txt file
    tags = open('tags.txt', 'r')
    rt(tags.read())

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
        except:
            print('Error')

main()