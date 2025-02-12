Feature: Consultar detalhes de um usuário

  Como um usuário autenticado
  Quero poder consultar meus detalhes na API
  Para verificar se minhas informações estão corretas

  Scenario: Recuperar os detalhes do usuário autenticado
    Given que eu tenho um usuário criado e autenticado
    When eu envio uma requisição para obter os detalhes do usuário
    Then a API deve retornar os detalhes corretos do usuário