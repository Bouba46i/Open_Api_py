from flask import jsonify
from app.services.person import retrieve_every_persons

def get_persons():
    """
    Obtenir la liste des personnes
    ---
    responses:
      200:
        description: Liste des personnes
      400:
        description: Erreur lors de la récupération des personnes
    """
    try:
        persons_list = retrieve_every_persons()
        return jsonify([person.to_dict() for person in persons_list])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
