from flask import Blueprint

root_bp = Blueprint('root', __name__)

from .get_home import get_home

root_bp.add_url_rule('', view_func=get_home, methods=['GET'])
