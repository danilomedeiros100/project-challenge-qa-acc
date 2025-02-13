Feature: Teste de janelas do navegador

  Scenario: Validar abertura de nova janela
    Given que estou na página "Browser Windows"
    When clico no botão "New Window"
    Then uma nova janela deve ser aberta com a mensagem "This is a sample page"