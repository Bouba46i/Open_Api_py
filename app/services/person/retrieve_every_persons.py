from app.repositories import PersonRepository

def retrieve_every_persons():
    persons = PersonRepository.get_all_persons()

    return persons