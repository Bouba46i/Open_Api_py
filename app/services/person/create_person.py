from app.const import MAX_PERSONS
from app.models import Person
from app.repositories import PersonRepository

def create_person(name):
    if not name: raise ValueError("Name cannot be an empty string")
    if PersonRepository.get_number_of_persons() >= MAX_PERSONS: raise ValueError("Can no longer add more persons")

    person = Person(name=name)
    PersonRepository.save_person(person)
    
    return person