from flask import Flask
from flasgger import Swagger

from .const import DATABASE_URI, TRACK_MODIFICATIONS
from .db import db_instance

from app.routes import init_routes


def create_app():
    # Init de l'app Flask
    app = Flask(__name__)

    # Configuration de l'app

    # db SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = TRACK_MODIFICATIONS


    # Init de SQLAlchemy
    db_instance.init_app(app)

    # Init des routes
    init_routes(app)

    with app.app_context():
        init_DB()

    # Init du Swagger
    Swagger(app)  

    # autre

    return app

def init_DB():
    from app.models import Person

    # Créer les tables
    db_instance.create_all()
    
    # Ajout de données de base si la table est vide
    if not Person.query.first():
        db_instance.session.add_all([
            Person(name="Jose"),
            Person(name="Henry")
        ])
    
    db_instance.session.commit()