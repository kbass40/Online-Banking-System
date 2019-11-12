import pyrebase
from dotenv import load_dotenv
import os
import re 

load_dotenv()

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# Configuration variables to connect with authentication database
config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": "obs-software-testing.firebaseapp.com",
    "databaseURL": "https://obs-software-testing.firebaseio.com",
    "projectId": "obs-software-testing",
    "storageBucket": "obs-software-testing.appspot.com",
    "messagingSenderId": "591353727823",
    "appId": "1:591353727823:web:8223673fb928e11b3c533a",
    "measurementId": "G-C57RM1FSR5"
}

def isEmailValid(email):
    if not isinstance(email, str):
            raise ValueError('ERROR email must be of type str')
    else:
        return re.search(regex, email)

class AuthDatabase():
    def __init__(self):
        self._firebase = pyrebase.initialize_app(config)
        self._auth = self._firebase.auth()
        self._db = self._firebase.database()

    # Function to return user api key info based on their email and password
    def authenticate_user_via_email_password(self, email, password):
        if not isinstance(email, str):
            raise ValueError('ERROR email must be of type str')

        if not isinstance(password, str):
            raise ValueError('ERROR password must be of type str')

        return self._auth.sign_in_with_email_and_password(email,password)['idToken']

    def _get_userID_from_authID(self, authID):
        return self._auth.get_account_info(authID)["users"][0]['localId']

    # Returns the json stock info of user given a valid session token
    def get_user_info(self, id_token):
        userId = self._get_userID_from_authID(id_token)
        return self._db.child('users').child(userId).get(id_token).val()

    # Creates new user in database based on their email, password, and username
    def create_new_user(self, email, username, password):
        if not isinstance(email, str):
            raise ValueError('ERROR email must be of type str')

        if not isinstance(password, str):
            raise ValueError('ERROR password must be of type str')

        if not isinstance(username, str):
            raise ValueError('ERROR username must be of type str')

        if not (isEmailValid(email)):
            raise SyntaxError('ERROR a valid email must be provided')

        auth_id = self._auth.create_user_with_email_and_password(email,password)['idToken']
        user_id = self._get_userID_from_authID(auth_id)
        blank_account = {'apple_stock':0, 'facebook_stock':0,'google_stock':0, 'ubisoft_stock':0,'oracle_stock':0}
        self._db.child('users').child(user_id).set(blank_account, auth_id)

# myDb = AuthDatabase()
# user_id = myDb.authenticate_user_via_email_password('daniel.tymecki@gmail.com','password')
# print(myDb.get_user_info(user_id))
# myDb.create_new_user('test@email.com','test_boi','password123')
