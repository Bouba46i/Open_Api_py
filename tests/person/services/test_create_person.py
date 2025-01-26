
import pytest
from tests.person.fixtures import *
from app.services.person import create_person, retrieve_person_by_id

def test_create_person(db_session):
    """Test de la création d'une personne."""
    person = create_person(name="Alice")
    person_created = retrieve_person_by_id(person.id)
    
    assert person_created.id is not None
    assert person_created.name == "Alice"

def test_create_person_without_name(db_session):
    """Test de la levée d'erreur quand création d'une personne sans nom."""
    with pytest.raises(TypeError) as err_info:
        create_person()
    
    assert str(err_info.value) == "create_person() missing 1 required positional argument: 'name'"

@pytest.mark.parametrize("invalid_name", ["", "   ", None])
def test_create_person_with_invalid_name(db_session, invalid_name):
    """Test de la levée d'erreur quand création d'une personne avec nom vide."""
    with pytest.raises(ValueError) as err_info:
        create_person(invalid_name)
    
    assert str(err_info.value) == "Name cannot be an empty string"