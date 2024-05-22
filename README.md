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

## Using the data to make entries on Admin Dashboard

In each {username} directory created, the {timestamp}.txt contains the caption of the post and {timestamp}.jpg file contains the images! 

**Note**: Some posts might have multiple images, make sure to check all of them!

### Common Errors

1. **HTTP error code 401**: Please check the username you entered and make sure it's a valid username
2. More common errors and fixes will be updated soon...
