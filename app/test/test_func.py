import pytest
from app import create_app
from app.models import add_document, get_all_documents

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        yield client

def test_create_survey(client):
    survey_data = {
        "creator_id": "123",
        "question": "Quel est votre animal préféré ?",
        "choices": ["Chien", "Chat", "Oiseau"],
        "start_date": "2024-01-01",
        "end_date": "2024-01-31",
        "algo": "simple_average"
    }
    response = client.post('/api/createSurveys', json=survey_data)
    assert response.status_code == 201
    assert 'id' in response.json


def test_get_surveys(client):
    response = client.get('/api/surveys')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_update_survey(client):
    survey_data = {
        "creator_id": "123",
        "question": "Quel est votre animal préféré ?",
        "choices": ["Chien", "Chat", "Oiseau"],
        "start_date": "2024-01-01",
        "end_date": "2024-01-31",
        "algo": "simple_average"
    }
    create_response = client.post('/api/createSurveys', json=survey_data)
    survey_id = create_response.json['id']

    updated_data = {
        "question": "Quel est votre film préféré ?",
        "choices": ["Action", "Comédie", "Drame"]
    }
    response = client.put(f'/api/surveys/{survey_id}', json=updated_data)
    assert response.status_code == 200
    assert response.json['question'] == updated_data['question']

def test_delete_survey(client):
    survey_data = {
        "creator_id": "123",
        "question": "Quel est votre animal préféré ?",
        "choices": ["Chien", "Chat", "Oiseau", "Renard"],
        "start_date": "2024-01-01",
        "end_date": "2024-01-31",
        "algo": "majority"
    }
    create_response = client.post('/api/createSurveys', json=survey_data)
    survey_id = create_response.json['id']
    response = client.delete(f'/api/surveys/{survey_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Survey deleted successfully'
