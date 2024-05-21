## Python Script to Scrape Posts from Instagram Profile

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
xz -d *json.xz
```


### If you get 401 Error (Too many requests)

You can run the alterante script as follows: 

```
python alternate.py
```

**Note:** You will need to manually change the username and date in the script file

Then, cd into the folder created:

```
cd {username}
```

Then run the following commands:

```
xz -d *json.xz
```