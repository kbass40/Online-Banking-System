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

## Documentation
- CI Server : 

- Style Guide : http://google.github.io/styleguide/pyguide.html

- Linter : https://www.pylint.org/

## Running Instruciton
- First make sure docker-compose is installed https://docs.docker.com/compose/install/

- For the authentication front end navigate to /Model/WebServer and first run docker-compose up then run python3 backend.py

- Navigate to localhost:5000

- For the api navigate to Model/<Stock Targeted> and first run docker-compose up then run python3 <Stock Targeted>.py
    
- Follow the api documentation in the MicroservicesApi.yaml file
