Feature: Testar o formulário de cadastro

  Scenario: Submeter formulário com sucesso
    Given que estou na página do formulário
    When preencho todos os campos corretamente
    And submeto o formulário
    Then devo ver a mensagem de sucesso

  Scenario: Tentar submeter formulário sem preencher todos os campos
    Given que estou na página do formulário
    When tento submeter o formulário sem preencher todos os campos
    Then devo ver mensagens de erro indicando os campos obrigatórios

  Scenario: Tentar submeter formulário com senha fraca
    Given que estou na página do formulário
    When preencho todos os campos corretamente com senha fraca
    And submeto o formulário
    Then devo ver uma mensagem de erro sobre senha fraca

  Scenario: Tentar submeter formulário com e-mails diferentes
    Given que estou na página do formulário
    When preencho todos os campos corretamente com e-mails diferentes
    And submeto o formulário
    Then devo ver uma mensagem de erro sobre e-mails diferentes