Feature: Testar o formulário de cadastro

  Scenario: Submeter formulário com sucesso
    Given que estou na página do formulário
    When preencho todos os campos corretamente
    And submeto o formulário
    Then devo ver a mensagem de sucesso
    And fecho o modal de sucesso


  Scenario: Tentar submeter formulário sem preencher todos os campos
    Given que estou na página do formulário
    When tento submeter o formulário sem preencher todos os campos
    Then os campos obrigatórios devem ficar destacados em vermelho

