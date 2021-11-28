from flask import jsonify, Blueprint, make_response

from api.data.workers.Operator import Operator
from api.handlers.Handler import Session, engine, Base
from tools.Keys import URL_OPERATORS

operators_bp = Blueprint('operators_bp', __name__)
Base.metadata.create_all(engine)
asession = Session()


@operators_bp.route(URL_OPERATORS + 'all', methods=['GET'])
def getAll(): # route pour récupérer tous les opérateurs
    operators = asession.query(Operator).all()
    response = []
    if len(operators) != 0:
        for operator in operators:
            response.append(operator.as_dict())
        asession.close()
        return jsonify(response)
    else:
        return "Operators not found"


@operators_bp.route(URL_OPERATORS + '<string:u_login>', methods=['GET'])
def getByLogin(u_login): # route pour récupérer un opérateur en fonction de son login
    operator = asession.query(Operator).filter_by(login=u_login).first()
    asession.close()
    if operator is not None:
        return jsonify(operator.as_dict())
    else:
        return make_response({'msg': 'Not found'}, 404)
