import os
import sys
sys.path.append(os.path.abspath(".."))
from pathlib import Path

# Both parent directories need to be added to function from top-level as well as from local 
path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')
sys.path.append(str(path) + '//..//..')

from Database import AuthenticationDatabase as authdb
import mock_adminAuthentication
from flask import Flask, render_template, request, redirect, url_for

template_dir = os.path.abspath('../HTML')
app = Flask(__name__, template_folder=template_dir)

#home directory
@app.route('/')
def admin_home():
    return render_template('admin_home.htm')

#admin home post request
@app.route('/', methods=['POST'])
def admin_home_auth():
    #getting user info
    email = request.form.get('email')
    psw = str(request.form.get('psw'))

    #send it to get authenticated
    #currently using a test double
    #authenticated = mock_adminAuthentication.auth(uname, psw)

    temp = authdb.AuthDatabase()

    try:
        token = temp.authenticate_user_via_email_password(email, psw)
    except Exception as e:
        return render_template("unauthenticated_admin").format(error=str(e))

    #creating a placeholder token and setting it as a cookie
    token = "abheo457612n"
    response = app.make_response(render_template('authenticated_admin.htm'))
    response.set_cookie("authenticated", value=token)
    return response

#Authentication Logs
@app.route('/auth-logs')
def auth_logs():
    #getting user token
    token = request.cookies.get('authenticated')

    valid = False

    #have to find a way to validate token, set to True for now
    if token is not None:
        valid = True

    if valid:
        #have to work with database or another function to get all the logs
        return 'Logs'
    else:
        return 'Log in to access this functionality'


#Have to change functionality for the next two
#Transaction Logs
@app.route('/transact-logs')
def transact_logs():
    #getting user token
    token = request.cookies.get('authenticated')

    valid = False

    #have to find a way to validate token, set to True for now
    if token is not None:
        valid = True

    if valid:
        return 'Logs'
    else:
        return 'Log in to access this functionality'

#Stock Transaction
@app.route('/stock-transact')
def stock_transact():
    #getting user token
    token = request.cookies.get('authenticated')

    valid = False

    #have to find a way to validate token, set to True for now
    if token is not None:
        valid = True

    if valid:
        return 'Logs'
    else:
        return 'Log in to access this functionality'


if __name__=="__main__":
    #running the server on port 5555
    app.run(port=5555)