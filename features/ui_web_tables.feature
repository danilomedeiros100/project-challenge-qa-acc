Feature: Testar Web Tables

  Scenario: Criar, editar e excluir um registro com sucesso
    Given que estou na página "Web Tables"
    When crio um novo registro
    Then o registro deve estar na tabela
    When edito o registro criado
    Then os dados atualizados devem ser exibidos corretamente
    When deleto o registro
    Then o registro não deve mais estar na tabela


  Scenario: Criar, validar e excluir múltiplos registros dinamicamente
    Given que estou na página "Web Tables"
    When crio 12 novos registros
    Then todos os 12 registros devem estar na tabela
    When deleto todos os registros
    Then a tabela deve estar vazia