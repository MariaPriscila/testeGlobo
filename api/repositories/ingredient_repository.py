from models.ingredient import Ingredient
from models import db

class IngredientRepository:

    def get_all(self):
        return Ingredient.query.all()

    def get_by_id(self, id):
        return Ingredient.query.get(id)

    def add(self, ingredient):
        db.session.add(ingredient)
        db.session.commit()

    def update(self, ingredient):
        db.session.commit()

    def delete(self, ingredient):
        db.session.delete(ingredient)
        db.session.commit()
