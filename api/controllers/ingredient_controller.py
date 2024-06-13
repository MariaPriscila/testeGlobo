from flask import Blueprint, jsonify, request
from models.ingredient import Ingredient
from repositories.ingredient_repository import IngredientRepository

ingredient_bp = Blueprint('ingredient_bp', __name__, url_prefix='/ingredients')
ingredient_repository = IngredientRepository()

@ingredient_bp.route('/', methods=['GET'])
def get_ingredients():
    ingredients = ingredient_repository.get_all()
    return jsonify([ingredient.to_dict() for ingredient in ingredients])

@ingredient_bp.route('/<uuid:id>', methods=['GET'])
def get_ingredient(id):
    ingredient = ingredient_repository.get_by_id(id)
    if ingredient:
        return jsonify(ingredient.to_dict())
    return jsonify({'error': 'Ingredient not found'}), 404

@ingredient_bp.route('/', methods=['POST'])
def create_ingredient():
    data = request.get_json()
    new_ingredient = Ingredient(name=data['name'])
    ingredient_repository.add(new_ingredient)
    return jsonify(new_ingredient.to_dict()), 201

@ingredient_bp.route('/<uuid:id>', methods=['PUT'])
def update_ingredient(id):
    data = request.get_json()
    ingredient = ingredient_repository.get_by_id(id)
    if ingredient:
        ingredient.name = data['name']
        ingredient_repository.update(ingredient)
        return jsonify(ingredient.to_dict())
    return jsonify({'error': 'Ingredient not found'}), 404

@ingredient_bp.route('/<uuid:id>', methods=['DELETE'])
def delete_ingredient(id):
    ingredient = ingredient_repository.get_by_id(id)
    if ingredient:
        ingredient_repository.delete(ingredient)
        return jsonify({'message': 'Ingredient deleted successfully'})
    return jsonify({'error': 'Ingredient not found'}), 404
