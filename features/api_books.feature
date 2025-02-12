Feature: Listagem de livros disponíveis

  Scenario: Recuperar a lista de livros
    Given que estou autenticado na API
    When envio uma requisição para listar os livros
    Then a API deve retornar a lista de livros disponíveis