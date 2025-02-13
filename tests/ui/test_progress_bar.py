import time
from pytest_bdd import scenario, given, when, then


@scenario("../../features/ui_progress_bar.feature", "Controlar o progresso da barra de progresso")
def test_progress_bar():
    pass

@given('que estou na página "Progress Bar"')
def acessar_pagina_progress_bar(browser, progress_bar_page):
    """Acessa a página Progress Bar"""
    progress_bar_page.open()
    assert progress_bar_page.is_loaded(), "A página Progress Bar não foi carregada corretamente."

@when("inicio o progresso")
def iniciar_progresso(progress_bar_page):
    """Clica no botão Start para iniciar a barra de progresso"""
    progress_bar_page.click_start_button()

@when("paro o progresso antes de 25%")
def parar_antes_25(progress_bar_page):
    """Interrompe a barra de progresso antes de atingir 25%"""
    progress_bar_page.stop_progress_before(25)

@then("o valor da progress bar deve ser menor ou igual a 25%")
def validar_progresso_menor_que_25(progress_bar_page):
    """Verifica se o progresso está abaixo ou igual a 25%"""
    assert progress_bar_page.get_progress_value() <= 25, "O valor da progress bar ultrapassou 25%!"
    time.sleep(3)

@when("inicio novamente e aguardo 100%")
def iniciar_e_aguardar_100(progress_bar_page):
    """Inicia a barra de progresso novamente e aguarda atingir 100%"""
    progress_bar_page.click_start_button()
    progress_bar_page.wait_until_complete()
    time.sleep(3)

@when("reseto a progress bar")
def resetar_progress_bar(progress_bar_page):
    """Clica no botão Reset para voltar o progresso a 0%"""
    progress_bar_page.click_reset_button()
    time.sleep(3)

@then("o valor da progress bar deve ser 0%")
def validar_reset_progress_bar(progress_bar_page):
    """Verifica se a barra de progresso foi reiniciada"""
    assert progress_bar_page.get_progress_value() == 0, "A progress bar não foi resetada corretamente!"
    time.sleep(3)