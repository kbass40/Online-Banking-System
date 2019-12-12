import os
import sys
sys.path.append(os.path.abspath(".."))
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
    response = app.make_response(render_template('admin_dashboard.htm'))
    response.set_cookie("authenticated", value=token)
    return response


#Print logs
@app.route('/admin_dashboard')
def print_logs():
    #getting user token
    token = request.cookies.get('authenticated')

    valid = False

    #have to find a way to validate token, set to True for now
    if token is not None:
        valid = True

    if valid:
        #have to work with database or another function to get all the logs
    return json2html.convert(json=requests.get("http://localhost:8000/api/admin_dashboard").text)
    else:
        return 'Logs cannot be printed at this time.'


#Handles post requests sent to /login
@app.route('/admin_login', methods=['POST'])
def adminLogin():
    #getting the user inputs
    email = request.form.get("email")
    psw = str(request.form.get("psw"))

    if ((email == "admin@admin.com") && (psw == "admin1"))
    #send it to authentication
    #authenticated = mock_auth.auth(uname, psw)

    #get session token
    temp = authdb.AuthDatabase()

    try:
        token = temp.authenticate_user_via_email_password(email, psw)
    except Exception as e:
        return render_template("failedLogin.htm").format(error=str(e))

    response = app.make_response(redirect(url_for("admin_dashboard")))
    response.set_cookie("admin", value=token)

    print(token)

    return response
    


if __name__=="__main__":
    #running the server on port 5555
    app.run(port=5555)