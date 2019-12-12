import os
import sys
from pathlib import Path
import pytest

# Both parent directories need to be added to function from top-level as well as from local 
path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')
sys.path.append(str(path) + '//..//..')

from Model.Database import AuthenticationDatabase as AuthDB
import random

# @pytest.mark.xfail
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
        pass
    except:
        print("Something else went wrong :(")
    finally:
        myDb.delete_autheticated_user_from_auth_id(auth_id)
