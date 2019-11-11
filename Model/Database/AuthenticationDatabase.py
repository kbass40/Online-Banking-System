import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

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

    def get_user_info(self, id_token):
        print(self._db.child('users').get(id_token))

myDb = AuthDatabase()
user_id = myDb.authenticate_user_via_email_password('daniel.tymecki@gmail.com','password')
print(user_id)
myDb.get_user_info('iskbvlksdhbvfksjbvkue')

#print(jwt.decode(user_id,'secret', algorithms=['RS256']))