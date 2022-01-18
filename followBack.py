from auth import api
import tweepy

def main():
    follow()

def follow():
    #Get account followers
    for follower in tweepy.Cursor(api.get_followers).items(1):
        follower.follow()
        print('New follow ' + follower.screen_name)
        
main()