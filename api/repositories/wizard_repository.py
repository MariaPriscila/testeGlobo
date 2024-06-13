import uuid
from models.wizard import Wizard
from models import db

class WizardRepository:

    def get_all(self):
        return Wizard.query.all()

    def get_by_id(self, id:uuid):
        return Wizard.query.get(id)

    def add(self, wizard):
        db.session.add(wizard)
        db.session.commit()

    def update(self, wizard):
        db.session.commit()

    def delete(self, wizard):
        db.session.delete(wizard)
        db.session.commit()
