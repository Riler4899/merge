from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField, RadioField, TextAreaField

class ClientForm(FlaskForm):
    name = StringField('Name')
    company = StringField('Company')
    address = StringField('Address')
    contact_no = StringField('Contact Number')
    email = StringField('Email Address')
    client_type = RadioField('Client Type', choices=[('DMME', 'DMME'), ('Student', 'Student'), ('Regular Client', 'Regular Client')])
    submit = SubmitField('Submit')

class RequestForm(FlaskForm):
    ref_no = IntegerField('RF#')
    details = TextAreaField('Inquiry/Request Details')
    endorse_for = RadioField('Endorse for', choices=[('Consultancy', 'Consultancy'), ('Training', 'Training'), ('','Others')])
    others = StringField('')
    bill_details = TextAreaField('Bill Details')
    mode_of_payment = RadioField('Mode of Payment', choices=[('Cash', 'Cash'), ('Check', 'Check'), ('Government Terms', 'Government Terms')])
    processed_by = StringField('Inquiry Processed By')
    endorsed_to = StringField('Inquiry Endorsed To')