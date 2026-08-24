import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Testa se a rota principal responde HTTP 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_content(client):
    """Testa se a mensagem de retorno está correta"""
    response = client.get('/')
    data = response.get_json()
    assert data['status'] == "sucesso"

def test_health_check(client):
    """Testa o endpoint de verificação de saúde da aplicação"""
    response = client.get('/health')
    assert response.status_code == 200