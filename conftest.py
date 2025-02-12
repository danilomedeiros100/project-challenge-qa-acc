import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="function", autouse=True)
def cleanup_user():
    """Deleta o usuário após o teste"""
    yield  # Executa o teste primeiro

    # ✅ Verifica se user_id e token existem antes de deletar
    if hasattr(pytest, "user_id") and hasattr(pytest, "token"):
        APIClient.delete_user(pytest.user_id, pytest.token)