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
