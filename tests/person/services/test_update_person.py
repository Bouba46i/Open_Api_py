
import pytest
from app.models.person import Person
from tests.person.fixtures import *
from app.services.person import update_person

def test_update_person(sample_person):
    """Test pour mettre à jour une personne."""
    sample_person.name = "Charles"
    updated_person = update_person(sample_person.id, sample_person)

    # Vérifie les résultats
    assert updated_person is not None
    assert updated_person.id == sample_person.id
    assert updated_person.name == "Charles"

def test_update_person_without_person(sample_person):
    """Test de la levée d'erreur quand mise a jour d'une personne sans nom."""
    with pytest.raises(TypeError) as err_info:
        update_person(1)
    
    assert str(err_info.value) == "update_person() missing 1 required positional argument: 'person'"

@pytest.mark.parametrize("invalid_name", ["", "   ", None])
def test_update_person_with_invalid_name(sample_person, invalid_name):
    """Test de la levée d'erreur quand mise a jour d'une personne avec nom vide."""
    
    with pytest.raises(ValueError) as err_info:
        sample_person.name = invalid_name
        update_person(1, sample_person)
    
    assert str(err_info.value) == "Name cannot be an empty string"

def test_update_nonexistant_person(sample_person):
    """Test de la levée d'erreur quand mise a jour d'une personne avec nom vide."""
    with pytest.raises(ValueError) as err_info:
        inexistent_person = Person(id = 2, name = "James")
        update_person(2, inexistent_person)
    
    assert str(err_info.value) == "This person does not exist"