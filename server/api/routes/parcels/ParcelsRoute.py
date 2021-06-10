from flask import Blueprint, jsonify

from api.data import Parcel
from api.handlers.Handler import Session, engine, Base
from tools.Keys import URL_PARCELS

parcels_bp = Blueprint('parcels_bp', __name__)
Base.metadata.create_all(engine)
asession = Session()


@parcels_bp.route(URL_PARCELS + 'all', methods=['GET'])
def getAll():
    parcels = asession.query(Parcel).all()
    response = []
    if len(parcels) != 0:
        for parcel in parcels:
            response.append(parcel.as_dict())
        asession.close()
        return jsonify(response)
    else:
        return "Parcels not found"


@parcels_bp.route(URL_PARCELS + 'get/<int:parcel_id>', methods=['GET'])
def getById(parcel_id):
    parcel = asession.query(Parcel).filter(Parcel.parcel_id == parcel_id).first()
    if parcel is not None:
        return jsonify(parcel)
    else:
        return "Parcel not found"


@parcels_bp.route(URL_PARCELS + 'get/users/<int:user_ref>', methods=['GET'])
def getByUser(user_ref):
    parcels = {
        'customer': asession.query(Parcel).filter_by(Parcel.customer_ref == user_ref).all(),
        'operator': asession.query(Parcel).filter_by(Parcel.operator_ref == user_ref).all(),
        'supplier': asession.query(Parcel).filter_by(Parcel.supplier_ref == user_ref).all()
    }
    result = None
    for i in parcels:
        if parcels[i] is not None:
            result = jsonify(parcels[i])
        else:
            result = None
    if result is not None:
        return result
    else:
        return "Parcels not found"


@parcels_bp.route(URL_PARCELS + 'add', methods=['POST'])
def addParcel():
    pass
