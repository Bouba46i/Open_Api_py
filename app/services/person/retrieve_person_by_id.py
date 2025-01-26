from app.repositories import PersonRepository

def retrieve_person_by_id(id : int):
    if not PersonRepository.person_exists(id): raise ValueError("This person does not exist")

    person = PersonRepository.get_person_by_id(id)

    return person