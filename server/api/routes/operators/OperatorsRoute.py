from flask import jsonify, Blueprint, abort

from api.data.workers.Operator import Operator
from api.handlers.Handler import Session, engine, Base
from tools.Keys import URL_CUSTOMERS, URL_OPERATORS

operators_bp = Blueprint('operators_bp', __name__)
Base.metadata.create_all(engine)
asession = Session()


@operators_bp.route(URL_OPERATORS + 'all', methods=['GET'])
def getAll():
    operators = asession.query(Operator).all()
    response = []
    if len(operators) != 0:
        for operator in operators:
            response.append(operator.as_dict())
        asession.close()
        return jsonify(response)
    else:
        return "Operators not found"


@operators_bp.route(URL_CUSTOMERS + '<string:u_login>', methods=['GET'])
def getByLogin(u_login):
    operator = asession.query(Operator).filter_by(login=u_login).first()
    if operator is not None:
        return jsonify(operator)
    abort(404)
