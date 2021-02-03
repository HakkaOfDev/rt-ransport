from flask import Flask
from flask_restplus import Api
from flask_cors import CORS

from api.routes.UserRoute import users_bp

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api_restful = Api(app=app, version='0.1', title='RT\'ransport API', description='', validate=True)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.config['CORS_HEADERS'] = 'application/json'
    app.config['JSON_SORT_KEYS'] = False
    app.run(debug=True, port=8887, host='localhost')
