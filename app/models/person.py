from app import db_instance

class Person(db_instance.Model):
	__tablename__ = "persons"

	id = db_instance.Column(db_instance.Integer, primary_key=True, autoincrement=True)
	name = db_instance.Column(db_instance.String(255), nullable=False)

	def to_dict(self):
		"""Convert the object to a dictionary"""
		return {"id": self.id, "name": self.name}