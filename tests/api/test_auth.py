import pytest
import json
from pytest_bdd import scenarios, given, when, then
from utils.api_client import APIClient
from utils.logger import logger

# Carrega os cenários do arquivo .feature
scenarios("../../features/api_auth.feature")

@given("que eu tenho um usuário criado")
def create_user():
    """Cria um usuário único antes da autenticação"""
    logger.info("🟢 [INÍCIO] Criando Usuário para Autenticação")

    response = APIClient.create_user(pytest.user_data["userName"], pytest.user_data["password"])
    if response.status_code == 201:
        pytest.user_id = response.json()["userID"]
        logger.info(f"✅ Usuário criado com sucesso! ID: {pytest.user_id}")
    else:
        logger.warning("⚠️ Usuário já existia na API, reutilizando credenciais.")

@when("envio uma requisição para autenticar o usuário")
def send_auth_request():
    """Envia uma requisição para autenticar o usuário"""
    logger.info("🔑 Solicitando autenticação...")

    response = APIClient.generate_token(pytest.user_data["userName"], pytest.user_data["password"])
    pytest.response = response
    logger.info(f"📤 Resposta recebida da API ({response.status_code}):\n{json.dumps(response.json(), indent=4)}")

@then("a API deve retornar um token de autenticação")
def verify_auth_token():
    """Verifica se a autenticação foi bem-sucedida e o token foi gerado"""
    logger.info("🔍 Validando resposta da API para autenticação...")

    assert pytest.response.status_code == 200, f"❌ Erro na autenticação: {json.dumps(pytest.response.json(), indent=4)}"

    response_json = pytest.response.json()
    assert "token" in response_json and response_json["token"], "❌ Erro: Token não encontrado ou é inválido!"

    pytest.token = response_json["token"]
    logger.info(f"✅ Token de autenticação gerado com sucesso: {pytest.token[:20]}..." if pytest.token else "❌ Erro: Token retornou None!")