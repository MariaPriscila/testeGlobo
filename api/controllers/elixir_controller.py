from flask import Blueprint, jsonify, request
from models.elixir import Elixir
from repositories.elixir_repository import ElixirRepository

elixir_bp = Blueprint('elixir_bp', __name__, url_prefix='/elixirs')
elixir_repository = ElixirRepository()

@elixir_bp.route('/', methods=['GET'])
def get_elixirs():
    elixirs = elixir_repository.get_all()
    return jsonify([elixir.to_dict() for elixir in elixirs])

@elixir_bp.route('/<uuid:id>', methods=['GET'])
def get_elixir(id):
    elixir = elixir_repository.get_by_id(id)
    if elixir:
        return jsonify(elixir.to_dict())
    return jsonify({'error': 'Elixir not found'}), 404

@elixir_bp.route('/', methods=['POST'])
def create_elixir():
    data = request.get_json()
    new_elixir = Elixir(
        name=data['name'],
        effect=data['effect'],
        side_effects=data['side_effects'],
        characteristics=data['characteristics'],
        time=data['time'],
        difficulty=data['difficulty'],
        ingredients=data['ingredients'],
        inventors=data['inventors'],
        manufacturer=data['manufacturer']
    )
    elixir_repository.add(new_elixir)
    return jsonify(new_elixir.to_dict()), 201

@elixir_bp.route('/<uuid:id>', methods=['PUT'])
def update_elixir(id):
    data = request.get_json()
    elixir = elixir_repository.get_by_id(id)
    if elixir:
        elixir.name = data['name']
        elixir.effect = data['effect']
        elixir.side_effects = data['side_effects']
        elixir.characteristics = data['characteristics']
        elixir.time = data['time']
        elixir.difficulty = data['difficulty']
        elixir.ingredients = data['ingredients']
        elixir.inventors = data['inventors']
        elixir.manufacturer = data['manufacturer']
        elixir_repository.update(elixir)
        return jsonify(elixir.to_dict())
    return jsonify({'error': 'Elixir not found'}), 404

@elixir_bp.route('/<uuid:id>', methods=['DELETE'])
def delete_elixir(id):
    elixir = elixir_repository.get_by_id(id)
    if elixir:
        elixir_repository.delete(elixir)
        return jsonify({'message': 'Elixir deleted successfully'})
    return jsonify({'error': 'Elixir not found'}), 404
