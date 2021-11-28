from flask import Flask

app = Flask(__name__)

from client.routes import MainRoute, AuthenticationRoute, ParcelsRoute
