from flask import jsonify, Blueprint, make_response

from api.data.workers.Customer import Customer
from api.handlers.Handler import Session, engine, Base
from tools.Keys import URL_CUSTOMERS

customers_bp = Blueprint('customers_bp', __name__)
Base.metadata.create_all(engine) # création des ORM si non créer
asession = Session() # session de connection à la bdd


@customers_bp.route(URL_CUSTOMERS + 'all', methods=['GET'])
def getAll(): # route pour récupérer tous les clients
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
def getByLogin(u_login): # route pour récupérer un client en fonction de son login
    customer = asession.query(Customer).filter_by(login=u_login).first()
    asession.close()
    if customer is not None:
        return jsonify(customer.as_dict())
    else:
        return make_response({'msg': 'Not found'}, 404)
