from flask import jsonify, Blueprint, make_response

from api.data.workers.Supplier import Supplier
from api.handlers.Handler import Session, engine, Base
from tools.Keys import URL_SUPPLIERS

suppliers_bp = Blueprint('suppliers_bp', __name__)
Base.metadata.create_all(engine)
asession = Session()


@suppliers_bp.route(URL_SUPPLIERS + 'all', methods=['GET'])
def getAll(): # route pour récupérer tous les fournisseurs
    suppliers = asession.query(Supplier).all()
    response = []
    if len(suppliers) != 0:
        for supplier in suppliers:
            response.append(supplier.as_dict())
        asession.close()
        return jsonify(response)
    else:
        return "Customers not found"


@suppliers_bp.route(URL_SUPPLIERS + '<string:u_login>', methods=['GET'])
def getByLogin(u_login): # route pour récupérer un fournisseur en fonction de son login
    supplier = asession.query(Supplier).filter_by(login=u_login).first()
    asession.close()
    if supplier is not None:
        return jsonify(supplier.as_dict())
    else:
        return make_response({'msg': 'Not found'}, 404)
