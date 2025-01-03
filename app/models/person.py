from app.db import db_instance

class Person(db_instance.Model):
	"""
    Modèle représentant une personne.

    Attributes:
        id (int): Identifiant unique.
        name (str): Nom de la personne.
    """
	__tablename__ = "persons"

	id: int = db_instance.Column(db_instance.Integer, primary_key=True, autoincrement=True)
	name: str = db_instance.Column(db_instance.String(255), nullable=False)

	def to_dict(self):
		"""Convert the object to a dictionary"""
		return {"id": self.id, "name": self.name}