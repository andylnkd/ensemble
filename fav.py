from auth import api
import time
import tweepy

def main():

    tags = open('tags.txt', 'r')
    fav(tags.read())


def fav(tags):
    search = tags
    nmbrtws = 1000
    sleepTime = 20
 
    for tweet in tweepy.Cursor(api.search_tweets, q = search, result_type = "recent").items(nmbrtws):
        try:
            if not tweet.favorited:
                print('Marked as fav')
                tweet.favorite()
                time.sleep(sleepTime)
        except:
                print('Error')

main()