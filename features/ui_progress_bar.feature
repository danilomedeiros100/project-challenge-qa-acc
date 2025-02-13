Feature: Testar o Progress Bar

  Scenario: Controlar o progresso da barra de progresso
    Given que estou na página "Progress Bar"
    When inicio o progresso
    And paro o progresso antes de 25%
    Then o valor da progress bar deve ser menor ou igual a 25%
    When inicio novamente e aguardo 100%
    And reseto a progress bar
    Then o valor da progress bar deve ser 0%