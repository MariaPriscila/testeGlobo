from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Ingredient(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
