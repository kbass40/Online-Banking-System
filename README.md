# Professional Practice Assignment: Online Banking System
### CIS4930 - Software Testing for Continuous Delivery
#### Contributors: Daniel Tymecki, Kyle Bassignani, Danilo Souza, Timothy Crowley, Danny Moolchand

# Project Overview / Overview of Setup
Our Online Banking System was built using a number of modern technologies. Most of the code was developed using Python3. For our backend databse, we used Firebase Realtime Database and connected to it using Pyrebase, a third party library to help Python interact with Firebase. We also used Firebase to handle our user authentication. And then for the front end we used Flask to handle routing to different webapges. Our system worked by the user interacting with the front end web page and that would make api calls to our microservice which would then interact with the database.

For our deployment program we used Google App Engine and for the continuous integration server we used TravisCI. TravisCI runs all of our unit tests, integration tests, and end-to-end tests in three different stages in the pipeline. At the end of the end-to-end tests, the server deploys our application to Google App Engine. For GAE, we have our main OBS application linked to the microservices service as a subdomain. Using a dispatch file, we are able to route any requests by the main domain to the subdomain. Everything for the Google App Engine and TravicCI is located on the 'prod' branch of our repository. Whenever a new commit is made to this branch, TravisCI runs the tests again and deploys the program if there are no errors.

## Virtual Environment
- To activate the virtual env, navigate to the project directory in you terminal and execute the following command depending on your platform.
    - For macOS/Linux : source env/Scripts/activate
    - For Windows : .\env\Scripts\activate

- To deactivate the virtual env simply type `deactivate` in the terminal instance

- To install the required libraries simply type `pip install requirements.txt`

- To update requirements.txt, simply type `pip freeze > requirements.txt`

## Testing Practices
- To conform tests to a set standard, please adhere to the following guidlines.

    - All tests should be written in the Tests folder in a subforder dictating the functionality tested. Make sure the subfolder is properly linked in `__init__.py`

    - All testing modules should start with "test_" and a descriptive name of the what the module is testing

## Documentation
- Production Web App : https://avid-circle-257318.appspot.com/

- CI Server : https://travis-ci.org/kbass40/Online-Banking-System

- Style Guide : http://google.github.io/styleguide/pyguide.html

- Linter : https://www.pylint.org/

## Rollback
Rollback for our project would be fairly simple. First we would git revert to a working commit and that would trigger TravisCI to run. TravisCI would run all its tests scripts and if all stages pass, then the working build would get automaticaly deployed to Google App Engine.

## How to Run
To run locally : first open the project and open a terminal in the root directory of the project. Next, perform the following commands to get the project up and running:
1. In one terminal, do the command `python Model/WebServer/backend.py` 
2. In a second terminal window, do the command `python Model/Microservice/Microservice.py` 
3. Navigate to `localhost:5000` and the app will be fully functional.

## How to view admin logs
In this project, there exists an account to view all the transaction, OBS, and authentication logs. Also on this dashboard you can view the profit and loss for the bank and each individual stock. To access the administrator account, perform the following steps:
1. Run the project. (Refer to the [How to Run](#how-to-run) section)
2. Click on 'Login'
3. Enter the username `admin@admin.com`
4. Enter the password `admin1`
5. Click 'Submit'
