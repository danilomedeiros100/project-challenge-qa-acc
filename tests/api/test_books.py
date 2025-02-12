import pytest
import json
from pytest_bdd import scenarios, given, when, then
from utils.api_client import APIClient
from utils.logger import logger

# Carrega os cenários do arquivo .feature
scenarios("../../features/api_books.feature")

@given("que estou autenticado na API")
def ensure_authentication():
    """Garante que o usuário está autenticado antes de buscar livros"""
    logger.info("🔑 Autenticando usuário para consulta de livros...")

    auth_response = APIClient.is_user_authorized(pytest.user_data["userName"], pytest.user_data["password"])
    assert auth_response.status_code == 200, f"❌ Erro: Usuário não está autorizado! {auth_response.text}"
    logger.info("✅ Usuário autenticado com sucesso!")

@given("que a API possui livros cadastrados")
def check_books_exist():
    """Verifica se existem livros disponíveis na API"""
    logger.info("📚 Verificando se há livros disponíveis na API...")

    response = APIClient.list_books()
    assert response.status_code == 200, f"❌ Erro ao buscar livros: {json.dumps(response.json(), indent=4)}"

    books = response.json().get("books", [])
    assert len(books) > 0, "❌ Erro: Nenhum livro disponível na API"
    pytest.books_data = books
    logger.info("✅ Livros disponíveis para consulta!")

@when("envio uma requisição para listar os livros")
def request_books():
    """Envia uma requisição para obter a lista de livros"""
    logger.info("📖 Solicitando lista de livros disponíveis...")

    response = APIClient.list_books()
    pytest.response = response

    logger.info(f"📤 Resposta recebida da API ({response.status_code}):\n{json.dumps(response.json(), indent=4)}")

@then("a API deve retornar a lista de livros disponíveis")
def verify_books_list():
    """Verifica se a API retornou a lista de livros corretamente"""
    logger.info("🔍 Validando resposta da API para a lista de livros...")

    assert pytest.response.status_code == 200, f"❌ Erro ao recuperar livros: {json.dumps(pytest.response.json(), indent=4)}"

    books = pytest.response.json().get("books", [])
    assert len(books) > 0, "❌ Erro: Lista de livros retornada está vazia"

    logger.info(f"📚 Total de livros recebidos: {len(books)}")
    logger.info("✅ Lista de livros retornada com sucesso!")