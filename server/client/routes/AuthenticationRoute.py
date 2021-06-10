import requests
from flask import request, abort, redirect
from flask_login import login_user, logout_user

from client.routes import app
from tools.Keys import URL_AUTH


@app.route(URL_AUTH + 'login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get('email') is None or request.form.get('password') is None:
            print('no data')
            abort(404)

        email = request.form.get('email')
        password = request.form.get('password')

        user = {
            'as_customer': requests.get("http://10.59.63.34:8886/api/v1/entities/customers/" + email).json(),
            'as_operator': requests.get("http://10.59.63.34:8886/api/v1/entities/operators/" + email).json(),
            'as_supplier': requests.get("http://10.59.63.34:8886/api/v1/entities/suppliers/" + email).json()
        }

        for i in user:
            if user[i] is not None:
                if user[i]['password'] == password:
                    login_user(user)
                    return redirect('/')


@app.route(URL_AUTH + 'logout', methods=['POST'])
def logout():
    logout_user()
    return redirect('/')
