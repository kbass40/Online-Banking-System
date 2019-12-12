import os
import sys
from pathlib import Path
# Both parent directories need to be added to function from top-level as well as from local 
path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')
sys.path.append(str(path) + '//..//..')

from Database import AuthenticationDatabase as authdb
import mock_adminAuthentication
from flask import Flask, render_template, request, redirect, url_for
from json2html import *
from requests import HTTPError

template_dir = str(path) + '//..//HTML'
app = Flask(__name__, template_folder=template_dir, static_folder=template_dir + "/static")

#home directory
@app.route('/admin')
def admin_home():
    return render_template('admin_home.htm')

#admin home post request
@app.route('/admin', methods=['POST'])
def admin_home_auth():
    #getting user info
    email = request.form.get('email')
    psw = str(request.form.get('psw'))
    if not (email == "admin@admin.com"):
        return 'placeholder'

    #send it to get authenticated
    #currently using a test double
    #authenticated = mock_adminAuthentication.auth(uname, psw)

    temp = authdb.AuthDatabase()

    try:
        token = temp.authenticate_user_via_email_password(email, psw)
    except Exception as e:
        return render_template("unauthenticated_admin.htm").format(error=str(e))

    bank_info = []

    try:
        for i in authdb.stock_symbols:
            bank_info.append(authdb.AuthDatabase().get_bank_info(i))
    except HTTPError:
        print("Oops something didn't go as planned")

    #creating a placeholder token and setting it as a cookie
    response = app.make_response(render_template('admin_dashboard.htm', 
    apple_amount=bank_info[0]['stock_num'], apple_gain_loss=bank_info[0]['gain-loss'],
    fcb_amount=bank_info[1]['stock_num'], fcb_gain_loss=bank_info[1]['gain-loss'],
    google_amount=bank_info[2]['stock_num'], google_gain_loss=bank_info[2]['gain-loss'],
    oracle_amount=bank_info[3]['stock_num'], oracle_gain_loss=bank_info[3]['gain-loss'],
    ubi_amount=bank_info[4]['stock_num'], ubi_gain_loss=bank_info[4]['gain-loss']))

    response.set_cookie("authenticated", value=token)
    return response


#Print logs
@app.route('/admin/logs')
def print_logs():
    #getting user token
    token = request.cookies.get('authenticated')

    try:
        logs = authdb.AuthDatabase().get_all_logs(token)
        stripped_logs = {}
        for i,key in enumerate(logs):
            stripped_logs[i] = logs[key]
        return json2html.convert(json=stripped_logs)
    except HTTPError:
        return 'Logs cannot be printed at this time.'

#get bank balace
@app.route('/admin/balance')
def bank_stocks():
    bank_info = []

    try:
        for i in authdb.stock_symbols:
            bank_info.append(authdb.AuthDatabase().get_bank_info(i))
    except HTTPError:
        return 'Something went wrong with the operation'

    


if __name__=="__main__":
    #running the server on port 5555
    app.run(port=5555)