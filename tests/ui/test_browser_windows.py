import pytest
from pytest_bdd import scenarios, given, when, then
from pages.browser_windows_page import BrowserWindowsPage
from pytest_bdd import given, when, then
from utils.data_generator import generate_valid_test_data

scenarios("../../features/ui_browser_windows.feature")

@pytest.fixture
def form_page(browser):
    """Inicializa a página do formulário"""
    return BrowserWindowsPage(browser)

@pytest.fixture
def test_data():
    """Gera massa de dados parametrizável"""
    return generate_valid_test_data()


@given('que estou na página "Browser Windows"')
def abrir_pagina_browser_windows(browser):
    """Abre a página de Browser Windows"""
    page = BrowserWindowsPage(browser)
    page.open()


@when('clico no botão "New Window"')
def clicar_botao_nova_janela(browser):
    """Clica no botão para abrir uma nova janela"""
    page = BrowserWindowsPage(browser)
    page.click_new_window_button()


@then('uma nova janela deve ser aberta com a mensagem "This is a sample page"')
def validar_mensagem_nova_janela(browser):
    """Valida que uma nova janela foi aberta com a mensagem correta"""
    page = BrowserWindowsPage(browser)
    assert page.is_new_window_opened(), "A nova janela não foi aberta corretamente."