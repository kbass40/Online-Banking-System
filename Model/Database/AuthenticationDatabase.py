import os
import re
import sys
from pathlib import Path

import pyrebase
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import auth, credentials

load_dotenv()

path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')

regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
stock_symbols = ['AAPL','FB','GOOGL','ORCL','UBSFY']

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
            raise TypeError('ERROR email must be of type str')
    else:
        return re.search(regex, email)

class AuthDatabase():
    def __init__(self):
        self._firebase = pyrebase.initialize_app(config)
        self._auth = self._firebase.auth()
        self._db = self._firebase.database()

        cred = credentials.Certificate(str(Path(__file__).parent)+"\\obs-software-testing-firebase-adminsdk-1m0eh-b9c8ed7a81.json")
        firebase_admin.initialize_app(cred)

    # Function to return user api key info based on their email and password
    def authenticate_user_via_email_password(self, email, password):
        if not isinstance(email, str):
            raise TypeError('ERROR email must be of type str')

        if not isinstance(password, str):
            raise TypeError('ERROR password must be of type str')

        if not (isEmailValid(email)):
            raise SyntaxError('ERROR a valid email must be provided')

        #need to check if email is valid

        return self._auth.sign_in_with_email_and_password(email,password)['idToken']

    def _get_userID_from_authID(self, authID):
        return self._auth.get_account_info(authID)["users"][0]['localId']

    # Returns the json stock info of user given a valid session token
    def get_user_info(self, id_token):
        userId = self._get_userID_from_authID(id_token)
        return self._db.child('users').child(userId).get(id_token).val()

    # Creates new user in database based on their email and password
    def create_new_user(self, email, password):
        if not isinstance(email, str):
            raise TypeError('ERROR email must be of type str')

        if not isinstance(password, str):
            raise TypeError('ERROR password must be of type str')

        if not (isEmailValid(email)):
            raise SyntaxError('ERROR a valid email must be provided')

        if len(password) < 8:
            raise ValueError('ERROR passwords must be at least 8 characters in length')

        auth_id = self._auth.create_user_with_email_and_password(email,password)['idToken']
        user_id = self._get_userID_from_authID(auth_id)
        blank_account = {stock_symbols[0]:0, stock_symbols[1]:0,stock_symbols[2]:0, stock_symbols[3]:0,stock_symbols[4]:0}
        self._db.child('users').child(user_id).set(blank_account, auth_id)
        return auth_id


    def update_user_info(self, auth_id, symbol, amount):
        if symbol not in stock_symbols:
            raise ValueError('ERROR symbol must be within the approved stock microservices')

        if not isinstance(amount,int):
            raise TypeError('ERROR amount must be of type int')

        user_info = self.get_user_info(auth_id)
        user_id = self._get_userID_from_authID(auth_id)
        old_amt = self._db.child('users').child(user_id).child(symbol).get(auth_id).val()
        self._db.child('users').child(user_id).update({symbol:old_amt+amount},auth_id)

    def delete_autheticated_user_from_auth_id(self,auth_id):
        user_id = self._get_userID_from_authID(auth_id)
        auth.delete_user(user_id)

    def delete_autheticated_user_from_uid(self,user_id):
        auth.delete_user(user_id)

    def delete_all_users(self):
        for user in auth.list_users().iterate_all():
            print('Deleted User: ' + user.uid)
            # Uncomment to actually delete 
            #self.delete_autheticated_user_from_uid(user.uid)


myDb = AuthDatabase()
myDb.create_new_user('kyle84684.5@email.com','password123')
auth_id = myDb.authenticate_user_via_email_password('kyle84684.5@email.com','password123')
print(myDb.get_user_info(auth_id))
myDb.delete_autheticated_user_from_auth_id(auth_id)
myDb.delete_all_users()
