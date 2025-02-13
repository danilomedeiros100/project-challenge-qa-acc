Feature: Validação de Alertas

  Scenario: Validar exibição de alerta
    Given que estou na página "Alerts"
    When clico no botão "Click me"
    Then um alerta deve ser exibido com a mensagem "You clicked a button"