from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Elixir(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String())
    effect = db.Column(db.String())
    side_effects = db.Column(db.String())
    characteristics = db.Column(db.String())
    time = db.Column(db.String())
    difficulty = db.Column(db.String())
    ingredients = db.Column(db.ARRAY(db.String()))
    inventors = db.Column(db.ARRAY(db.String()))
    manufacturer = db.Column(db.String())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'effect': self.effect,
            'side_effects': self.side_effects,
            'characteristics': self.characteristics,
            'time': self.time,
            'difficulty': self.difficulty,
            'ingredients': self.ingredients,
            'inventors': self.inventors,
            'manufacturer': self.manufacturer
        }
