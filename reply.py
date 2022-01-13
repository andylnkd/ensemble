from auth import api
import tweepy


#Create a new txt file to store the tweets id

File = 'id.txt'

def follow():

    lastID = retrieveID(File)

    #Checks mentions 
    if lastID == None:
        mentions = api.mentions_timeline(tweet_mode = 'extended')
    else:
        #Use the last tweet responded id to avoid double responses
        mentions = api.mentions_timeline(lastID, tweet_mode = 'extended')
    
    #Loop in the mentions 
    for mention in reversed(mentions):
        #Checks for commands 
        if ('#Help' or '#help') in mention.txt:
            mention.favorite()
            lastID = mention.id
            storeID(lastID, File)
            api.update_status('@' + mention.user.screen_name + 'Simply reply or QT with an NFT URI and we will provide an estimate and a Yay/ Nay from our experts!')

        elif ('#Discord' or '#discord') in mention.txt:
            mention.favorite()
            lastID = mention.id
            storeID(lastID, File)
            api.update_status('@' + mention.user.screen_name + 'Join our free Discord server to get rating at any time 24x7! Server here:')
        
        elif ('#Price' or '#price') in mention.txt:
            mention.favorite()
            lastID = mention.id
            storeID(lastID, File)
            api.update_status('@' + mention.user.screen_name + 'Hey there, we would love to provide a free price estimate for NFTs. Feel free to click here or go to getmagic.ai on your mobile browser!')
        
        elif ('#FindMore' or '#findmore') in mention.txt:
            mention.favorite()
            lastID = mention.id
            api.update_status('@' + mention.usser.screen_name + 'You could find more in  https://opensea.io/assets?search[query]=new')

             
def retrieveID(file):
    id_read = open(file, 'r')
    lastID = int(id_read.read().strip())
    id_read.close()

    return lastID

def storeID(id, file):
    id_write = open(file, 'w')
    id_write.write(str(id))
    id_write.close()

    return


def main():
    follow()
    

