import os
import re

import pyrebase
from dotenv import load_dotenv

load_dotenv()

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

    # Function to return user api key info based on their email and password
    def authenticate_user_via_email_password(self, email, password):
        if not isinstance(email, str):
            raise TypeError('ERROR email must be of type str')

        if not isinstance(password, str):
            raise TypeError('ERROR password must be of type str')

        if not (isEmailValid(email)):
            raise SyntaxError('ERROR a valid email must be provided')

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

        auth_id = self._auth.create_user_with_email_and_password(email,password)['idToken']
        user_id = self._get_userID_from_authID(auth_id)
        blank_account = {stock_symbols[0]:0, stock_symbols[1]:0,stock_symbols[2]:0, stock_symbols[3]:0,stock_symbols[4]:0}
        self._db.child('users').child(user_id).set(blank_account, auth_id)
        return auth_id

    # Interface to update a user's stock info based on microservice purchuse
    def update_user_info(self,auth_id,symbol,amount):
        if not isinstance(symbol, str):
            raise TypeError('ERROR symbol must be of type str')

        if symbol not in stock_symbols:
            raise ValueError('ERROR symbol must be within the approved stock microservices')

        if not isinstance(amount,int):
            raise TypeError('ERROR amount must be of type int')

        user_info = self.get_user_info(auth_id)
        user_id = self._get_userID_from_authID(auth_id)
        old_amt = self._db.child('users').child(user_id).child(symbol).get(auth_id).val()
        self._db.child('users').child(user_id).update({symbol:old_amt+amount},auth_id)
    
    '''
    #Pyrebase won't support removing authenticated users so R I P delete
    def delete_user(self,auth_id):
        headers = {
            'Content-Type': 'application/json',
        }

        params = (('key', config['apiKey']),)   

        data = '{"idToken":'+auth_id+'}'

        response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:delete', headers=headers, params=params, data=data)

        user_id = self._get_userID_from_authID(auth_id)
        self._db.child('users').child(user_id).remove()
    '''

# myDb = AuthDatabase()
# myDb.create_new_user('kyle@email.com','password')
# user_id = myDb.authenticate_user_via_email_password('kyle@email.com','password')
# print(myDb.get_user_info(user_id))