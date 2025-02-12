import pytest
from pytest_bdd import scenarios, given, when, then
from utils.api_client import APIClient
from utils.data_generator import generate_username, get_default_password

# Carrega os cenários do arquivo .feature
scenarios("../../features/api_auth.feature")

@pytest.fixture
def user_data():
    """Gera um usuário dinâmico"""
    return {
        "userName": generate_username(),
        "password": get_default_password()
    }

@given("que eu tenho um usuário criado")
def create_user(user_data):
    """Cria um usuário antes de autenticar"""
    response = APIClient.create_user(user_data["userName"], user_data["password"])
    assert response.status_code == 201, f"Erro ao criar usuário: {response.text}"
    response_json = response.json()
    pytest.user_id = response_json["userID"]
    pytest.user_data = user_data  # ✅ Armazena os dados do usuário para uso posterior

@when("envio uma requisição para autenticar o usuário")
def send_auth_request():
    """Envia uma requisição para autenticar o usuário"""
    response = APIClient.generate_token(pytest.user_data["userName"], pytest.user_data["password"])
    pytest.response = response
    return response

@then("a API deve retornar um token de autenticação")
def verify_auth_token():
    """Verifica se a autenticação foi bem-sucedida e o token foi gerado"""
    assert pytest.response.status_code == 200, f"Erro na autenticação: {pytest.response.text}"
    response_json = pytest.response.json()
    assert "token" in response_json, "Erro: Token não encontrado na resposta"
    pytest.token = response_json["token"]  # ✅ Armazena o token para uso posterior