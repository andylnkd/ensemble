from auth import api
import tweepy


#Create a new txt file to store the tweets id

File = 'id.txt'

def follow():

    lastID = retrieveID(File)

    #Checks mentions 
    
    mentions = api.mentions_timeline(since_id = lastID)
    
    #Loop in the mentions 
    for mention in reversed(mentions):
        print('Looking for mentions')
        #Checks for commands
        if ('#Help' or '#help') in mention.text:
            #Mark as favorite
            #mention.favorite()
            print(mention.text)
            #Store the id of the mention 
            last_ID = mention.id
            storeID(last_ID, File)
            #Reply to the mention 
            api.update_status('@' + mention.user.screen_name + ' Simply reply or QT with an NFT URI and we will provide an estimate and a Yay/ Nay from our experts!', in_reply_to_status_id = mention.id)
            print('tweet answer')

        elif('#Discord' or '#discord') in mention.text:
            print(mention.text)
            #Mark as favorite
            mention.favorite()
            #Store the id
            last_ID = mention.id
            storeID(last_ID, File)
            #Reply to mention
            api.update_status('@' + mention.user.screen_name + ' Join our free Discord server to get rating at any time 24x7! Server here: https://discord.com/channels/933156809944993802/933156809944993804', in_reply_to_status_id = mention.id)
            print('tweet answer')

        elif ('#Price' or '#price') in mention.text:
            print(mention.text)
            #Mark as favorite
            #mention.favorite()
            #Store the id
            last_ID = mention.id
            storeID(last_ID, File)
            #Reply to mention
            api.update_status('@' + mention.user.screen_name + ' Hey there, we would love to provide a free price estimate for NFTs. Feel free to click here or go to getmagic.ai on your mobile browser!', in_reply_to_status_id = mention.id)
            print('tweet answer')

        elif ('#FindMore' or '#findmore') in mention.text:
            print(mention.text)
            #Mark as favorite
            #mention.favorite()
            #Store the id
            last_ID = mention.id
            storeID(last_ID, File)
            #Reply to mention
            api.update_status('@' + mention.user.screen_name + ' You could find more in  https://opensea.io/assets?search[query]=new',  in_reply_to_status_id = mention.id)
            print('tweet answer')
        else:
            print(mention.text)
            #Mark as favorite
            mention.favorite()
            #Store the id
            last_ID = mention.id
            storeID(last_ID, File)
            #Reply to mention
            api.update_status('@' + mention.user.screen_name + ' To get a free rating simply fill out this form, we will send you an update when our experts have their rating ready! https://anup702844.typeform.com/to/DxmDIZ0t',   in_reply_to_status_id = mention.id)
            print('tweet answer')
             
def retrieveID(file):
    id_read = open(file, 'r')
    lastID = id_read.read().strip('\n')
    id_read.close()

    return lastID

def storeID(id, file):
    id_write = open(file, 'w')
    id_write.write(str(id))
    id_write.close()

    return


def main():
    follow()

main()