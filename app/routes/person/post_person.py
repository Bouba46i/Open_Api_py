from flask import jsonify, request
from app.services.person import create_person

def post_person():
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
      403:
        description: nombre maximal de personnes créées atteint
    """
    try:
        data = request.get_json()
        person = create_person(data["name"])
        return jsonify(person.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400 # distinguish with 403