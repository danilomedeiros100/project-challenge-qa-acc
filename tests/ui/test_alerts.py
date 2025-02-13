import time
from pytest_bdd import scenario, given, when, then
from pages.alerts_page import AlertsPage

@scenario("../../features/ui_alerts.feature", "Validar exibição de alerta")
def test_validar_alerta():
    """Cenário: Validar que um alerta é exibido corretamente ao clicar no botão"""

@given('que estou na página "Alerts"')
def abrir_pagina_alerts(browser):
    """Abre a página de Alerts"""
    page = AlertsPage(browser)
    page.open()

@when('clico no botão "Click me"')
def clicar_botao_alerta(browser):
    """Clica no botão que aciona o alerta"""
    page = AlertsPage(browser)
    page.click_alert_button()

@then('um alerta deve ser exibido com a mensagem "You clicked a button"')
def validar_alerta_exibido(browser):
    """Verifica se o alerta foi exibido corretamente"""
    page = AlertsPage(browser)
    time.sleep(3)
    assert page.is_alert_present(), "O alerta não foi exibido corretamente."