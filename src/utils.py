
def update_objet(objets, objet_id, updated_data):
    """
    Modifie un objet dans une liste d'objets.

    :param objets: Liste d'objets (dictionnaires).
    :param objet_id: ID de l'objet à modifier.
    :param updated_data: Dictionnaire contenant les nouvelles valeurs.
    :return: Booléen indiquant si la modification a eu lieu.
    """
    for objet in objets:
        if objet["id"] == objet_id:
            objet.update(updated_data)
            return True
    return False