import json

from flask import Blueprint, request, abort, Response, session

from data.workers.Customer import Customer
from data.workers.Operator import Operator
from data.workers.Supplier import Supplier
from encoders.Encoder import Encoder
from handlers.Handler import Session, engine, Base
from tools.Keys import *

authentication_bp = Blueprint('authentiation_bp', __name__)
Base.metadata.create_all(engine)
asession = Session()


@authentication_bp.route(URL_AUTH + 'login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    asession.add(
        Customer(6, 'aCustomerRef', 'Ecila', 'Alice', '32 Rue des Caribous 32000 Caribouville', 'login1', 'pass1'))
    asession.commit()

    for i in [Customer, Supplier, Operator]:
        user = asession.query(i).filter(i.login == email).first()
        if user is not None:
            if user.password == password:
                session['user'] = user.as_dict()
                abort(Response({'res': 'Succes login', 'code': 200}, status=200))
            else:
                return {'res': 'Invalid credentials', 'code': 401}
        else:
            return {'res': 'User doesn\'t exists', 'code': 404}


@authentication_bp.route(URL_AUTH + 'logout', methods=['POST'])
def logout():
    session['user'] = None
    return Response('Logout successful', status=200, mimetype='application/json')


@authentication_bp.route(URL_AUTH + 'me', methods=['GET'])
def get():
    return {'user': session['user']}