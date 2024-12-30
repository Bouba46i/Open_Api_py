from flask import Flask, jsonify, request
from flasgger import Swagger

from utils import update_objet

app = Flask(__name__)
Swagger(app)  # Init du Swagger

MAX_FAKE_PERSONS = 10

# Données simulées
fake_persons = [
    {"id": 1, "name": "Jose"},
    {"id": 2, "name": "Henry"},
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the CRUD API with Flask - Go to /apidocs to see the documentation or /persons to see the persons list"})


@app.route("/persons", methods=["GET"])
def get_persons():
    """
    Obtenir la liste des personnes
    ---
    responses:
      200:
        description: Liste des personnes
    """
    return jsonify(fake_persons)


@app.route("/persons/<int:person_id>", methods=["GET"])
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
    person = next((person for person in fake_persons if person["id"] == person_id), None)
    if person:
        return jsonify(person)
    return jsonify({"error": "personne non trouvé"}), 404


@app.route("/persons", methods=["POST"])
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
    if len(fake_persons) >= MAX_FAKE_PERSONS:
         return jsonify({"error": "nombre maximal de personnes atteint"}), 405

    data = request.get_json()
    new_id = max(person["id"] for person in fake_persons) + 1 if fake_persons else 1
    new_person = {"id": new_id, "name": data["name"]}
    fake_persons.append(new_person)
    return jsonify(new_person), 201


@app.route("/persons/<int:person_id>", methods=["PUT"])
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
    global fake_persons
    
    person_to_update = next((person for person in fake_persons if person["id"] == person_id), None)
    if person_to_update == None:
         return jsonify({"error": "cette personne n'existe pas"}), 404
    
    old_data = person_to_update.copy()
    data = request.get_json()
    data_to_update = {"name": data["name"]}
    
    update_objet(fake_persons, person_id, data_to_update)
    
    return jsonify({"message": f"{old_data["name"]} renommée en {person_to_update["name"]}"}), 200

@app.route("/persons/<int:person_id>", methods=["DELETE"])
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
    global fake_persons
    
    person_to_delete = next((person for person in fake_persons if person["id"] == person_id), None)
    if person_to_delete == None:
         return jsonify({"error": "cette personne n'existe pas"}), 404
    
    fake_persons = [person for person in fake_persons if person["id"] != person_to_delete["id"]]
    return jsonify({"message": f"personne {person_to_delete["name"]} supprimée"}), 200


if __name__ == "__main__":
    app.run(debug=True)