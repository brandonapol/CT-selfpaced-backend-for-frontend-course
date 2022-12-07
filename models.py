# imports 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow 
import secrets

# set variables for class instantiation
ma = Marshmallow()
db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(200))

    def __init__(self,name,email,phone_number,address, id = ''):
        self.id = self.set_id()
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address


    def __repr__(self):
        return f'The following contact has been added to the phonebook: {self.name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class ContactSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name','email','phone_number', 'address']

contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)