## NOTICE FOR STUDENTS
Please do not share personal information of any kind on the database! In order to make it easier for you to use,
I have removed basically all safety parameters. I also obliterate all the data on the first of each month, so 
don't post anything you want to keep.

# How to use this API

### Steps to make it run
Open up a terminal. Navigate to a folder where you want to stash the app, then clone this repo.

If you're familiar with Docker, the Dockerfile includes commands to get the app to run, 
and can be executed with docker commands. Otherwise:

### In your terminal, type:
1. python3 -m venv venv 
This is like Python's version of setting up NPM.
2. If you're on Mac:
Type: source venv/bin/activate
3. If you're on Windows:
Type: venv\Scripts\activate
4. pip3 install -r requirements.txt
This is using NPM to install every dependency in the requirements.txt folder. There's some extra stuff in there
so it's fairly large, be sure to be on steady wifi to install it.
5. Type: flask run
This should work, but if it tells you it doesn't know where the Flask app is (it will complain about FLASK_APP= or similar),
then type 
- FLASK_APP=app
- FLASK_ENV=development
You'll also need to connect to the database here, which will be in Google Classroom.

## Using the database
Inside of /app/api/routes.py you will see a variety of functions in Python to connect to.

- getdata: 
This is just a tester function. After you start the app, go to http://127.0.0.1:5000/api/getdata and 
you should see "{'yee': 'haw'}".
- /:
This is also a tester: After you start, go to http://127.0.0.1:5000/api/ and it should congratulate you.
- contacts:
Navigating to http://127.0.0.1:5000/api/contacts will display the current data in the database.
There are two kinds of /contacts endpoints: one is a get, and one is a post.
- contacts/id
If you copy-paste one of the id values from the contacts endpoint and put the id after http://127.0.0.1:5000/api/contacts, 
you will see only that specific piece of data.
Depending on which contacts/id methods you use, you have options to get a single piece of data, update it, or delete it.
- clean
This is my function to empty the database and repopulate it.

### Since I clean out and update the database regularly, feel free to modify and delete data as you like.
## Please don't leave the database empty, so other students aren't confused by empty returns. Thanks!