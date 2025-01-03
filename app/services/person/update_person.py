from app.models.person import Person
from app.repositories import PersonRepository

def update_person(id, person: Person):
    if not PersonRepository.person_exists(id): raise ValueError("This person does not exist")
    
    person_to_update = PersonRepository.update_person(id, person)

    return person_to_update