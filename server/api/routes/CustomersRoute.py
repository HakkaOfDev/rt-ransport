from flask import jsonify, Blueprint

from data.workers.Customer import Customer
from handlers.Handler import Session, engine, Base
from tools.Keys import *

customers_bp = Blueprint('customers_bp', __name__)
Base.metadata.create_all(engine)
session = Session()


@customers_bp.route(URL_CUSTOMERS + 'all', methods=['GET'])
def getAll():
    customers = session.query(Customer).all()
    response = []
    if len(customers) != 0:
        for customer in customers:
            response.append(customer.as_dict())
        session.close()
        return jsonify(response)
    else:
        return "Customers not found"
