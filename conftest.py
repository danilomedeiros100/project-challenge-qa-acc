import pytest
import logging
from utils.api_client import APIClient
from utils.data_generator import generate_username, get_default_password

import pytest
import logging
from utils.api_client import APIClient
from utils.data_generator import generate_username, get_default_password

@pytest.fixture(scope="function", autouse=True)
def setup_user():
    """Cria um novo usuário para cada teste e gera um novo token"""
    user_data = {
        "userName": generate_username(),
        "password": get_default_password()
    }
    logging.debug(f"👤 Criando novo usuário para o teste: {user_data['userName']}")

    response = APIClient.create_user(user_data["userName"], user_data["password"])
    assert response.status_code == 201, f"Erro ao criar usuário: {response.text}"

    response_json = response.json()
    pytest.user_id = response_json["userID"]
    pytest.user_data = user_data

    # Gerar token para o usuário recém-criado
    token_response = APIClient.generate_token(pytest.user_data["userName"], pytest.user_data["password"])
    assert token_response.status_code == 200, f"Erro ao gerar token: {token_response.text}"
    pytest.token = token_response.json().get("token")

    # 🚀 **Verifica se o token pode ser usado para autenticação**
    auth_response = APIClient.is_user_authorized(pytest.user_data["userName"], pytest.user_data["password"])
    assert auth_response.status_code == 200, f"Erro ao validar usuário após gerar token: {auth_response.text}"

    logging.debug(f"✅ Usuário criado e autorizado com sucesso. ID: {pytest.user_id}, Token: {pytest.token}")

    return pytest.user_id, pytest.token