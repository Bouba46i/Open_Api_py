from app.models.person import Person
from app.repositories import PersonRepository

def update_person(id: int, person: Person):
    if not PersonRepository.person_exists(id): raise ValueError("This person does not exist")
    # TODO : trouver pq ca ne se stop pas au 'None' 
    if not person.name or not person.name.strip() or person.name == None: raise ValueError("Name cannot be an empty string")

    person_to_update = PersonRepository.update_person(id, person)

    return person_to_update