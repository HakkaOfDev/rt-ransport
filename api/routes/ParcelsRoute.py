import random

from flask import Blueprint, jsonify, request, make_response
from sqlalchemy import desc
from sqlalchemy.sql.functions import now

from api.data.Parcel import Parcel
from api.data.actions.Leave import Leave
from api.data.actions.Send import Send
from api.data.actions.Transmit import Transmit
from api.data.platforms.PLD import PLD
from api.data.workers.Operator import Operator
from api.handlers.Handler import Session, engine, Base
from tools.Keys import URL_PARCELS

parcels_bp = Blueprint('parcels_bp', __name__)
Base.metadata.create_all(engine)
asession = Session()


@parcels_bp.route(URL_PARCELS + 'all', methods=['GET'])
def getAll(): # route pour récupérer tous les colis
    parcels = asession.query(Parcel).all()
    response = []
    if len(parcels) != 0:
        for parcel in parcels:
            response.append(parcel.as_dict())
        asession.close()
        return jsonify(response)
    else:
        return "Parcels not found"


@parcels_bp.route(URL_PARCELS + 'get/<string:parcel_ref>', methods=['GET'])
def getByRef(parcel_ref): # route pour un parcel
    parcel = asession.query(Parcel).filter_by(ref=parcel_ref).first()
    if parcel is not None:
        return jsonify(parcel.as_dict())
    else:
        return "Parcel not found"


@parcels_bp.route(URL_PARCELS + 'get/users/<string:user_ref>', methods=['GET'])
def getByUser(user_ref): # route récupération des parcels en fonction d'un user
    parcels = {
        'customer': asession.query(Parcel).filter_by(customer_ref=user_ref).all(),
        'operator': asession.query(Parcel).filter_by(operator_ref=user_ref).all(),
        'supplier': asession.query(Parcel).filter_by(supplier_ref=user_ref).all()
    }
    result = None
    resp = []
    for i in parcels:
        if parcels[i] is None or len(parcels[i]) == 0:
            continue
        for p in parcels[i]:
            resp.append(p.as_dict())
    if resp is not None and len(resp) != 0:
        result = jsonify(resp)
        return make_response(result, 200)
    else:
        return make_response(jsonify({'msg': 'Parcels not found'}), 404)


@parcels_bp.route(URL_PARCELS + 'tracking/<string:parcel_ref>', methods=['GET'])
def track(parcel_ref): # trakc route
    parcel = asession.query(Parcel).filter_by(ref=parcel_ref).first()
    resp = []
    send = asession.query(Send).filter_by(parcel=parcel_ref).order_by(desc('send_date')).all() # tous les envois par ordre décroissant de la date d'envoie
    if send is not None: # si envois non null
        transmit = asession.query(Transmit).filter_by(parcel=parcel_ref).first() # récupère le transmit
        if len(send) == 1 and transmit is None: # si un envoie et un transmit
            pos = asession.query(PLD).filter_by(id_pld=send[0].pld).first()
            send0_dict = send[0].as_dict()
            send0_dict['pos'] = pos.name
            resp.append(send0_dict)
            return make_response(jsonify(resp), 200)
        elif len(send) == 1 and transmit is not None:  # si un envoie et pas de transmit
            pos = asession.query(PLD).filter_by(id_pld=send[0].pld).first()
            send0_dict = send[0].as_dict()
            send0_dict['pos'] = pos.name
            transmit_dict = transmit.as_dict()
            transmit_dict['pos'] = 'Between PLR'
            resp.append(transmit_dict)
            resp.append(send0_dict)
            return make_response(jsonify(resp), 200)
        elif len(send) == 2 and transmit is not None:  # si deux envoies et un transmit
            pos = asession.query(PLD).filter_by(id_pld=send[0].pld).first()
            send0_dict = send[0].as_dict()
            send0_dict['pos'] = pos.name
            transmit_dict = transmit.as_dict()
            transmit_dict['pos'] = "Between PLR"
            pos2 = asession.query(PLD).filter_by(id_pld=send[1].pld).first()
            send1_dict = send[1].as_dict()
            send1_dict['pos'] = pos2.name
            resp.append(send1_dict)
            resp.append(transmit_dict)
            resp.append(send0_dict)
            return make_response(jsonify(resp), 200)
        else:
            return make_response({'msg': 'An error occurred !, please retry again...'}, 404)
    else:
        return make_response({'msg': 'An error occurred !, please retry again...'}, 404)


@parcels_bp.route(URL_PARCELS + 'delete/<string:parcel_ref>', methods=['GET'])  # décorateur
def delete(parcel_ref): # route delete parcel
    parcel = asession.query(Parcel).filter_by(ref=parcel_ref).first()
    try:
        asession.delete(parcel)
        asession.commit()
        return make_response({'msg': 'Delete successful !'}, 200)
    except:
        asession.rollback()
        return make_response({'msg': 'An error occurred !, please retry again...'}, 404)
    finally:
        asession.close()


@parcels_bp.route(URL_PARCELS + 'validation/<string:parcel_ref>', methods=['GET'])  # décorateur
def validation(parcel_ref):
    parcel = asession.query(Parcel).filter_by(ref=parcel_ref).first()  # récupération colis
    current = asession.query(PLD).filter_by(name=parcel.current).first()  # récupération position courante
    end_dest = asession.query(PLD).filter_by(name=parcel.end_dest).first()  # récupération destination finale
    send = asession.query(Send).filter_by(parcel=parcel_ref).order_by(
        desc('send_date')).first()  # récupération du dernier envoie
    if send is not None:  # si l'envoie n'est pas null
        if send.pld_to_plr:  # si l'envoie est pld to plr
            transmit = asession.query(Transmit).filter_by(
                parcel=parcel_ref).first()  # check si un transmit de plr to plr existe
            if transmit is not None:  # si transmit
                transmit.reception_date = now()  # set reception du transmit à la date du clic de validation
                new_send = Send(parcel=parcel_ref, pld=end_dest.id_pld, plr=end_dest.id_plr, send_date=now(),
                                reception_date=None,
                                pld_to_plr=False)  # un nouvel envoie vers la destination finale PLD
                asession.add(new_send)  # ajoute de l'orm à la session
                asession.commit()  # envoie la session pour mettre à jour la bdd
                return make_response({'msg': 'Successful!'}, 200)
            else:  # si aucun transmit
                send.reception_date = now()  # set reception de l'envoie à la date du clic de validation
                transmit = Transmit(parcel=parcel_ref, plr=current.id_plr, dest_plr=end_dest.id_plr, send_date=now(),
                                    reception_date=None)  # créer le transmit
                asession.add(transmit)  # ajoute le transmit à la session
                asession.commit()  # envoie la session pour mettre à jour la bdd
                return make_response({'msg': 'Successful!'}, 200)
        else:  # si non pld to plr
            send.reception_date = now()  # set reception de l'envoie à la date du clic de validation
            parcel.current = end_dest.name  # mets à jour la position courante
            asession.commit()  # envoie la session pour mettre à jour la bdd
            return make_response({'msg': 'Successful!'}, 200)
    return make_response({'msg': 'Error!'}, 404)


@parcels_bp.route(URL_PARCELS + 'add', methods=['POST'])
def addParcel(): # route add parcel
    datas = request.form
    operator = asession.query(Operator).one_or_none()
    if operator is None:
        return make_response({"msg": "Can't find any operators"}, 404)

    # récupération des données du form
    supplier_ref = datas.get('supplier_ref')
    customer_ref = datas.get('customer_ref')
    weight = int(datas.get('weight'))
    width = int(datas.get('width'))
    height = int(datas.get('height'))
    depth = int(datas.get('depth'))
    packaging = datas.get('packaging')
    type = datas.get('type')
    assured = bool(datas.get('assured'))
    fragile = bool(datas.get('fragile'))
    end_dest = datas.get('end_dest')
    start_dest = datas.get('start_dest')

    ref = str(random.random())
    # créer un object Parcel
    parcel = Parcel(ref=ref[2:],
                    operator_ref=operator.ref,
                    customer_ref=customer_ref,
                    supplier_ref=supplier_ref,
                    type=type,
                    height=height,
                    width=width,
                    depth=depth,
                    weight=weight,
                    packaging=packaging,
                    assured=assured,
                    fragile=fragile,
                    current=start_dest,
                    end_dest=end_dest)

    pld = asession.query(PLD).filter_by(name=start_dest).first()
    # créer un object leave
    leave_action = Leave(parcel=ref[2:], pld=pld.id_pld, supplier=supplier_ref, deposit_date=now())
    current = asession.query(PLD).filter_by(name=parcel.current).first()
    end_dest = asession.query(PLD).filter_by(name=parcel.end_dest).first()
    send = None
    if (current.id_plr == 13 and end_dest.id_plr == 13) or (current.id_plr == 12 and end_dest.id_plr == 12): # on check si c'est un chemin pld to pld
        send = Send(parcel=parcel.ref, pld=end_dest.id_pld, plr=end_dest.id_plr, send_date=now(), reception_date=None,
                    pld_to_plr=False)
    elif current.id_plr != end_dest.id_plr: # sinon
        send = Send(parcel=parcel.ref, pld=end_dest.id_pld, plr=current.id_plr, send_date=now(), reception_date=None,
                    pld_to_plr=True)

    try:
        # ajoute les données et on commit
        asession.add(parcel)
        asession.add(leave_action)
        asession.add(send)
        asession.commit()
        return make_response({'msg': 'Deposition successful !'}, 200)
    except:
        asession.rollback()
        return make_response({'msg': 'An error occurred !, please retry again...'}, 404)
    finally:
        asession.close()
