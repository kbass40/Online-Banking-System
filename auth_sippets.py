 // install requirement
pip install firebase

 // snippet to initialize our firebase database
from firebase import Firebase

const firebaseConfig = {
  apiKey: "AIzaSyB-EZ68VfSTbsGrRTmAqBhbF-SNkurtmA4",
  authDomain: "obs-group8.firebaseapp.com",
  databaseURL: "https://obs-group8.firebaseio.com",
  projectId: "obs-group8",
  storageBucket: "obs-group8.appspot.com",
  messagingSenderId: "107046196516",
  appId: "1:107046196516:web:2db03aec2aa107ea47cfb1",
  measurementId: "G-MWV31E677L"
};

firebase = Firebase(config)


 // log in with email and password
# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Joe Tilsed"
}

# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])


 // tokens expire after 1 hour so need to refresh
user = auth.sign_in_with_email_and_password(email, password)

# before the 1 hour expiry:
user = auth.refresh(user['refreshToken'])

# now we have a fresh token
user['idToken']


 // create user
 auth.create_user_with_email_and_password(email, password)


 // password reset
 auth.send_password_reset_email("email")
