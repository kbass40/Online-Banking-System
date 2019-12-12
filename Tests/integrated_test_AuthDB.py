import os
import sys
from pathlib import Path

# Both parent directories need to be added to function from top-level as well as from local 
path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')
sys.path.append(str(path) + '//..//..')

from Model.Database import AuthenticationDatabase as AuthDB
import random

def test_create_more_than_three_accounts_for_single_user():
    r = str(random.randint(1,100))
    myDb = AuthDB.AuthDatabase()
    myDb.delete_all_random_kyles()
    myDb.create_new_user('kyle'+r+'@email.com','password123')
    auth_id = myDb.authenticate_user_via_email_password('kyle'+r+'@email.com','password123')
    myDb.create_new_account_for_user(auth_id,'Account v1')
    myDb.update_user_balance(auth_id,'Account v1',5000.00)
    myDb.create_new_account_for_user(auth_id,'Account v2')

    try:
        myDb.create_new_account_for_user(auth_id,'Account v3')
    except RuntimeError:
        print('Stopped adding an invalid number of accounts')
    except:
        print("Something else went wrong :(")
    
    myDb.delete_autheticated_user_from_auth_id(auth_id)


test_create_more_than_three_accounts_for_single_user()
