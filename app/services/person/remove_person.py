from app.repositories import PersonRepository

def remove_person(id : int):
    if not PersonRepository.person_exists(id): raise ValueError("This person does not exist")

    person_to_delete = PersonRepository.delete_person(id)

    return person_to_delete