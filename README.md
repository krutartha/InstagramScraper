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

Then, the scraping will begin. The scrape json will be placed in the current directory im {username}.json file!

Then, cd into the folder created:

```
cd {username}
```

Then run the following commands:

```
rm *.json.xz
```

**Note**: Above command will only work on a linux/unix based terminal (linux/macos). If you're using windows, you can ignore the .json.xz files for now. 

## Using the data to make entries on Admin Dashboard

In each folder created, the {timestamp}.txt contains the caption of the post and {timestamp}.jpg file contains the images! 

**Note**: Some posts might have multiple images, make sure to check all of them!