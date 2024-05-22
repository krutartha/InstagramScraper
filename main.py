#import
from subprocess import run
import shlex
username = input("Enter HY Chapter's Instagram username: ") #get username from commandline
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
print("###########commencing scrape###########") #print message
command = f'instaloader --post-filter="date_utc >= datetime({start_year}, {start_month}, 1)" {username}'
command = shlex.split(command)
run(command)
print("###########scraping done###############") #print message

