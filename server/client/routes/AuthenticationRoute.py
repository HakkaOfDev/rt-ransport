import requests
from flask import request, abort, redirect, session
from client.routes import app


@app.route('/authentication/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get('email') is None or request.form.get('password') is None:
            abort(404)

        email = request.form.get('email')
        password = request.form.get('password')

        for i in ['customers', 'operators', 'suppliers']:
            user = requests.get("http://127.0.0.1:8886/api/v1/entities/" + i + "/" + email).json()
            if user is not None:
                if user['password'] == password:
                    session['user'] = user
                    return redirect('/')


@app.route('/authentication/logout', methods=['POST'])
def logout():
    session['user'] = None
    return redirect('/')
