import pytest
from app import create_test_app
from app.db import db_instance

from app.services.person import create_person

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
        
__all__ = ['app', 'client', 'db_session', 'sample_person', 'sample_persons']