from flask import Blueprint, request, jsonify

from models import db, Contact, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'naw'}

@api.route('/')
def home():
    return "<h3>Congrats</h3>"

@api.route('/contacts', methods = ['POST'])
def create_contact():
    name = request.json['name']
    email = request.json['email']
    phone_number = request.json['phone_number']
    address = request.json['address']

    contact = Contact(name, email, phone_number, address )

    db.session.add(contact)
    db.session.commit()

    response = contact_schema.dump(contact)
    return jsonify(response)

@api.route('/contacts', methods = ['GET'])
def get_contact():
    contacts = Contact.query.all()
    response = contacts_schema.dump(contacts)
    return jsonify(response)

@api.route('/contacts/<id>', methods = ['GET'])
def get_contact_two(id):
    contact = Contact.query.get(id)
    response = contact_schema.dump(contact)
    return jsonify(response)

# UPDATE endpoint
@api.route('/contacts/<id>', methods = ['POST','PUT'])
def update_contact(id):
    contact = Contact.query.get(id) 
    contact.name = request.json['name']
    contact.email = request.json['email']
    contact.phone_number = request.json['phone_number']
    contact.address = request.json['address']

    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)


# DELETE contact ENDPOINT
@api.route('/contacts/<id>', methods = ['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)