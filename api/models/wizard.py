from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Wizard(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
