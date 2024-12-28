import pytest
from app import create_app
from app.models import add_document, get_all_documents

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        yield client

def test_create_survey(client):
    # Test de création de sondage
    pass

def test_get_surveys(client):
    # Test de récupération de sondages
    pass

def test_update_survey(client):
    # Test de mise à jour d'un sondage
    pass

def test_delete_survey(client):
    # Test de suppression d'un sondage
    pass