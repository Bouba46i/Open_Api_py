from flask import Flask
from flask_cors import CORS

from app.routes.root import root_bp
from app.routes.person import person_bp

def init_routes(app: Flask):
    CORS(app)
    # Ajouter chaque blueprints ici
    app.register_blueprint(root_bp, url_prefix='/')
    app.register_blueprint(person_bp, url_prefix='/persons')
