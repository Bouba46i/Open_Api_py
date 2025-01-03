from flask import jsonify
from app.services.person import remove_person

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
    try:
        person = remove_person(person_id)
        return jsonify({"message": f"personne {person.name} supprimée"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400 # distinguish with 404