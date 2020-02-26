import requests
from flask import render_template, url_for, redirect, request, flash
from webapp.forms import ClientForm, RequestForm
from webapp import app

@app.route('/clients/add', methods=['GET', 'POST'])
def add_client():
    form = ClientForm()

    if form.validate_on_submit():
        payload = {'name': form.name.data, 'company': form.company.data, 'address': form.address.data, 'contact_no': form.contact_no.data, 'email': form.email.data, 'client_type': form.client_type.data}
        r = requests.post('http://localhost:8000/clients/add', json=payload)

        if r.ok:
            flash('A new client has been added!')
        else:
            flash('Error, client was not added.')

        return redirect(url_for('add_client'))

    return render_template('add_client.html', form=form)

@app.route('/clients', methods=['GET'])
def get_clients():
    r = requests.get('http://localhost:8000/clients')

    return render_template('clients.html', clients=r.json())