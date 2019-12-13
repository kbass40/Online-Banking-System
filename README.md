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
- Production Web App : https://avid-circle-257318.appspot.com/

- CI Server : https://travis-ci.org/kbass40/Online-Banking-System

- Style Guide : http://google.github.io/styleguide/pyguide.html

- Linter : https://www.pylint.org/

## Rollback
Rollback for our project would be fairly simple. First we would git revert to a working commit and that would trigger TravisCI to run. TravisCI would run all its tests scripts and if all stages pass, then the working build would get automaticaly deployed to Google App Engine.
