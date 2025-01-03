from flask import jsonify, request
from app.services.person import update_person

def put_person(person_id):
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
    try:
        data = request.get_json()
        person = update_person(person_id, { "id": person_id, "name": data["name"] })
        return jsonify({"message": f"Personne {person_id} renommée en {person.name}"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400 # distinguish with 404