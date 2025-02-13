Feature: Validação da Abertura de Nova Aba

  Scenario: Validar abertura de nova aba
    Given que estou na página "Browser Windows"
    When clico no botão "New Tab"
    Then uma nova aba deve ser aberta com a mensagem "This is a sample page"