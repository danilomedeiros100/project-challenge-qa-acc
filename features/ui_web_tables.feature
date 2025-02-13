Feature: Gerenciamento de registros na Web Tables

#  Scenario: Criar múltiplos registros dinamicamente
#    Given que estou na página Web Tables
#    When crio 12 novos registros
#    Then todos os 12 registros devem estar na tabela

  Scenario: Deletar todos os registros
    Given que estou na página Web Tables
    When deleto todos os registros
    Then a tabela deve estar vazia