import time
import pytest
from pytest_bdd import scenario, given, when, then
from utils.data_generator import  generate_valid_web_tables_data


# Cenário 1: Criar, editar e excluir um registro com sucesso
@scenario("../../features/ui_web_tables.feature", "Criar, editar e excluir um registro com sucesso")
def test_criar_editar_excluir_registro():
    pass


# Cenário 2: Criar, validar e excluir múltiplos registros dinamicamente
@scenario("../../features/ui_web_tables.feature", "Criar, validar e excluir múltiplos registros dinamicamente")
def test_criar_validar_excluir_multiplos_registros():
    pass


@given('que estou na página "Web Tables"')
def acessar_pagina_web_tables(browser, web_tables_page):
    """Acessa a página Web Tables, remove registros existentes e ajusta a exibição da tabela"""
    web_tables_page.open()
    assert web_tables_page.is_loaded(), "A página Web Tables não foi carregada corretamente."

    # Excluir todos os registros existentes antes de criar novos
    web_tables_page.delete_all_records()

    # 🔹 Alterar para exibir 20 registros por página **logo após a remoção**
    web_tables_page.change_table_display_count(20)


@when("crio um novo registro")
def criar_novo_registro(web_tables_page):
    """Cria um novo registro na tabela"""
    web_tables_page.open_add_record_modal()  # Garante que o modal será aberto antes de preencher

    # 🔹 Aguarda a abertura do modal antes de prosseguir
    assert web_tables_page.is_modal_open(), "O modal de registro não foi aberto!"

    registro = generate_valid_web_tables_data()  # 🚀 Certifique-se de usar a função correta

    print(f"🔍 Chaves no registro gerado: {registro.keys()}")

    campos_validos = ["first_name", "last_name", "email", "age", "salary", "department"]
    for campo in campos_validos:
        registro.setdefault(campo, "N/A")  # Evita KeyError caso algum campo esteja ausente

    web_tables_page.fill_registration_form(**registro)
    web_tables_page.submit_registration()

    pytest.registro_atual = registro  # 🔹 Salva o registro para ser validado depois
    print(f"📌 Registro salvo para validação: {pytest.registro_atual}")  # Debugging


@then("o registro deve estar na tabela")
def validar_registro_na_tabela(web_tables_page):
    """Verifica se o registro foi adicionado corretamente na tabela"""
    print(f"📌 Verificando registro salvo: {pytest.registro_atual}")  # Debugging

    assert pytest.registro_atual, "O registro_atual não foi definido!"
    assert web_tables_page.is_record_present(pytest.registro_atual), "O registro não foi encontrado na tabela!"


@when("edito o registro criado")
def editar_registro(web_tables_page):
    """Edita o primeiro registro na tabela"""
    assert pytest.registro_atual, "Não há registro salvo para edição!"

    novo_nome = "Editado " + pytest.registro_atual["first_name"]
    pytest.registro_atual["first_name"] = novo_nome  # Atualiza o nome

    web_tables_page.edit_first_record(novo_nome)  # Chama o método para editar o primeiro registro


@then("os dados atualizados devem ser exibidos corretamente")
def validar_registro_editado(web_tables_page):
    """Confirma que o nome foi alterado corretamente na tabela"""
    assert web_tables_page.is_record_present(pytest.registro_atual), "O registro editado não foi encontrado!"


@when("deleto o registro")
def deletar_registro(web_tables_page):
    """Remove o primeiro registro da tabela"""
    web_tables_page.delete_first_record()


@then("o registro não deve mais estar na tabela")
def validar_registro_excluido(web_tables_page):
    """Verifica se o registro foi removido da tabela"""
    assert not web_tables_page.is_record_present(pytest.registro_atual), "O registro ainda está na tabela!"



@when("crio 12 novos registros")
def criar_multiplos_registros(web_tables_page):
    """Cria 12 novos registros dinamicamente"""
    pytest.registros_criados = []
    for _ in range(10):
        registro = generate_valid_web_tables_data()
        pytest.registros_criados.append(registro)
        web_tables_page.click_add_button()
        web_tables_page.fill_registration_form(**registro)
        web_tables_page.submit_registration()

    # Alterar para exibir 20 registros por página
    web_tables_page.change_table_display_count(20)


@when("crio 12 novos registros")
def criar_multiplos_registros(web_tables_page):
    """Cria 12 novos registros dinamicamente"""
    pytest.registros_criados = []

    for _ in range(12):
        registro = generate_valid_web_tables_data()
        pytest.registros_criados.append(registro)
        web_tables_page.click_add_button()
        web_tables_page.fill_registration_form(**registro)
        web_tables_page.submit_registration()

    # 📌 Alterar exibição para garantir que todos os 12 registros apareçam
    web_tables_page.change_table_display_count(20)

@then("todos os 12 registros devem estar na tabela")
def validar_multiplos_registros_na_tabela(web_tables_page):
    """Verifica se todos os 12 registros foram adicionados corretamente na tabela"""
    assert len(pytest.registros_criados) == 12, "Os registros criados não foram armazenados corretamente!"

    for registro in pytest.registros_criados:
        assert web_tables_page.is_record_present(registro), f"O registro {registro} não foi encontrado na tabela!"

@when("deleto todos os registros")
def deletar_todos_registros(web_tables_page):
    """Deleta todos os registros criados"""
    web_tables_page.delete_all_records()


@then("a tabela deve estar vazia")
def validar_tabela_vazia(web_tables_page):
    """Verifica se a tabela está vazia"""
    assert web_tables_page.is_table_empty(), "A tabela ainda contém registros!"