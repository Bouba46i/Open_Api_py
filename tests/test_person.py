import pytest
from app import create_test_app
from app.db import db_instance

from app.models.person import Person
from app.services.person import *

# Fixtures
@pytest.fixture
def app():
    """Fixture pour créer l'application Flask avec une DB temporaire."""
    app = create_test_app()
    
    with app.app_context():
        yield app
        db_instance.drop_all()

@pytest.fixture
def client(app):
    """Client Flask pour tester les endpoints si nécessaire."""
    return app.test_client()

@pytest.fixture
def db_session(app):
    """Session DB pour manipuler les données durant les tests."""
    with app.app_context():
        yield db_instance.session

@pytest.fixture
def sample_person(db_session):
    """Fixture pour fournir une personne."""
    return create_person(name="John Doe")

@pytest.fixture
def sample_persons(db_session):
    """Fixture pour fournir une liste complète de 9 personnes."""
    for i in range(1, 10):
        create_person(name=f"Person {i}")

# Routes Tests
# def test_retrieve_every_persons(client):
# 	response = client.get('/persons')

# 	assert response.status_code == 200
# 	assert response.json == []

# Services Tests
def test_create_person(db_session):
    """Test de la création d'une personne."""
    # Appelle le service
    person = create_person(name="Alice")
    
    # Vérifie les résultats
    assert person.id is not None
    assert person.name == "Alice"

def test_retrieve_person_by_id(sample_person):
    """Test pour récupérer une personne par son ID."""
    # Appelle le service
    retrieved_person = retrieve_person_by_id(sample_person.id)

    # Vérifie les résultats
    assert retrieved_person is not None
    assert retrieved_person.id == sample_person.id
    assert retrieved_person.name == sample_person.name

def test_update_person(sample_person):
    """Test pour mettre à jour une personne."""
    # Appelle le service pour mettre à jour la personne
    sample_person.name = "Charles"
    updated_person = update_person(sample_person.id, sample_person)

    # Vérifie les résultats
    assert updated_person is not None
    assert updated_person.id == sample_person.id
    assert updated_person.name == "Charles"

def test_remove_person(db_session, sample_person):
    """Test pour supprimer une personne."""
    # Appelle le service pour supprimer la personne
    remove_person(sample_person.id)

    # Vérifie que la personne a été supprimée
    deleted_person = db_session.get(Person, sample_person.id)
    assert deleted_person is None

def test_retrieve_all_persons(sample_persons):
    """Test pour récupérer toutes les personnes."""

    # Appelle le service pour récupérer toutes les personnes
    persons = retrieve_every_persons()

    # Vérifie les résultats
    assert len(persons) == 9
    for i, person in enumerate(persons):
        assert person is not None
        assert person.name == f"Person {i + 1}"
