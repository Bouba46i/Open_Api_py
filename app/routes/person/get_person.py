from flask import jsonify
from app.services.person import retrieve_person_by_id

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
    try:
        person = retrieve_person_by_id(person_id)
        return jsonify(person.to_dict())
    except ValueError as e:
        # TODO : distinguish between 404 and 400 errors
        return jsonify({"error": str(e)}), 400
        # return jsonify({"error": str(e)}), 404