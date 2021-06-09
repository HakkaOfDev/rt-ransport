from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

from api.routes.CustomersRoute import customers_bp
from api.routes.authentication.AuthenticationRoute import authentication_bp
from api.routes.parcels.ParcelsRoute import parcels_bp
from tools.Keys import DEBUG

app = Flask(__name__)

cors_config = {
    "origins": ["*"],
    "methods": ["OPTIONS", "GET", "POST"],
    "Access-Control-Allow-Origin": "*",
}
cors = CORS(app, supports_credentials=True, resources={"/api/v1/*": cors_config})

api_restful = Api(app=app, version='0.1', title='RT\'ransport API', description='', validate=True)
app.register_blueprint(authentication_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(parcels_bp)

if __name__ == "__main__":
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['REMEMBER_COOKIE_HTTPONLY'] = True
    app.config['JSON_SORT_KEYS'] = False
    app.config['SECRET_KEY'] = "Test"
    app.run(debug=DEBUG, port=8887, host='localhost')