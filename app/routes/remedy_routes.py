from flask import Blueprint, request, jsonify
from app.models import Remedy
from app import db

remedy_bp = Blueprint('remedy', __name__)

@remedy_bp.route('/remedies', methods=['GET'])
def get_remedies():
    remedies = Remedy.query.all()
    return jsonify([remedy.serialize() for remedy in remedies])

@remedy_bp.route('/remedies/<int:id>', methods=['GET'])
def get_remedy(id):
    remedy = Remedy.query.get(id)
    return jsonify(remedy.serialize())

@remedy_bp.route('/remedies', methods=['POST'])
def create_remedy():
    data = request.get_json()
    remedy = Remedy(name=data['name'], description=data['description'], ingredients=data['ingredients'], symptoms=data['symptoms'])
    db.session.add(remedy)
    db.session.commit()
    return jsonify({'message': 'Remedy added successfully.'}), 201
