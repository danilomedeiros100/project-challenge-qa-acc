Feature: Reserva de livros

  Scenario: Reservar dois livros disponíveis
    Given que estou autenticado na API
    And tenho o ID de dois livros disponíveis
    When envio uma requisição para reservar os livros
    Then a API deve confirmar a reserva dos livros
    And os livros devem estar no perfil do usuário