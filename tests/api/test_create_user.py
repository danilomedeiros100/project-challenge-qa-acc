import pytest
from pytest_bdd import scenarios, given, when, then
from utils.api_client import APIClient
from utils.data_generator import generate_username, get_default_password

# Carrega os cenários do arquivo .feature
scenarios("../../features/api_create_user.feature")

@pytest.fixture
def user_data():
    """Gera um usuário dinâmico"""
    return {
        "userName": generate_username(),
        "password": get_default_password()
    }

@given("que eu tenho um nome de usuário e uma senha válidos")
def setup_user(user_data):
    """Configura os dados do usuário"""
    return user_data

@when("envio uma requisição para criar um usuário")
def send_create_user_request(user_data):
    """Faz a requisição para criar o usuário"""
    response = APIClient.create_user(user_data["userName"], user_data["password"])
    pytest.response = response
    return response

@then("a API deve retornar um status 201")
def verify_status_code():
    """Verifica se o status code é 201 (Created)"""
    assert pytest.response.status_code == 201, f"Erro: {pytest.response.text}"

@then("o usuário deve ser criado com sucesso")
def verify_user_created():
    """Valida se o usuário foi criado corretamente"""
    response_json = pytest.response.json()
    assert "userID" in response_json, "Erro: userID não encontrado na resposta"
    pytest.user_id = response_json["userID"]