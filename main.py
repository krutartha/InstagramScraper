#import
from subprocess import run #this import is for running the instaloader command 
import shlex #this import is for splitting command into an array of integers
import glob, os #these imports are for removing uncessary files
from PIL import Image #this import is for the image compression
username = input("Enter HY Chapter's Instagram username: ") #get username from commandline
start_year = input("Enter start year in YYYY format: ") #get the year from which you want to scrape posts from
got_valid_start_month = False #boolean to keep track of whether a valid start month has been received
while(not got_valid_start_month):
    start_month = input("Enter start month in MM format: ") #get the month from which you want to scrape the posts from
    if(start_month != "00" and start_month != "0"):
        start_month = start_month.lstrip('0') #strip any leading zeros in case of a single digit month. EG: 09 becomes 9
        got_valid_start_month = True #update boolean value
    elif(int(start_month) <= 0 or int(start_month) > 12): #in case the input month value is not valid
        print("Invalid start month! Please try again") #print error message and prompt for input again
        pass #pass this iteration of the while loop
print("###############################################################") #print message
print("starting scrape....")
command = f'instaloader --post-filter="date_utc >= datetime({start_year}, {start_month}, 1)" {username}' #using f-strings for string interpolation
command = shlex.split(command) #split string to an array of parameters
run(command) #run the split command using subprocess.run method
print("scraping done!")
print("###############################################################") #print message
print("removing uncessary files....")
os.chdir(username)
for file in glob.glob("*.json.xz"): #regex pattern matching for all json.xz files
    os.remove(file) #remove each .json.xz file
for profile_pic in glob.glob("*_profile_pic.jpg"): #regex pattern matching to get the profile_pic.jpg file
    os.remove(profile_pic) #remove the profile pic jpg file
for id_file in glob.glob("*id*"): #regex pattern matching for the instagram account id number file
    os.remove(id_file) #remove the id file
print("done removing")
print("###############################################################") #print message
print("starting image compression...")
initial_size = 0 #variable to hold initial size of all images combined
compressed_size = 0 #variable to hold post compression size of all images combined
for i in glob.glob("*.jpg"): #get all files with extension .jpg in the folder
    initial_size += os.path.getsize(i) #get the current image's size and update the size var
    image = Image.open(i) #open the file using PIL submodule called Image, using the supported open method
    width, height = image.size #get opened image's width and height
    # new_size = (width, height) #reduce image width and height by half
    # resized_image = image.resize(new_size) #resize opened image with new size
    os.remove(i) #remove current image
    image.save(i, optimize=True, quality=70) #save the image with 30% quality reduction
    # resized_image.save(i, optimize=True, quality=70) #save the resized image with 30% quality reduction
    compressed_size += os.path.getsize(i) #get the compressed image's size and update var
print("pre-compression images were: ", str(initial_size/1000000) + " MB") #print message
print("post-compression images are: ", str(compressed_size/1000000) + " MB") #print message
print("finished image compression!") #print message 
print("###############################################################") #print message

