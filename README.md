## Python Script to Scrape Posts from Instagram Profile

### Prerequisites

1. Download Python: https://wiki.python.org/moin/BeginnersGuide/Download
2. Make sure python is executable from your cmd/terminal by running:
```
python --version
```
3. Make sure pip is installed:
```
pip --version
```

4. Optional, but recommended: Installa Anaconda and set up an environment: https://conda.io/projects/conda/en/latest/user-guide/getting-started.html

### Setup Instructions

```
    pip install -r requirements.txt
```

If you want the Generative AI based Event Description feature, you will need a Groq Cloud API key. Follow these steps:

1. Visit: https://console.groq.com/keys
2. Login using email, github, or your google account
3. Click on Create API Key
4. Enter any desired name
5. Copy the API key displayed
6. In the directory of this project, create a new file with name ".env"
7. Add the following line inside the newly created .env file:

```
KEY={paste API key from clipboard}
```


### Running Instructions

```
    python main.py
```

Then, the command line prompt will ask you to enter the username of the instagram profile: 

```
    Enter HY Chapter's Instagram username:
```

Here, put in the instagram handle (username) of the account. Make sure to remove any leading or trailing spaces. 

Then, the prompt will ask you to enter the start year: 

```
    Enter start year in YYYY format:
```

Enter the beginning year from when you want the posts from in YYYY format

Then, the prompt will ask you to enter the start month: 

```
    Enter start month in MM format:
```

Enter the beginning month from when you want the posts from in MM format.

Then, the scraping will begin. The scrape files will be placed in a directory with the name {username}

## Generating JSON files with GenAI based Event Descriptions

Run the following script:

```
    python make_json.py
```

This will create the respective json file in the chapter directory with a 200 word event description (obtained by Groq Cloud, a service similar to ChatGPT) based on the instagram post's caption

## Using the data to make entries on Admin Dashboard

In each {username} directory created, the {timestamp}.txt contains the caption of the post and {timestamp}.jpg file contains the images! 

**Note**: Some posts might have multiple images, make sure to check all of them!

**Alternatively**, if you used the GenAI based description feature, you could just go to the {username} directory and use the {username}.json file to access each event and description. The img_array attribute will contain the names of each image associated witht he particular event. 

### Common Errors

1. **HTTP error code 401**: Please check the username you entered and make sure it's a valid username
2. **Redirected to login page. Use --login**: You have exceeded the maximum number of scraping requests. Please allow some time before you run the script again.
3. More common errors and fixes will be updated soon...
