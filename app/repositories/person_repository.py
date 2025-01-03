from sqlalchemy import exists
from app.models import Person
from app.db import db_instance

class PersonRepository:
	def __init__(self):
		pass

	def get_all_persons() -> list[Person]:
		return Person.query.all()

	def get_person_by_id(id: int) -> Person:
		return Person.query.get(id)

	def get_number_of_persons() -> int:
		return Person.query.count()

	def save_person(person: Person) -> Person:
		db_instance.session.add(person)
		db_instance.session.commit()

		return person

	def update_person(id: int, person: Person) -> Person:
		person_to_update = Person.query.get(id)

		# TODO : trouver un moyen de rendre ca dynamique
		person_to_update.name = person["name"]
		db_instance.session.commit()

		return person_to_update

	def delete_person(id: int) -> Person:
		person_to_delete = Person.query.get(id)

		db_instance.session.delete(person_to_delete)
		db_instance.session.commit()

		return person_to_delete

	def person_exists(id: int) -> bool:
		return db_instance.session.query(exists().where(Person.id == id)).scalar()