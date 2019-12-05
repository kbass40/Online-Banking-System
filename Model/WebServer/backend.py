import os
import sys
from pathlib import Path
import requests
from json2html import *

# Both parent directories need to be added to function from top-level as well as from local 
path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')
sys.path.append(str(path) + '//..//..')

#import mock_auth, mock_signUp
import urllib
from Model.Database import AuthenticationDatabase as authdb
from flask import Flask, render_template, request, redirect, url_for

template_dir = str(path) + '//..//HTML'
app = Flask(__name__, template_folder=template_dir, static_folder=template_dir + "/static")
print(app.static_folder)

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
    #authenticated = mock_auth.auth(uname, psw)

    #get session token
    temp = authdb.AuthDatabase()

    try:
        token = temp.authenticate_user_via_email_password(email, psw)
    except Exception as e:
        return render_template("failedLogin.htm").format(error=str(e))

    response = app.make_response(redirect(url_for("accounts")))
    response.set_cookie("authenticated", value=token)

    print(token)

    return response


@app.route('/Microservices')
def mservices():
    return render_template('mservices.htm')

#Routes for all the web services
#Ubisoft microservice web page (have to make the html)
@app.route('/Microservices/Ubisoft')
def ubi():
    return render_template('ubi.htm')

@app.route('/Microservices/Ubisoft/Price')
def ubi_price():
    return json2html.convert(json=requests.get("http://localhost:8000/api/ubisoft/get-last").text)

#Ubisoft buy and sell
@app.route('/Microservices/Ubisoft/Buy')
def ubi_buy():
    return render_template('microservices_buy.htm').format(ref="/Microservices/Ubisoft", text="Ubisoft")

@app.route('/Microservices/Ubisoft/Buy', methods=['POST'])
def ubi_buy_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/ubisoft/buy-stocks=" + quantity + "/" + token).text)

@app.route('/Microservices/Ubisoft/Sell')
def ubi_sell():
    return render_template('microservices_sell.htm').format(ref="/Microservices/Ubisoft", text="Ubisoft")

@app.route('/Microservices/Ubisoft/Sell', methods=['POST'])
def ubi_sell_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/ubisoft/sell-stocks=" + quantity + "/" + token).text)

#Google microservice web page 
#Google get price
@app.route('/Microservices/Google')
def google():
    return render_template('google.htm')

@app.route('/Microservices/Google/Price')
def google_price():
    return json2html.convert(json=requests.get("http://localhost:8000/api/google/get-last").text)

#Google buy and sell
@app.route('/Microservices/Google/Buy')
def google_buy():
    return render_template('microservices_buy.htm').format(ref="/Microservices/Google", text="Google")

@app.route('/Microservices/Google/Buy', methods=['POST'])
def google_buy_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/google/buy-stocks=" + quantity + "/" + token).text)

@app.route('/Microservices/Google/Sell')
def google_sell():
    return render_template('microservices_sell.htm').format(ref="/Microservices/Google", text="Google")

@app.route('/Microservices/Google/Sell', methods=['POST'])
def google_sell_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/google/sell-stocks=" + quantity + "/" + token).text)

#Facebook microservice web page 
#Facebook get price
@app.route('/Microservices/Facebook')
def fbook():
    return render_template('fbook.htm')

@app.route('/Microservices/Facebook/Price')
def fbook_price():
    return json2html.convert(json=requests.get("http://localhost:8000/api/facebook/get-last").text)

#Facebook buy and sell
@app.route('/Microservices/Facebook/Buy')
def fbook_buy():
    return render_template('microservices_buy.htm').format(ref="/Microservices/Facebook", text="Facebook")

@app.route('/Microservices/Facebook/Buy', methods=['POST'])
def fbook_buy_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/facebook/buy-stocks=" + quantity + "/" + token).text)

@app.route('/Microservices/Facebook/Sell')
def fbook_sell():
    return render_template('microservices_sell.htm').format(ref="/Microservices/Facebook", text="Facebook")

@app.route('/Microservices/Facebook/Sell', methods=['POST'])
def fbook_sell_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/facebook/sell-stocks=" + quantity + "/" + token).text)

#Apple microservice web page 
#Apple get price
@app.route('/Microservices/Apple')
def aple():
    return render_template('aple.htm')

@app.route('/Microservices/Google/Price')
def aple_price():
    return json2html.convert(json=requests.get("http://localhost:8000/api/apple/get-last").text)

#Apple buy and sell
@app.route('/Microservices/Apple/Buy')
def aple_buy():
    return render_template('microservices_buy.htm').format(ref="/Microservices/Apple", text="Apple")

@app.route('/Microservices/Apple/Buy', methods=['POST'])
def aple_buy_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/apple/buy-stocks=" + quantity + "/" + token).text)

@app.route('/Microservices/Apple/Sell')
def aple_sell():
    return render_template('microservices_sell.htm').format(ref="/Microservices/Apple", text="Apple")

@app.route('/Microservices/Apple/Sell', methods=['POST'])
def aple_sell_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/apple/sell-stocks=" + quantity + "/" + token).text)

#Oracle microservice web page 
#Oracle get price
@app.route('/Microservices/Oracle')
def oracle():
    return render_template('oracle.htm')

@app.route('/Microservices/Oracle/Price')
def oracle_price():
    return json2html.convert(json=requests.get("http://localhost:8000/api/oracle/get-last").text)

#Oracle buy and sell
@app.route('/Microservices/Oracle/Buy')
def oracle_buy():
    return render_template('microservices_buy.htm').format(ref="/Microservices/Oracle", text="Oracle")

@app.route('/Microservices/Oracle/Buy', methods=['POST'])
def oracle_buy_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/oracle/buy-stocks=" + quantity + "/" + token).text)

@app.route('/Microservices/Oracle/Sell')
def oracle_sell():
    return render_template('microservices_sell.htm').format(ref="/Microservices/Oracle", text="Oracle")

@app.route('/Microservices/Oracle/Sell', methods=['POST'])
def oracle_sell_post():
    quantity = request.form.get('quantity')
    token = request.cookies.get('authenticated')
    if token is None:
        #placeholder
        return 'Need a token'

    return json2html.convert(json=requests.get("http://localhost:8000/api/oracle/sell-stocks=" + quantity + "/" + token).text)

#Sign up page initialization
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
        authdb.AuthDatabase().create_new_user(email, psw)
    except Exception as e:
        return render_template("failedSignUp.htm").format(error=str(e))


    #if registered:
        #return render_template('successfulSignUp.htm')
    #else:
        #return render_template('failedSignUp.htm')

    data = {
        "email":email,
        "psw":psw
    }

    return redirect(url_for('loginPost'), code=307)
    
    #return render_template('successfulSignUp.htm')

#User's account creation
@app.route('/Accounts')
def accounts():
    acc = authdb.AuthDatabase().get_user_accounts(request.cookies.get("authenticated"))
    acc_str = ""
    acc_length = 0
    if acc is not None:
        for i in acc:
            acc_str = acc_str + i + ","
        acc_str = acc_str[:-1]
        acc_length = len(acc)

    return render_template("account_selection.htm", arr=acc_str, len=acc_length)

@app.route('/Accounts', methods=['POST'])
def accountsPost():
    name = request.form.get("name")

    #Updating database
    try:
        authdb.AuthDatabase().create_new_account_for_user(request.cookies.get("authenticated"), name)
    except RuntimeError as e:
        return str(e)

    return redirect(url_for('accounts'))

#Dashboard
@app.route('/Accounts/Dashboard/<name>')
def dashboard(name):
    #get name of the account

    #Getting Stock info
    stock_info = authdb.AuthDatabase().get_account_info(request.cookies.get("authenticated"), name)


    return render_template("dashboard.htm", uname=name, bal=stock_info['balance'], appl=stock_info['AAPL']['stock_num'], 
    goog=stock_info['GOOGL']['stock_num'], fcb=stock_info['FB']['stock_num'], orc=stock_info['ORCL']['stock_num'], 
    ubi=stock_info['UBSFY']['stock_num'])

@app.route('/Accounts/Dashboard/<name>', methods=['POST'])
def dashboardPost(name):
    token = request.cookies.get("authenticated")
    delta = float(request.form.get("amount"))

    authdb.AuthDatabase().update_user_balance(token, name, delta)

    return redirect(url_for('dashboard', name=name))
    

if __name__ == "__main__":
    app.run()
