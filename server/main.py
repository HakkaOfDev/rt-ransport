from flask import Flask, render_template, jsonify
from flask_restplus import Api, Resource
import json
import requests

app = Flask(__name__)
api = Api(app=app, version='0.1', title='RT\'ransport API', description='', validate=True)

if __name__ == "__main__":
    app.run(debug=True, port=8887, host='localhost')
