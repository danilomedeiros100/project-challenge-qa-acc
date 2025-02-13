import requests
from utils.logger import logger

BASE_URL = "https://demoqa.com"

class APIClient:
    """Classe para gerenciar chamadas à API"""

    @staticmethod
    def create_user(username, password):
        """Cria um usuário na API"""
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
    def is_user_authorized(username, password):
        """Verifica se o usuário está autorizado"""
        payload = {"userName": username, "password": password}
        response = requests.post(f"{BASE_URL}/Account/v1/Authorized", json=payload)
        return response

    @staticmethod
    def get_user_details(user_id, token):
        """Obtém detalhes do usuário autenticado"""
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}/Account/v1/User/{user_id}", headers=headers)
        logger.debug(f"📥 Resposta da API ao obter detalhes do usuário: {response.status_code} - {response.text}")
        return response

    @staticmethod
    def list_books():
        """Obtém a lista de livros disponíveis"""
        response = requests.get(f"{BASE_URL}/BookStore/v1/Books")
        return response

    @staticmethod
    def reserve_books(user_id, book_isbns, token):
        """Reserva livros para o usuário"""
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        payload = {
            "userId": user_id,  # 🔹 Garante que o ID do usuário está sendo enviado corretamente
            "collectionOfIsbns": [{"isbn": isbn} for isbn in book_isbns]
        }
        logger.debug(f"📤 Enviando requisição para reservar livros. Payload: {payload}")

        response = requests.post(f"{BASE_URL}/BookStore/v1/Books", json=payload, headers=headers)
        logger.debug(f"📥 Resposta recebida da API: {response.status_code} - {response.text}")
        return response