import os
import mock_auth, mock_signUp
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
    uname = request.form.get("uname")
    psw = request.form.get("psw")

    #send it to authentication
    #currently using a mock
    authenticated = mock_auth.auth(uname, psw)

    #get session token
    #currently using a placeholder
    token ="atrgewa123456678"

    if authenticated:
        return render_template("successfulLogin.htm").format(token=token)

    else:
        return render_template("failedLogin.htm")


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
    psw = request.form.get('psw')

    #using a mock
    registered = mock_signUp.signUp(uname, email, psw)

    if registered:
        return render_template('successfulSignUp.htm')
    else:
        return render_template('failedSignUp.htm')
    

if __name__ == "__main__":
    app.run()