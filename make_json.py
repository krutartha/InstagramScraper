import glob, os #for iterating files in folder
from groq import Groq #generative AI model
from dotenv import load_dotenv #to load API key from .env file
import json #to dump results to json
import unicodedata #to convert unicode strings
load_dotenv() #load the .env file
client = Groq(api_key=os.getenv("KEY")) #create new Grop client and pass in the api key
username = input("Enter HY Chapter's Instagram username: ") #get username from commandline
os.chdir(username) #change directory to chapter dir
events = [] #create events array to hold all the events
for txt_file in glob.glob("*.txt"): #iterate over each .txt files
    txt_file_contents = open(txt_file, "r").read() #open txt file to get caption data
    txt_file_contents = str(unicodedata.normalize("NFKD", txt_file_contents).encode('ascii', 'ignore')) #convert from unicode to deal with characters
    groq_resp = client.chat.completions.create(  #use groq client to generate response
    messages=[
        {
            "role": "user",
            "content": f'Generate a simple 200 word post event description for an event that had the following description on the poster: {txt_file_contents}',
        }
    ],
    model="llama3-8b-8192",
)
    groq_event_description = groq_resp.choices[0].message.content #get the first response's message
    img_regex = txt_file[:-4]+"*.jpg" #regex pattern for getting the associated image files for the post
    img_array = [] #array to hold names of all image files
    for img_file in glob.glob(img_regex): #itearte over each image file associated with post
        img_array.append(img_file) #append image file name to img array
    event = { #create new dict to hold event details
        "event_date": txt_file[:-8], #timestamp
        "instagram_caption": txt_file_contents, #insta caption
        "chatgpt_event_desc": groq_event_description, #chatgpt response
        "img_array": img_array #array containing associated image files
    }
    events.append(event) #add event to events array
fd = open(f'{username}.json', "w") #open new json file for the chapter
json.dump(events, fd) #dump events array to json
