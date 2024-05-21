#imports
from instaloader import * 
import datetime
import json
import glob, os
# create instance
L = instaloader.Instaloader() #creating a new instaloader instance
username = input("Enter HY Chapter's Instagram username: ") #get username from commandline
profile = Profile.from_username(L.context, username) #create a Profile object from given username
start_year = input("Enter start year in YYYY format: ") #get the year from which you want to scrape posts from
got_valid_start_month = False #boolean to keep track of whether a valid start month has been received
while(not got_valid_start_month):
    start_month = input("Enter start month in MM format: ") #get the month from which you want to scrape the posts from
    if(start_month != "00" and start_month != "0"):
        start_month = start_month.lstrip('0') #strip any leading zeros in case of a single digit month. EG: 09 becomes 9
        got_valid_start_month = True
    elif(int(start_month) <= 0 or int(start_month) > 12):
        print("Invalid start month! Please try again")
        pass
out_array = [] #creating an array to hold every post from the instagram user
print("###########commencing scrape###########") #print message
for post in profile.get_posts():
    if post.date > datetime.datetime(int(start_year), int(start_month), 1, 0, 0): #filter posts by post date
        post_info = {
        "title": post.title, #post title, usually None
        "is_video": post.is_video, #check if the post is a video or a reel
        "date": str(post.date), #covert datetime object to a string representation of date
        "caption": str(post.caption), #get the post caption
        "thumbnail_url": post.url #get the url of the image or video
        }   
        out_array.append(post_info) #add current post to the posts array
        try:
            L.download_post(post, username) #download post including pictures and metadata
        except:
            print("Error occured on post with date: " + post_info.get('date') + " and caption: " + post_info.get("caption") + ", but will continue with other posts!")
            continue
out_file = open(username+"/"+username+".json", "w") #open new file to dump array to
json.dump(out_array, out_file) #convert array to json array
out_file.close() #close fd
print("#######################################") #print message
print("removing unecessary files...")
for f in glob.glob(username+"/*.json.xz"):
    os.remove(f)
for f in glob.glob(username+"/*.txt"):
    os.remove(f)
print("removed unecessary files!")
print("#######################################") #print message
print("#######################################") #print message
print("scraping done! file saved in " + username + ".json")#print message
print("#######################################") #print message