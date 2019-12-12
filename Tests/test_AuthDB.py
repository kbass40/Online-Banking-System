from Model.Database import AuthenticationDatabase as AuthDB
import pytest

def test_AuthDB_creation():
    AuthDB.AuthDatabase()

def test_fail_authenticate_user_with_bad_email_type():
    with pytest.raises(TypeError):
        myDB = AuthDB.AuthDatabase()
        myDB.authenticate_user_via_email_password(1685438,'156463543')

def test_fail_authenticate_user_with_bad_password_type():
    with pytest.raises(TypeError):
        myDB = AuthDB.AuthDatabase()
        myDB.authenticate_user_via_email_password('test@gmail.com',156463543)

def test_fail_authenticate_user_with_invalid_email():
    with pytest.raises(SyntaxError):
        myDB = AuthDB.AuthDatabase()
        myDB.authenticate_user_via_email_password('@gmail.com','156463543')

def test_authenticate_valid_user():
    myDB = AuthDB.AuthDatabase()
    myDB.authenticate_user_via_email_password('kyle84684.5@email.com','password123')

def test_fail_create_user_with_bad_email_type():
    with pytest.raises(TypeError):
        myDB = AuthDB.AuthDatabase()
        myDB.create_new_user(1685438,'156463543')

def test_fail_create_user_with_bad_password_type():
    with pytest.raises(TypeError):
        myDB = AuthDB.AuthDatabase()
        myDB.create_new_user('test@gmail.com',156463543)

def test_fail_create_user_with_invalid_email():
    with pytest.raises(SyntaxError):
        myDB = AuthDB.AuthDatabase()
        myDB.create_new_user('@gmail.com','156463543')

def test_fail_create_user_with_invalid_password():
    with pytest.raises(ValueError):
        myDB = AuthDB.AuthDatabase()
        myDB.create_new_user('temp@gmail.com','passwoo')

def test_authenticated_create_and_delete_user():
    myDB = AuthDB.AuthDatabase()
    myDB.create_new_user('temp@gmail.com','password')
    auth_id = myDB.authenticate_user_via_email_password('temp@gmail.com','password')
    myDB.delete_autheticated_user_from_auth_id(auth_id)