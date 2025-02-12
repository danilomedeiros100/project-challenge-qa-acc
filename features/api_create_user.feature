Feature: Criar um novo usuário na API

  Scenario: Criar um usuário com credenciais válidas
    Given que eu tenho um nome de usuário e uma senha válidos
    When envio uma requisição para criar um usuário
    Then a API deve retornar um status 201
    And o usuário deve ser criado com sucesso