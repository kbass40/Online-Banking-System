# Online Banking System

## Virtual Environment
- To activate the virtual env, navigate to the project directory in you terminal and execute the following command depending on your platform.
    - For macOS/Linux : source env/bin/activate
    - For Windows : .\env\Scripts\activate

- To deactivate the virtual env simply type 'deactivate' in the terminal instance

- To install the required libraries simply type 'pip install requirements.txt'

- To update requirements.txt, simply type 'pip freeze > requirements.txt'

## Testing Practices
- To conform tests to a set standard, please adhere to the following guidlines.

    - All tests should be written in the Tests folder in a subforder dictating the functionality tested. Make sure the subfolder is properly linked in '__init__.py'

    - All testing modules should start with "test_" and a descriptive name of the what the module is testing