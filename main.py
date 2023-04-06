from instagrapi import Client
from instagrapi.exceptions import ClientLoginRequired
import os
import schedule
import time
import glob
def post(account,passw):

# Login to Instagram
    client = Client()
    client.login(username=account, password=passw)


    # Upload Reels from local stored videos
    try:
        lines = []
        with open('tags.txt', 'r') as file:
            for line in file:
                lines.append(line.strip())
        i=0
        path="videos"
        n=len(os.listdir(path))
        while(i<n):
            client.video_upload(path+"/sv"+str(i)+".mp4",caption=lines[i])
            i=i+1

    except ClientLoginRequired:
        print("Client login required")
    files = glob.glob('videos/*.jpg')

# Iterate over the list of files and remove individually
    for file in files:
        print("Deleting image: ",file)
        os.remove(file)


####################################################################################
############# add acounts and password in the function and video is schedulet at time yiu can change it ####

def post_itsmeshreya():
    post("itsmeshreya_officials","passw2")

def post_priyanka_j():
    post("priyanka_j_officials","passsw04")

schedule.every().day.at("00:54").do(post_itsmeshreya)
schedule.every().day.at("00:56").do(post_priyanka_j)       
# schedule.every().day.at("00:50").do(post("itsmeshreya_officials","Insta@js02"))
# schedule.every().day.at("00:52").do(post("priyanka_j_officials","Insta@js04"))

while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

