import pytest
import random
from pytest_bdd import scenarios, given, when, then
from utils.api_client import APIClient
from utils.logger import logger

# Carrega os cenários do arquivo .feature
scenarios("../../features/api_create_user.feature")

@given("que eu tenho um nome de usuário e uma senha válidos")
def generate_user_data():
    """Gera credenciais válidas para o usuário"""
    logger.info("🟢 [INÍCIO] Gerando Usuário para Teste")

    pytest.user_data = {
        "userName": f"usuario_teste_{random.randint(1000, 9999)}",
        "password": "Teste@123"
    }
    logger.info(f"👤 Usuário Gerado: {pytest.user_data['userName']}")

@when("envio uma requisição para criar um usuário")
def create_user():
    """Cria um usuário na API"""
    logger.info("📩 Enviando requisição para criar usuário...")

    response = APIClient.create_user(pytest.user_data["userName"], pytest.user_data["password"])
    pytest.response = response
    logger.info(f"📤 Resposta recebida da API: {response.status_code} - {response.text}")

@then("a API deve retornar um status 201")
def verify_user_creation():
    """Verifica se o usuário foi criado com sucesso"""
    assert pytest.response.status_code == 201, f"❌ Erro ao criar usuário: {pytest.response.text}"
    logger.info("✅ Usuário criado com sucesso na API!")

@then("o usuário deve ser criado com sucesso")
def verify_user_details():
    """Verifica se o usuário está registrado corretamente"""
    logger.info("🔍 Verificando se o usuário foi registrado corretamente...")

    response_json = pytest.response.json()
    assert "userID" in response_json, "❌ Erro: ID do usuário não retornado pela API"
    pytest.user_id = response_json["userID"]

    # 🚀 **Agora garantimos que o token está correto antes de buscar detalhes**
    token_response = APIClient.generate_token(pytest.user_data["userName"], pytest.user_data["password"])
    assert token_response.status_code == 200, f"❌ Erro ao gerar token para validação do usuário: {token_response.text}"
    pytest.token = token_response.json().get("token")

    user_details = APIClient.get_user_details(pytest.user_id, pytest.token)
    assert user_details.status_code == 200, f"❌ Erro ao buscar usuário criado: {user_details.text}"
    logger.info("✅ Usuário registrado com sucesso na API!")