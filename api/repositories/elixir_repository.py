from models.elixir import Elixir
from models import db

class ElixirRepository:

    def get_all(self):
        return Elixir.query.all()

    def get_by_id(self, id):
        return Elixir.query.get(id)

    def add(self, elixir):
        db.session.add(elixir)
        db.session.commit()

    def update(self, elixir):
        db.session.commit()

    def delete(self, elixir):
        db.session.delete(elixir)
        db.session.commit()
