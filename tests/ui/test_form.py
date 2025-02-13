import time
from pytest_bdd import scenario, given, when, then
from utils.data_generator import generate_valid_test_data


@scenario("../../features/ui_form.feature", "Submeter formulário com sucesso")
def test_submeter_formulario_com_sucesso():
    pass

@given("que estou na página do formulário")
def acessar_pagina_formulario(form_page):
    """Acessa a página do formulário via navegação"""
    form_page.open()
    assert form_page.is_page_loaded(), "A página do formulário não foi carregada corretamente."


@when("preencho todos os campos corretamente")
def preencher_formulario_completo(form_page):
    """Preenche o formulário com dados válidos e realiza o upload de um arquivo"""
    test_data = generate_valid_test_data()
    form_page.fill_form(**test_data)
    form_page.upload_file("utils/sample_upload.txt")  # Caminho do arquivo no repositório


@when("submeto o formulário")
def submeter_formulario(form_page):
    """Clica no botão de submissão do formulário"""

    form_page.submit_form()


@then("devo ver a mensagem de sucesso")
def validar_mensagem_sucesso(form_page):
    """Valida se o modal de sucesso foi exibido"""
    assert form_page.is_success_modal_visible(), "O modal de sucesso não foi exibido."


@then("fecho o modal de sucesso")
def fechar_modal_sucesso(form_page):
    """Fecha o modal de sucesso após a submissão do formulário."""
    form_page.close_success_modal()


@scenario("../../features/ui_form.feature", "Tentar submeter formulário sem preencher todos os campos")
def test_tentar_submeter_formulario_sem_preencher_todos_os_campos():
    pass


@when("tento submeter o formulário sem preencher todos os campos")
def submeter_formulario_vazio(form_page):
    """Clica no botão de submit sem preencher nenhum campo"""
    form_page.submit_form_none()
    time.sleep(3)


@then("os campos obrigatórios devem ficar destacados em vermelho")
def validar_campos_destacados(form_page):
    """Verifica se os campos obrigatórios receberam um contorno vermelho"""
    campos_vermelhos = form_page.get_highlighted_required_fields()
    assert len(campos_vermelhos) == 4, f"Esperado 4 campos destacados, mas foram encontrados {len(campos_vermelhos)}"