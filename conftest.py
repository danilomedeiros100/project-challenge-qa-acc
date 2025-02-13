from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage
import pytest
import logging
from pages.progress_bar_page import ProgressBarPage
from pages.web_tables_page import WebTablesPage
from utils.api_client import APIClient
from utils.data_generator import generate_username, get_default_password

@pytest.fixture(scope="session", autouse=True)
def setup_user():
    """Cria um novo usuário e gera um token, reutilizando-o nos testes."""
    user_data = {
        "userName": generate_username(),
        "password": get_default_password()
    }
    logging.debug(f"👤 Criando novo usuário para o teste: {user_data['userName']}")

    response = APIClient.create_user(user_data["userName"], user_data["password"])

    if response.status_code not in [201, 406]:  # 406 = "User exists"
        pytest.fail(f"Erro ao criar usuário: {response.text}")

    pytest.user_data = user_data

    # Gerar token
    token_response = APIClient.generate_token(user_data["userName"], user_data["password"])
    if token_response.status_code != 200:
        pytest.fail(f"Erro ao gerar token: {token_response.text}")

    pytest.token = token_response.json().get("token")

    # Validar autenticação
    auth_response = APIClient.is_user_authorized(user_data["userName"], user_data["password"])
    if auth_response.status_code != 200:
        pytest.fail(f"Erro ao validar usuário após gerar token: {auth_response.text}")

    logging.debug(f"✅ Usuário criado e autorizado com sucesso. Token: {pytest.token}")
    return pytest.user_data, pytest.token

@pytest.fixture
def authenticated_user():
    """Retorna os dados do usuário autenticado"""
    if not hasattr(pytest, "user_data"):
        pytest.fail("❌ `pytest.user_data` não foi inicializado corretamente!")
    return pytest.user_data

@pytest.fixture
def web_tables_page(browser):
    """Retorna uma instância da página Web Tables"""
    page = WebTablesPage(browser)
    page.open()
    return page

@pytest.fixture
def browser():
    """Configura o WebDriver do Chrome"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

@pytest.fixture
def form_page(browser):
    """Retorna uma instância da página do formulário"""
    page = FormPage(browser)
    return page

@pytest.fixture
def progress_bar_page(browser):
    """Inicializa a página Progress Bar"""
    return ProgressBarPage(browser)

import pytest
from pages.sortable_page import SortablePage

@pytest.fixture
def sortable_page(browser):
    """Inicializa a página Sortable."""
    return SortablePage(browser)