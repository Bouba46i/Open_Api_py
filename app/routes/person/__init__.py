from flask import Blueprint

# blueprint pour les routes /persons afin de récup les personnes
person_bp = Blueprint('person', __name__)

from .get_persons import get_persons
from .get_person import get_person
from .post_person import post_person
from .put_person import put_person
from .delete_person import delete_person

# Ajout des routes au blueprint
person_bp.add_url_rule('', view_func=get_persons, methods=['GET'])
person_bp.add_url_rule('/<int:person_id>', view_func=get_person, methods=['GET'])
person_bp.add_url_rule('', view_func=post_person, methods=['POST'])
person_bp.add_url_rule('/<int:person_id>', view_func=put_person, methods=['PUT'])
person_bp.add_url_rule('/<int:person_id>', view_func=delete_person, methods=['DELETE'])
