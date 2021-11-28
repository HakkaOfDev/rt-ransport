import requests
from flask import render_template, session

from client.routes import app


@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')


@app.route('/prices')
def prices():
    return render_template('prices.html')


@app.route('/my-parcels')
def my_parcels():
    parcels = requests.get('http://127.0.0.1:8886/api/v1/entities/parcels/get/users/' + session['user']['ref'])
    return render_template('my-parcels.html', parcels=(None, parcels.json())[parcels.status_code == 200])


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/authentication')
def authentication():
    return render_template('authentication.html')


@app.route('/deposition')
def deposition():
    return render_template('deposition.html')
