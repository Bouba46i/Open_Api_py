from flask import Flask

from app.routes.root import root_bp
from app.routes.person import person_bp

def init_routes(app: Flask):
    # Ajouter chaque blueprints ici
    app.register_blueprint(root_bp, url_prefix='/')
    app.register_blueprint(person_bp, url_prefix='/persons')
