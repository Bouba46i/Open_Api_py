
import pytest
from tests.person.fixtures import *
from app.services.person import create_person, retrieve_person_by_id

def test_retrieve_person_by_id(sample_person):
    """Test pour récupérer une personne par son ID."""
    retrieved_person = retrieve_person_by_id(sample_person.id)

    assert retrieved_person is not None
    assert retrieved_person.id == sample_person.id
    assert retrieved_person.name == sample_person.name

def test_retrieve_person_by_empty_id():
    """Test pour récupérer une personne avec un ID vide."""
    with pytest.raises(TypeError) as err_info:
        retrieve_person_by_id()
    
    assert str(err_info.value) == "retrieve_person_by_id() missing 1 required positional argument: 'id'"

def test_retrieve_person_by_nonexistent_id(sample_person):
    """Test pour récupérer une personne avec un ID inexistant."""
    nonexistent_id = 2
    with pytest.raises(ValueError) as err_info:
        retrieve_person_by_id(nonexistent_id)

    assert str(err_info.value) == "This person does not exist"