import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="function", autouse=True)
def cleanup_user():
    """Deleta o usuário após o teste"""
    yield  # Executa o teste primeiro
    if hasattr(pytest, "user_id"):
        APIClient.delete_user(pytest.user_id, pytest.token)