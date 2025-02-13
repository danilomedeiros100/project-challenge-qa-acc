from pytest_bdd import scenario, given, when, then


@scenario("../../features/ui_sortable.feature", "Ordenar elementos na lista Sortable em ordem decrescente")
def test_ordenar_elementos():
    """Executa o teste de ordenação no Sortable"""
    pass

@given('que estou na página "Sortable"')
def acessar_pagina_sortable(browser, sortable_page):
    """Acessa a página Sortable"""
    sortable_page.open()
    assert sortable_page.is_loaded(), "A página Sortable não foi carregada corretamente."

@when("organizo os elementos na ordem decrescente")
def ordenar_elementos(sortable_page):
    """Organiza os elementos na ordem decrescente"""
    sortable_page.sort_elements_descending()

@then("os elementos devem estar na ordem decrescente")
def validar_ordenacao(sortable_page):
    """Valida se os elementos foram reordenados corretamente na ordem decrescente"""
    assert sortable_page.is_sorted_correctly_descending(), "Os elementos não estão na ordem correta!"