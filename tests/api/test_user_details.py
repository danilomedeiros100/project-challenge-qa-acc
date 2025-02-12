import pytest
import json
import random
from pytest_bdd import scenarios, given, when, then
from utils.api_client import APIClient
from utils.logger import logger

# Carrega os cenários do arquivo .feature
scenarios("../../features/api_user_details.feature")

@given("que eu tenho um usuário criado e autenticado")
def create_and_authenticate_user():
    """Cria um usuário e gera um token válido para ele"""
    logger.info("🟢 [INÍCIO] Criando e autenticando usuário para consulta de detalhes")

    # Gerar nome de usuário único para evitar conflitos
    pytest.user_data = {
        "userName": f"usuario_teste_{random.randint(1000, 9999)}",
        "password": "Teste@123"
    }

    # Criar usuário
    response = APIClient.create_user(pytest.user_data["userName"], pytest.user_data["password"])

    if response.status_code == 201:  # Usuário criado com sucesso
        pytest.user_id = response.json()["userID"]
        logger.info(f"✅ Usuário criado com sucesso! ID: {pytest.user_id}")

    elif response.status_code == 406 and response.json().get("code") == "1204":  # Usuário já existe
        logger.warning("⚠️ Usuário já existe! Tentando autenticar com as credenciais existentes...")
        auth_response = APIClient.generate_token(pytest.user_data["userName"], pytest.user_data["password"])
        assert auth_response.status_code == 200, f"❌ Erro ao autenticar usuário existente: {json.dumps(auth_response.json(), indent=4)}"

        pytest.token = auth_response.json().get("token")

        # Buscar userID do usuário existente
        user_details = APIClient.get_user_by_username(pytest.user_data["userName"], pytest.token)
        assert user_details.status_code == 200, f"❌ Erro ao recuperar usuário existente: {json.dumps(user_details.json(), indent=4)}"

        pytest.user_id = user_details.json().get("userId")
        logger.info(f"✅ Usuário encontrado e autenticado! ID: {pytest.user_id}")

    else:
        pytest.fail(f"❌ Erro inesperado ao criar usuário: {json.dumps(response.json(), indent=4)}")

    # Autenticar usuário e gerar token
    token_response = APIClient.generate_token(pytest.user_data["userName"], pytest.user_data["password"])
    assert token_response.status_code == 200, f"❌ Erro ao gerar token: {json.dumps(token_response.json(), indent=4)}"

    pytest.token = token_response.json().get("token")
    logger.info(f"🔑 Token gerado com sucesso: {pytest.token[:20]}...")

@when("eu envio uma requisição para obter os detalhes do usuário")
def request_user_details():
    """Faz uma requisição para obter os detalhes do usuário"""
    logger.info("🔍 Solicitando detalhes do usuário...")

    response = APIClient.get_user_details(pytest.user_id, pytest.token)
    pytest.response = response

    logger.info(f"📤 Resposta recebida da API ({response.status_code}):\n{json.dumps(response.json(), indent=4)}")

@then("a API deve retornar os detalhes corretos do usuário")
def verify_user_details():
    """Verifica se os detalhes do usuário estão corretos"""
    logger.info("✅ Validando resposta da API para detalhes do usuário...")

    assert pytest.response.status_code == 200, f"❌ Erro ao buscar detalhes do usuário: {json.dumps(pytest.response.json(), indent=4)}"

    response_json = pytest.response.json()
    assert response_json["userId"] == pytest.user_id, "❌ Erro: ID do usuário não corresponde ao esperado"
    assert response_json["username"] == pytest.user_data["userName"], "❌ Erro: Nome de usuário não corresponde ao esperado"

    logger.info("✅ Os detalhes do usuário estão corretos!")