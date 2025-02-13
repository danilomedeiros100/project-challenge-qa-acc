Feature: Testar a funcionalidade de ordenação no Sortable

  Scenario: Ordenar elementos na lista Sortable em ordem decrescente
    Given que estou na página "Sortable"
    When organizo os elementos na ordem decrescente
    Then os elementos devem estar na ordem decrescente