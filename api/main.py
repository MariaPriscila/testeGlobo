import sys
from flask import Flask
from models import db
from dotenv import load_dotenv
import os
from controllers.wizard_controller import wizard_bp
from controllers.elixir_controller import elixir_bp
from controllers.ingredient_controller import ingredient_bp

env = os.getenv('API_ENV_FILE', sys.path[0]+"/.env")
load_dotenv(env)
DATABASE_URL = os.getenv('DATABASE_URL')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(wizard_bp)
app.register_blueprint(elixir_bp)
app.register_blueprint(ingredient_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)