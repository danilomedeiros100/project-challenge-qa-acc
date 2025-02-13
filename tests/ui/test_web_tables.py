import pytest
from pytest_bdd import given, when, then, scenarios

from pages.web_tables_page import WebTablesPage


scenarios("../../features/ui_web_tables.feature")

@pytest.fixture
def web_tables_page(browser):

    page = WebTablesPage(browser)
    page.open()
    return page

@given("que estou na página Web Tables")
def acessar_pagina_web_tables(browser):
    """Abre a página Web Tables"""
    page = WebTablesPage(browser)
    page.open()
    time.sleep(5)

import time


@then("todos os 12 registros devem estar na tabela")
def validar_registros(web_tables_page):
    """Verifica se os 12 registros foram inseridos corretamente"""
    web_tables_page.set_page_size("25")  # Ajusta para exibir mais registros
    time.sleep(2)  # Pequena pausa para evitar falsos negativos
    assert web_tables_page.count_table_rows() == 12, "Nem todos os registros foram adicionados corretamente!"

@then("todos os 12 registros devem estar na tabela")
def validar_registros(web_tables_page):
    assert web_tables_page.count_table_rows() == 12, "Nem todos os registros foram adicionados corretamente!"

@when("deleto todos os registros")
def deletar_todos_registros(web_tables_page):
    web_tables_page.delete_all_records()

@then("a tabela deve estar vazia")
def validar_tabela_vazia(web_tables_page):
    assert web_tables_page.count_table_rows() == 0, "A tabela ainda contém registros!"