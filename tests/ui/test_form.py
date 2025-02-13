import pytest
from pytest_bdd import scenario, given, when, then
from pages.form_page import FormPage
from utils.data_generator import (
    generate_valid_test_data,
    generate_weak_password_data,
    generate_mismatched_email_data,
    generate_incomplete_data
)

# 📌 Cenário 1: Submeter formulário com sucesso
import os
from pytest_bdd import scenario

feature_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../features/ui_form.feature"))

@scenario(feature_file, "Submeter formulário com sucesso")
def test_submeter_formulario_com_sucesso():
    pass

def test_submeter_formulario_com_sucesso():
    pass

@given("que estou na página do formulário")
def acessar_pagina_formulario(form_page):
    """Garante que a página do formulário está carregada"""
    form_page.open()
    assert form_page.is_page_loaded(), "A página do formulário não foi carregada corretamente."

@when("preencho todos os campos corretamente")
def preencher_formulario_completo(form_page):
    """Preenche todos os campos corretamente e submete"""
    test_data = generate_valid_test_data()
    form_page.fill_form(**test_data)  # Ajustado para garantir que `fill_form` aceita os argumentos corretamente
    form_page.submit_form()

@then("devo ver a mensagem de sucesso")
def validar_mensagem_sucesso(form_page):
    """Verifica se a mensagem de sucesso é exibida"""
    assert form_page.is_success_modal_visible(), "O modal de sucesso não foi exibido."


# 📌 Cenário 2: Tentar submeter formulário sem preencher todos os campos
@scenario("../../features/ui_form.feature", "Tentar submeter formulário sem preencher todos os campos")
def test_tentar_submeter_formulario_sem_preencher_todos_os_campos():
    pass

@when("tento submeter o formulário sem preencher todos os campos")
def submeter_formulario_vazio(form_page):
    """Tenta submeter um formulário incompleto"""
    test_data = generate_incomplete_data()
    form_page.fill_form(**test_data)
    form_page.submit_form()

@then("devo ver mensagens de erro indicando os campos obrigatórios")
def validar_mensagem_erro(form_page):
    """Valida se as mensagens de erro aparecem para campos obrigatórios"""
    assert form_page.has_validation_errors(), "As mensagens de erro não foram exibidas."


# 📌 Cenário 3: Tentar submeter formulário com senha fraca
@scenario("../../features/ui_form.feature", "Tentar submeter formulário com senha fraca")
def test_tentar_submeter_formulario_com_senha_fraca():
    pass

@when("preencho todos os campos corretamente com senha fraca")
def preencher_formulario_senha_fraca(form_page):
    """Tenta preencher o formulário com uma senha fraca"""
    test_data = generate_weak_password_data()
    form_page.fill_form(**test_data)
    form_page.submit_form()

@then("devo ver uma mensagem de erro sobre senha fraca")
def validar_mensagem_senha_fraca(form_page):
    """Verifica se a mensagem de erro de senha fraca aparece"""
    assert form_page.is_password_error_visible(), "A mensagem de senha fraca não foi exibida."


# 📌 Cenário 4: Tentar submeter formulário com e-mails diferentes
@scenario("../../features/ui_form.feature", "Tentar submeter formulário com e-mails diferentes")
def test_tentar_submeter_formulario_com_emails_diferentes():
    pass

@when("preencho todos os campos corretamente com e-mails diferentes")
def preencher_formulario_emails_diferentes(form_page):
    """Preenche o formulário com e-mails diferentes nos campos"""
    test_data = generate_mismatched_email_data()
    form_page.fill_form(**test_data)
    form_page.submit_form()

@then("devo ver uma mensagem de erro sobre e-mails diferentes")
def validar_mensagem_emails_diferentes(form_page):
    """Verifica se a mensagem de erro sobre e-mails diferentes aparece"""
    assert form_page.is_email_mismatch_error_visible(), "A mensagem de erro de e-mails diferentes não foi exibida."