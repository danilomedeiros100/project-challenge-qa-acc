import time
from pytest_bdd import scenario, given, when, then
from pages.browser_tabs_page import BrowserTabsPage


@scenario("../../features/ui_browser_tabs.feature", "Validar abertura de nova aba")
def test_validar_abertura_de_nova_aba():
    """Cenário: Validar que ao clicar no botão 'New Tab' uma nova aba é aberta corretamente"""

@given('que estou na página "Browser Windows"')
def abrir_pagina_browser_tabs(browser):
    """Abre a página de Browser Windows"""
    page = BrowserTabsPage(browser)
    page.open()

@when('clico no botão "New Tab"')
def clicar_botao_nova_aba(browser):
    """Clica no botão que abre uma nova aba"""
    page = BrowserTabsPage(browser)
    page.click_new_tab_button()
    time.sleep(3)

@then('uma nova aba deve ser aberta com a mensagem "This is a sample page"')
def validar_mensagem_nova_aba(browser):
    """Valida que uma nova aba foi aberta com a mensagem correta"""
    page = BrowserTabsPage(browser)
    assert page.is_new_tab_opened(), "A nova aba não foi aberta corretamente."