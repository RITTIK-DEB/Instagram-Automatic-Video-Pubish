from instagrapi import Client
from instagrapi.exceptions import ClientLoginRequired
import os

# Login to Instagram
client = Client()
client.login(username="username", password="password")


# Upload Reels from local stored videos
try:
    lines = []
    with open('tags.txt', 'r') as file:
        for line in file:
            lines.append(line.strip())
    i=0
    path="videos"
    n=len(os.listdir(path))
    while(i<=n):
        client.video_upload(path+"/sv"+str(i)+".mp4",caption="#"+lines[i])
        i=i+1

except ClientLoginRequired:
    print("Client login required")
