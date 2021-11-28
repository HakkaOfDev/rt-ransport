from flask import Flask
from flask_restplus import Api

from api.routes.CustomersRoute import customers_bp
from api.routes.OperatorsRoute import operators_bp
from api.routes.ParcelsRoute import parcels_bp
from api.routes.SuppliersRoute import suppliers_bp

app = Flask(__name__)

api_restful = Api(app=app, version='0.1', title='RT\'ransport API', description='', validate=True)
app.register_blueprint(customers_bp)
app.register_blueprint(operators_bp)
app.register_blueprint(suppliers_bp)
app.register_blueprint(parcels_bp)
