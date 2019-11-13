# Online Banking System

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

## Working with the Logging Database
- To run the logging database, type `docker-compose up` which will set up a docker container specified in the yml file

- To properly close the logging database, type `docker-compose down`

## Running Instruciton
- First make sure docker-compose is installed https://docs.docker.com/compose/install/

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< refs/remotes/origin/authentication
>>>>>>> Update README.md
- For the authentication front end navigate to /Model/WebServer and first run docker-compose up then run python3 backend.py

- Navigate to localhost:5000

- For the api navigate to Model/<Stock Targeted> and first run docker-compose up then run python3 <Stock Targeted>.py
=======
- For the authentication front end navigate to /Model/WebServer and first run 'docker-compose up' then run 'python3 backend.py'

- Navigate to localhost:5000

- For the api navigate to Model/<Stock Targeted> and first run 'docker-compose up' then run 'python3 <Stock Targeted>.py'
>>>>>>> Update README.md
<<<<<<< HEAD
=======
- For the authentication front end navigate to /Model/WebServer and run 'python3 backend.py'

- Navigate to localhost:5000

- For the api navigate to Model/<Stock Targeted> and run 'python3 <Stock Targeted>.py'
>>>>>>> Update README.md
=======
>>>>>>> Update README.md
    
- Follow the api documentation in the MicroservicesApi.yaml file
