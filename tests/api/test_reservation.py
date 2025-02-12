import pytest
import json
from pytest_bdd import scenarios, given, when, then
from utils.api_client import APIClient
from utils.logger import logger

# Carrega os cenários do arquivo .feature
scenarios("../../features/api_reservation.feature")

@given("que estou autenticado na API")
def ensure_authentication():
    """Garante que o usuário está autenticado e autorizado"""
    logger.info("🟢 [INÍCIO] Teste de Autenticação do Usuário")
    logger.debug(f"🔑 Verificando usuário... ID: {pytest.user_id} | Token: {pytest.token[:20]}...")

    auth_response = APIClient.is_user_authorized(pytest.user_data["userName"], pytest.user_data["password"])
    assert auth_response.status_code == 200, f"❌ Erro: Usuário não está autorizado! {json.dumps(auth_response.json(), indent=4)}"
    logger.info("✅ Usuário autenticado com sucesso!")

    # 🚀 **Verifica se o usuário realmente existe antes da reserva**
    user_details = APIClient.get_user_details(pytest.user_id, pytest.token)

    # **Se a API retornar erro 401, tentamos gerar um novo token**
    if user_details.status_code == 401:
        logger.warning("🔄 Token pode estar inválido, gerando um novo...")
        new_token_response = APIClient.generate_token(pytest.user_data["userName"], pytest.user_data["password"])
        assert new_token_response.status_code == 200, f"❌ Erro ao gerar novo token: {json.dumps(new_token_response.json(), indent=4)}"

        pytest.token = new_token_response.json().get("token")
        logger.info(f"🔄 Novo Token Gerado: {pytest.token[:20]}...")

        # **Verifica os detalhes do usuário novamente com o novo token**
        user_details = APIClient.get_user_details(pytest.user_id, pytest.token)

    assert user_details.status_code == 200, f"❌ Erro: Usuário não encontrado antes da reserva! {json.dumps(user_details.json(), indent=4)}"
    logger.info("✅ Usuário validado com sucesso para reserva de livros!")

@given("tenho o ID de dois livros disponíveis")
def get_two_books():
    """Obtém os IDs de dois livros disponíveis na API"""
    logger.info("📚 Buscando livros disponíveis...")
    response = APIClient.list_books()
    assert response.status_code == 200, f"❌ Erro ao buscar livros: {json.dumps(response.json(), indent=4)}"

    books = response.json().get("books", [])
    assert len(books) >= 2, "❌ Erro: Menos de dois livros disponíveis na API"

    pytest.book_ids = [books[0]["isbn"], books[1]["isbn"]]
    logger.info(f"📖 Livros selecionados para reserva: {pytest.book_ids}")

@when("envio uma requisição para reservar os livros")
def reserve_books():
    """Reserva dois livros disponíveis"""
    logger.info("📝 Solicitando reserva dos livros...")
    response = APIClient.reserve_books(pytest.user_id, pytest.book_ids, pytest.token)
    pytest.response = response
    logger.info(f"📤 Resposta recebida da API ({response.status_code}):\n{json.dumps(response.json(), indent=4)}")

@then("a API deve confirmar a reserva dos livros")
def verify_books_reserved():
    """Verifica se a API confirmou a reserva"""
    assert pytest.response.status_code == 201, f"❌ Erro ao reservar livros: {json.dumps(pytest.response.json(), indent=4)}"
    logger.info("✅ Reserva confirmada com sucesso!")

@then("os livros devem estar no perfil do usuário")
def verify_books_in_profile():
    """Verifica se os livros reservados aparecem no perfil do usuário"""
    logger.info("🔍 Validando se os livros estão no perfil do usuário...")
    response = APIClient.get_user_details(pytest.user_id, pytest.token)
    assert response.status_code == 200, f"❌ Erro ao obter detalhes do usuário: {json.dumps(response.json(), indent=4)}"

    user_books = [book["isbn"] for book in response.json().get("books", [])]
    assert all(book_id in user_books for book_id in pytest.book_ids), "❌ Erro: Livros não encontrados no perfil do usuário"

    logger.info("✅ Livros reservados confirmados no perfil do usuário!")