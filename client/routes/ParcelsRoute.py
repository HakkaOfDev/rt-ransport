import requests
from flask import request, redirect, flash, render_template

from client.routes import app


@app.route('/parcels/deposition', methods=['POST', 'GET'])
def send_deposition():
    if request.method == 'POST':
        # if request.form.get('email') is None or request.form.get('password') is None:
        #     abort(404)

        supplier_ref = request.form.get('supplier_ref')
        customer_ref = request.form.get('customer_ref')
        weight = request.form.get('weight')
        width = request.form.get('width')
        height = request.form.get('height')
        depth = request.form.get('depth')
        packaging = request.form.get('packaging')
        type = request.form.get('type')
        assured = request.form.get('assured')
        fragile = request.form.get('fragile')
        start_dest = request.form.get('start_dest')
        end_dest = request.form.get('end_dest')

        parcel_dict = {
            'supplier_ref': supplier_ref,
            'customer_ref': customer_ref,
            'weight': weight,
            'width': width,
            'height': height,
            'depth': depth,
            'packaging': packaging,
            'type': type,
            'assured': assured,
            'fragile': fragile,
            'start_dest': start_dest,
            'end_dest': end_dest,
        }

        req = requests.post("http://127.0.0.1:8886/api/v1/entities/parcels/add", parcel_dict)
        if req.status_code == 200:
            flash('Deposition successful !', 'success')
            return redirect('/')
        else:
            flash("An error occurred !, please retry again...", 'error')
            return redirect('/')


@app.route('/parcel/<string:parcel_ref>')
def by_parcel_ref(parcel_ref):
    parcel = requests.get('http://127.0.0.1:8886/api/v1/entities/parcels/get/' + parcel_ref).json()
    tracking = requests.get('http://127.0.0.1:8886/api/v1/entities/parcels/tracking/' + parcel_ref).json()
    for track in tracking:
        print(track)
    return render_template('parcel.html', parcel=parcel, tracking=tracking)


@app.route('/parcel/validation/<string:parcel_ref>')
def validation_parcel(parcel_ref):
    parcel = requests.get('http://127.0.0.1:8886/api/v1/entities/parcels/validation/' + parcel_ref)
    if parcel.status_code == 200:
        flash('Validation successful !', 'success')
        return redirect('/parcel/'+parcel_ref)


@app.route('/parcel/delete/<string:parcel_ref>')
def delete_parcel(parcel_ref):
    parcel = requests.get('http://127.0.0.1:8886/api/v1/entities/parcels/delete/' + parcel_ref)
    if parcel.status_code == 200:
        flash('Deletation successful !', 'success')
        return redirect('/my-parcels')
