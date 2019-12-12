import os
import sys
from pathlib import Path
import pytest

# Both parent directories need to be added to function from top-level as well as from local 
path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')
sys.path.append(str(path) + '//..//..')

from Model.Database import AuthenticationDatabase as AuthDB
from Model.Microservice import Microservice as MICROSERVICE
import random

# Integration Test
def test_create_more_than_three_accounts_for_single_user():
    r = str(random.randint(1,100))
    myDb = AuthDB.AuthDatabase()
    myDb.create_new_user('kyle'+r+'@email.com','password123')
    auth_id = myDb.authenticate_user_via_email_password('kyle'+r+'@email.com','password123')
    myDb.create_new_account_for_user(auth_id,'Account v1')
    myDb.create_new_account_for_user(auth_id,'Account v2')
    myDb.create_new_account_for_user(auth_id,'Account v3')

    try:
        myDb.create_new_account_for_user(auth_id,'Account v4')
    except RuntimeError:
        print('Stopped adding an invalid number of accounts')
    except:
        print("Something else went wrong :(")
    finally:
        myDb.delete_autheticated_user_from_auth_id(auth_id)
        return True

# Integration Test
def test_authenticated_create_and_delete_user():
    myDB = AuthDB.AuthDatabase()
    myDB.create_new_user('temp1@gmail.com','password')
    auth_id = myDB.authenticate_user_via_email_password('temp1@gmail.com','password')
    myDB.delete_autheticated_user_from_auth_id(auth_id)
    return True

# Integration test
def test_add_funds_to_user():
	r = str(random.randint(1,100))
	myDb = AuthDB.AuthDatabase()
	myDb.create_new_user('kyle'+r+'@email.com','password123')
	auth_id = myDb.authenticate_user_via_email_password('kyle'+r+'@email.com','password123')
	myDb.create_new_account_for_user(auth_id,'Account v1')

	MICROSERVICE.user_adds_money("5000", 'Account v1', auth_id)

	balance = MICROSERVICE.get_account_balance('Account v1', auth_id)
	
	myDb.delete_autheticated_user_from_auth_id(auth_id)

	return balance == 5000

if __name__ == '__main__':
    successful = True
    successful = successful and test_create_more_than_three_accounts_for_single_user()
    successful = successful and test_authenticated_create_and_delete_user()
    successful = successful and test_add_funds_to_user()

    assert successful == True
