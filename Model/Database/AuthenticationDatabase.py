from Model.Misc import Time as TIME
import os
import re
import sys
from pathlib import Path

import pyrebase
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import auth, credentials
from requests import HTTPError

load_dotenv()

path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')
sys.path.append(str(path) + '//..//..')


regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
stock_symbols = ['AAPL', 'FB', 'GOOGL', 'ORCL', 'UBSFY']
log_types = ['TRANSACTION', 'MISC', 'INFO']

# Configuration variables to connect with authentication database
config = {
    # "apiKey": "AIzaSyCBNsjeqTwLByOJdGKqaY5VyWvcjJe8UTY",
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

        if (not len(firebase_admin._apps)):
            cred = credentials.Certificate(
                str(Path(__file__).parent)+"/firebase-admin-sdk.json")
            firebase_admin.initialize_app(cred)

    # Function to return user api key info based on their email and password
    def authenticate_user_via_email_password(self, email, password):
        if not isinstance(email, str):
            raise TypeError('ERROR email must be of type str')

        if not isinstance(password, str):
            raise TypeError('ERROR password must be of type str')

        if not (isEmailValid(email)):
            raise SyntaxError('ERROR a valid email must be provided')

        return self._auth.sign_in_with_email_and_password(email, password)['idToken']

    def _get_userID_from_authID(self, auth_id):
        return self._auth.get_account_info(auth_id)["users"][0]['localId']

    def get_user_accounts(self, auth_id):
        userId = self._get_userID_from_authID(auth_id)
        return self._db.child('users').child(userId).shallow().get(auth_id).val()

    # Returns the json stock info of user given a valid session token
    def get_user_info(self, auth_id):
        userId = self._get_userID_from_authID(auth_id)
        return self._db.child('users').child(userId).get(auth_id).val()

    # Returns the user's balance for a particular account
    def get_account_balance(self, auth_id, account_name):
        user_id = self._get_userID_from_authID(auth_id)
        return self._db.child('users').child(user_id).child(account_name).child('balance').get(auth_id).val()

    # Returns all the info for a user account
    def get_account_info(self, auth_id, account_name):
        user_id = self._get_userID_from_authID(auth_id)
        return self._db.child('users').child(user_id).child(account_name).get(auth_id).val()

    # Function to retrieve bank info for a particular stock
    def get_bank_info(self, symbol):
        if symbol not in stock_symbols:
            raise ValueError(
                'ERROR symbol must be within the approved stock microservices')

        return self._db.child('admin').child('bank').child(symbol).get().val()

    # Creates new user in database based on their email and password
    def create_new_user(self, email, password):
        if not isinstance(email, str):
            raise TypeError('ERROR email must be of type str')

        if not isinstance(password, str):
            raise TypeError('ERROR password must be of type str')

        if not (isEmailValid(email)):
            raise SyntaxError('ERROR a valid email must be provided')

        if len(password) < 8:
            raise ValueError(
                'ERROR passwords must be at least 8 characters in length')

        auth_id = self._auth.create_user_with_email_and_password(email, password)[
            'idToken']
        user_id = self._get_userID_from_authID(auth_id)
        self._db.child('users').set(user_id)
        return auth_id

    '''
    def create_admin(self):
        act_data = {}
        for s in stock_symbols:
            act_data[s] = {
                "gain-loss" : 0,
                "stock_num" : 0
            }
        act_data["balance"] = 0

        self._db.child('admin').child('bank').set(act_data)
        self._db.child('admin').child('logs').push('This is an example log')
    '''

    # Create a new banking account for a user
    def create_new_account_for_user(self, auth_id, account_name):
        user_id = self._get_userID_from_authID(auth_id)

        # Generate json data to add to new account
        act_data = {}
        for s in stock_symbols:
            act_data[s] = {
                "gain-loss": 0,
                "stock_num": 0
            }
        act_data["balance"] = 0

        accounts = self._db.child('users').child(
            user_id).shallow().get(auth_id).val()
        # If a user has an account
        if (not isinstance(accounts, type(None))):
            # if an account(s) exists, check how many. If < 3 then fine
            if (len(accounts) < 3):
                self._db.child('users').child(user_id).child(
                    account_name).set(act_data)
            # Otherwise throw exception
            else:
                raise RuntimeError(
                    "ERROR an account may not have more than 3 sub accounts!")
        # Otherwise add one
        else:
            self._db.child('users').child(user_id).child(
                account_name).set(act_data)

    # Update bank info for a particular stock
    def update_bank_info(self, symbol, stock_amt, gainloss):
        if symbol not in stock_symbols:
            raise ValueError(
                'ERROR symbol must be within the approved stock microservices')

        return self._db.child('admin').child('bank').child(symbol).update({'gain-loss': gainloss, 'stock_num': stock_amt})

    # Checks if an account name is valid for a user
    def is_valid_account_for_user(self, auth_id, account_name):
        accounts = self.get_user_accounts(auth_id)
        return account_name in accounts

    # Updates the user's stock info be specified amount / gainloss
    def update_user_info(self, auth_id, account_name, symbol, amount, gainloss):
        if symbol not in stock_symbols:
            raise ValueError(
                'ERROR symbol must be within the approved stock microservices')

        if not isinstance(amount, int):
            raise TypeError('ERROR amount must be of type int')

        if not isinstance(gainloss, float):
            raise TypeError('ERROR amount must be of type float')

        user_id = self._get_userID_from_authID(auth_id)
        old_amt = self._db.child('users').child(user_id).child(
            account_name).child(symbol).get(auth_id).val()

        if old_amt is None:
            raise ValueError('ERROR account name must be valid for this user')

        self._db.child('users').child(user_id).child(account_name).child(
            symbol).update({'stock_num': amount}, auth_id)
        self._db.child('users').child(user_id).child(account_name).child(
            symbol).update({'gain-loss': gainloss}, auth_id)

    # Updates the user's balance by specified delta amount
    def update_user_balance(self, auth_id, account_name, delta):
        if not isinstance(delta, float):
            raise TypeError('ERROR delta value must be of type float')

        user_id = self._get_userID_from_authID(auth_id)
        old_balance = self._db.child('users').child(user_id).child(
            account_name).child('balance').get(auth_id).val()

        if old_balance is None:
            raise ValueError('ERROR account name must be valid for this user')

        self._db.child('users').child(user_id).child(
            account_name).update({'balance': old_balance+delta}, auth_id)

    # Adds logs to database
    def push_log(self, time, log_type='MISC', log_message='null'):
        if not TIME.is_time_formatted(time):
            raise TypeError(
                'ERROR time variable must be formatted in the proper format %Y-%m-%d %H:%M:%S')

        if log_type not in log_types:
            raise ValueError(
                'ERROR log_type must be within the approved log types')

        if not isinstance(log_message, str):
            raise TypeError('ERROR log message must be of type str')

        log = {'time': time, 'type': log_type, 'content': log_message}

        self._db.child('admin').child('logs').push(log)

    # Retrieves all logs as an ordered dict if user is admin
    def get_all_logs(self, admin_id):
        try:
            logs = self._db.child('admin').child('logs').get(admin_id).val()
            return logs
        except HTTPError:
            raise ValueError(
                'ERROR must be authenticated admin to get content')

    def delete_autheticated_user_from_auth_id(self, auth_id):
        user_id = self._get_userID_from_authID(auth_id)
        self.delete_autheticated_user_from_uid(user_id)

    def delete_autheticated_user_from_uid(self, user_id):
        self._db.child('users').child(user_id).remove()
        auth.delete_user(user_id)

    def delete_all_users(self, confirm=False):
        for user in auth.list_users().iterate_all():
            print('Deleted User: ' + user.uid)
            # Uncomment to actually delete
            '''
            if confirm:
                # self.delete_autheticated_user_from_uid(user.uid)
            #'''

    def delete_all_data(self, confirm=False):
        # Uncomment to actually delete
        '''
        if confirm:
            self._db.child('users').remove()
            self._db.set('users')
        #'''


#''' The following is a complete test that creates an account
myDb = AuthDatabase()
#myDb.create_new_user('kyle84684.5@email.com','password123')
auth_id = myDb.authenticate_user_via_email_password(
    'kyle84684.5@email.com', 'password123')
#admin_id = myDb.authenticate_user_via_email_password('admin@admin.com','admin1')
#myDb.get_all_logs(admin_id)

#myDb.update_bank_info(stock_symbols[0],5,213.25)
print(myDb.get_account_balance(auth_id, 'Account v1'))
#myDb.push_log('2019-11-14 15:11:36',log_message='TESTING LOGGING FUNCTIONALITY')

#myDb.update_user_info(auth_id,'Account v1',stock_symbols[0],200,1520.24)
#myDb.update_user_balance(auth_id,'Account v1',20.24)
#myDb.create_new_account_for_user(auth_id,'Account v1')
#myDb.create_new_account_for_user(auth_id,'Account v2')
#myDb.create_new_account_for_user(auth_id,'Account v3')
'''
#try:
    myDb.create_new_account_for_user(auth_id,'Account v4')
except RuntimeError:
    print('Stopped adding an invalid number of accounts')

#myDb.delete_all_users()
#'''

#myDb.delete_autheticated_user_from_auth_id(auth_id)
