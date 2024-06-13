import uuid
from flask import Blueprint, jsonify, request
from models.wizard import Wizard
from repositories.wizard_repository import WizardRepository

wizard_bp = Blueprint('wizard_bp', __name__, url_prefix='/wizards')
wizard_repository = WizardRepository()

@wizard_bp.route('/', methods=['GET'])
def get_wizards():
    wizards = wizard_repository.get_all()
    return jsonify([wizard.to_dict() for wizard in wizards])

@wizard_bp.route('/<uuid:id>', methods=['GET'])
def get_wizard(id:uuid):
    wizard = wizard_repository.get_by_id(id)
    if wizard:
        return jsonify(wizard.to_dict())
    return jsonify({'error': 'Wizard not found'}), 404

@wizard_bp.route('/', methods=['POST'])
def create_wizard():
    data = request.get_json()
    new_wizard = Wizard(first_name=data['first_name'], last_name=data['last_name'])
    wizard_repository.add(new_wizard)
    return jsonify(new_wizard.to_dict()), 201

@wizard_bp.route('/<uuid:id>', methods=['PUT'])
def update_wizard(id):
    data = request.get_json()
    wizard = wizard_repository.get_by_id(id)
    if wizard:
        wizard.first_name = data['first_name']
        wizard.last_name = data['last_name']
        wizard_repository.update(wizard)
        return jsonify(wizard.to_dict())
    return jsonify({'error': 'Wizard not found'}), 404

@wizard_bp.route('/<uuid:id>', methods=['DELETE'])
def delete_wizard(id):
    wizard = wizard_repository.get_by_id(id)
    if wizard:
        wizard_repository.delete(wizard)
        return jsonify({'message': 'Wizard deleted successfully'})
    return jsonify({'error': 'Wizard not found'}), 404
