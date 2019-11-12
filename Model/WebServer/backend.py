import os
import sys
sys.path.append(os.path.abspath('..'))
#import mock_auth, mock_signUp
import urllib
from Database import AuthenticationDatabase as authdb
from flask import Flask, render_template, request

template_dir = os.path.abspath('../HTML')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('home.htm')

#Handles get requests sent to /login
@app.route('/login')
def login():
    #have to manage getting the credentials
    return render_template('login.htm')

#Handles post requests sent to /login
@app.route('/login', methods=['POST'])
def loginPost():
    #getting the user inputs
    email = request.form.get("email")
    psw = str(request.form.get("psw"))

    #send it to authentication
    #currently using a mock
    #authenticated = mock_auth.auth(uname, psw)

    #get session token
    #currently using a placeholder
    temp = authdb.AuthDatabase()

    try:
        token = temp.authenticate_user_via_email_password(email, psw)
    except Exception as e:
        return render_template("failedLogin.htm").format(error=str(e))

    return render_template("successfulLogin.htm").format(token=token)


@app.route('/Microservices')
def mservices():
    return render_template('mservices.htm')

#Routes for all the web services
#Ubisoft microservice web page (have to make the html)
@app.route('/Microservices/Ubisoft')
def ubi():
    return render_template('ubi.htm')

#Ubisoft buy and sell
#placeholders for now
@app.route('/Microservices/Ubisoft/Buy')
def ubi_buy():
    return 'bought'

@app.route('/Microservices/Ubisoft/Sell')
def ubi_sell():
    return 'sold'

@app.route('/SignUp')
def signUp():
    return render_template('signUp.htm')

#Handles sign up post requests
@app.route('/SignUp', methods=['POST'])
def signUpPost():
    #getting user inputs
    uname = request.form.get('uname')
    email = request.form.get('email')
    psw = str(request.form.get('psw'))

    if len(psw) < 7:
        short = "password needs to be at least 8 characters long"
        return render_template("failedSignUp.htm").format(error=str(short))

    #using a mock
    #registered = mock_signUp.signUp(uname, email, psw)

    try:
        authdb.AuthDatabase().create_new_user(email, uname, psw)
    except Exception as e:
        return render_template("failedSignUp.htm").format(error=str(e))


    #if registered:
        #return render_template('successfulSignUp.htm')
    #else:
        #return render_template('failedSignUp.htm')
    
    return render_template('successfulSignUp.htm')
    

if __name__ == "__main__":
    app.run()
