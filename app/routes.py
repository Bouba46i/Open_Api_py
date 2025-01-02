
import copy
from flask import jsonify, request, Blueprint
from app import db_instance

from app.models.person import Person
from app.const import MAX_PERSONS

# blueprint pour organiser les routes
api_bp = Blueprint('api', __name__)

@api_bp.route("/")
def home():
    return jsonify({"message": "Welcome to the CRUD API with Flask - Go to /apidocs to see the documentation or /persons to see the persons list"})


@api_bp.route("/persons", methods=["GET"])
def get_persons():
    """
    Obtenir la liste des personnes
    ---
    responses:
      200:
        description: Liste des personnes
    """
    persons = Person.query.all()
    return jsonify([person.to_dict() for person in persons])


@api_bp.route("/persons/<int:person_id>", methods=["GET"])
def get_person(person_id):
    """
    Obtenir une personne grace a son ID
    ---
    parameters:
      - name: person_id
        in: path
        type: integer
        required: true
        description: ID de la personne
    responses:
      200:
        description: personne trouvée
      404:
        description: personne non trouvée
    """
    person = Person.query.get(person_id)

    if not person: return jsonify({"error": "personne non trouvé"}), 404

    return jsonify(person.to_dict())


@api_bp.route("/persons", methods=["POST"])
def create_person():
    """
    Créer une nouvelle personne
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Jacques
              description: Nom de la nouvelle personne
    responses:
      201:
        description: personne créée
      405:
        description: nombre maximal de personnes créées atteint
    """
    if Person.query.count() >= MAX_PERSONS: return jsonify({"error": "nombre maximal de personnes atteint"}), 405

    data = request.get_json()
    new_person = Person(name=data["name"])

    db_instance.session.add(new_person)
    db_instance.session.commit()

    return jsonify(new_person.to_dict()), 201


@api_bp.route("/persons/<int:person_id>", methods=["PUT"])
def update_person(person_id):
    """
    Mettre a jour une personne grace a son ID
    ---
    parameters:
      - name: person_id
        in: path
        type: integer
        required: true
        description: ID de la personne
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Jacques
              description: Nouveau nom de la personne
    responses:
      200:
        description: personne trouvée
      404:
        description: personne non trouvée
    """
    person_to_update = Person.query.get(person_id)
    
    if not person_to_update : return jsonify({"error": "cette personne n'existe pas"}), 404
    
    old_data = copy.deepcopy(person_to_update)
    data = request.get_json()
    person_to_update.name = data["name"]
    db_instance.session.commit()
    
    return jsonify({"message": f"{old_data.name} renommée en {person_to_update.name}"}), 200

@api_bp.route("/persons/<int:person_id>", methods=["DELETE"])
def delete_person(person_id):
    """
    Supprimer une personne grace a son ID
    ---
    parameters:
      - name: person_id
        in: path
        type: integer
        required: true
        description: ID de la personne
    responses:
      200:
        description: personne supprimée
      404:
        description: personne non trouvée
    """
    person_to_delete = Person.query.get(person_id)
    
    if not person_to_delete : return jsonify({"error": "cette personne n'existe pas"}), 404
    
    db_instance.session.delete(person_to_delete)
    db_instance.session.commit()

    return jsonify({"message": f"personne {person_to_delete.name} supprimée"}), 200
