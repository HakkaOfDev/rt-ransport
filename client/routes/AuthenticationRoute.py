import requests
from flask import request, abort, redirect, session, flash, render_template

from client.routes import app


@app.route('/authentication/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get('email') is None or request.form.get('password') is None:
            abort(404)

        for i in ["customers", "suppliers", "operators"]:
            user = requests.get(f"http://127.0.0.1:8886/api/v1/entities/{i}/" + request.form.get('email'))
            if user is not None and user.status_code != 404:
                session['user'] = user.json()
                flash('Login successful !', 'success')
                return render_template('index.html')
            else:
                continue
        flash('An error occured...', 'error')
        return render_template('authentication.html')


@app.route('/authentication/logout')
def logout():
    session['user'] = None
    return redirect('/')
