from flask import jsonify, Blueprint, abort

from api.data.workers.Customer import Customer
from api.handlers.Handler import Session, engine, Base
from tools.Keys import URL_CUSTOMERS

customers_bp = Blueprint('customers_bp', __name__)
Base.metadata.create_all(engine)
asession = Session()


@customers_bp.route(URL_CUSTOMERS + 'all', methods=['GET'])
def getAll():
    customers = asession.query(Customer).all()
    response = []
    if len(customers) != 0:
        for customer in customers:
            response.append(customer.as_dict())
        asession.close()
        return jsonify(response)
    else:
        return "Customers not found"


@customers_bp.route(URL_CUSTOMERS + '<string:u_login>', methods=['GET'])
def getByLogin(u_login):
    customer = asession.query(Customer).filter_by(login=u_login).first()
    if customer is not None:
        return jsonify(customer.as_dict())
    abort(404)
