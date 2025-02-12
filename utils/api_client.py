import requests
from utils.config import BASE_URL

class APIClient:
    """Classe para gerenciar chamadas à API"""

    @staticmethod
    def create_user(username, password):
        """Cria um novo usuário"""
        payload = {"userName": username, "password": password}
        response = requests.post(f"{BASE_URL}/Account/v1/User", json=payload)
        return response

    @staticmethod
    def generate_token(username, password):
        """Gera um token de autenticação"""
        payload = {"userName": username, "password": password}
        response = requests.post(f"{BASE_URL}/Account/v1/GenerateToken", json=payload)
        return response

    @staticmethod
    def delete_user(user_id, token):
        """Deleta um usuário"""
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(f"{BASE_URL}/Account/v1/User/{user_id}", headers=headers)
        return response