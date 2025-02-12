Feature: Autenticação do Usuário

  Scenario: Gerar token de autenticação válido
    Given que eu tenho um usuário criado
    When envio uma requisição para autenticar o usuário
    Then a API deve retornar um token de autenticação