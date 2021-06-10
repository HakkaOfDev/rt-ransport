from flask import render_template

from client.routes import app


@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')


@app.route('/prices')
def prices():
    return render_template('prices.html')


@app.route('/my-parcels')
def myparcels():
    return render_template('my-parcels.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/authentication')
def authentication():
    return render_template('authentication.html')
