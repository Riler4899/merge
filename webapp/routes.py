import requests
from flask import escape, render_template, url_for, redirect, request, flash
from webapp.forms import ClientForm, RequestForm
from webapp import app


titleDict = {
    "caseTitle" : "DMMME - Cases",
    "addCaseTitle" : "DMMME - Cases - Add Case",
    "clientsTitle": "DMMME - Clients",
    "accountsTitle" : "DMMME - Accounts",
    "scheduleTitle" : "DMMME - Schedule"
}

@app.route('/', methods=['GET', 'POST'])

def start():
    form = LoginForm()
    if form.validate_on_submit():
        #redirects to cases if valid log in submission
        return redirect('/cases')
    else:
        return render_template('log.html', form=form) 

#Our cases page
@app.route('/cases')
def cases():
    return render_template("cases.html",title = titleDict["caseTitle"])

@app.route('/clients')
def clients():
    return render_template("clients.html",title = titleDict["clientsTitle"])



@app.route('/schedule')
def schedule():
    return render_template("schedule.html",title = titleDict["scheduleTitle"])

@app.route('/accounts')
def accounts():
    return render_template("accounts.html", title = titleDict["accountsTitle"])
    
@app.route('/addcase')
def addcase():
    cform = ClientForm()
    rform = RequestForm()
    return render_template("addcase.html",title = titleDict["addCaseTitle"] ,cform = cform, rform = rform)


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