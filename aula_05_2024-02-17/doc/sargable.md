# SARGABLE

"SARGABLE" é uma abreviação para *"Search ARGument ABLE"* no contexto de bancos de dados, especialmente no Microsoft SQL Server. Esse termo refere-se à capacidade de uma expressão de busca (cláusula `WHERE`) ser otimizada para tirar vantagem dos índices existentes em uma tabela, resultando em consultas mais eficientes.

Quando uma expressão de busca é SARGABLE, o otimizador de consultas pode usar índices para acelerar a execução da consulta, reduzindo assim o tempo necessário para recuperar os dados desejados. Por outro lado, expressões não SARGABLE podem exigir uma varredura completa da tabela, tornando as consultas mais lentas, especialmente em tabelas grandes.

### Alguns exemplos de práticas que tornam uma expressão não SARGABLE incluem:

1. Uso de funções em colunas na cláusula WHERE: Se você aplicar funções a colunas em uma expressão de busca, o otimizador pode não ser capaz de usar índices eficientemente. Por exemplo, evitar algo como `WHERE UPPER(nome_coluna) = 'VALOR'`.

2. Uso de OR em vez de IN: A utilização de cláusulas OR pode dificultar a otimização da consulta. Em alguns casos, usar a cláusula IN pode ser mais eficiente.

3. Operadores de comparação não sargáveis: Alguns operadores de comparação podem tornar uma expressão não SARGABLE, como `LIKE '%valor%'`. Isso pode resultar em varreduras completas da tabela.

4. Combinação de colunas usando funções: Evitar combinações de colunas usando funções, como `WHERE CONCAT(coluna1, coluna2) = 'VALOR'`.

Ao escrever consultas no MS SQL Server, é importante considerar a sargabilidade para garantir um desempenho eficiente das consultas, especialmente em ambientes com grandes volumes de dados. Utilizar índices adequadamente e escrever expressões de busca de forma otimizada são práticas importantes para otimizar consultas SQL.

## Definição e exemplo

**SARGABLE** é um termo usado no contexto de consultas SQL para descrever predicados que permitem otimização eficiente de consultas pelo sistema de gerenciamento de banco de dados (SGBD). Vamos entender melhor:

### 1. **Definição**:
   - **SARGABLE** (ou "Search ARGument Able") refere-se aos predicados presentes na cláusula **WHERE** de uma consulta.
   - Um predicado é considerado **sargable** se o SGBD pode aproveitar um índice para melhorar o tempo de execução da consulta.
   - Em outras palavras, um predicado sargable permite que o SGBD realize uma operação de **Index Seek**.

### 2. **Exemplo**:
   - Suponha que temos uma tabela de funcionários com uma coluna **FirstName**.
   - Consultas como `WHERE FirstName = 'Paul'` são sargables, pois podem usar um índice na coluna **FirstName** para acelerar a busca.
   - No entanto, consultas como `WHERE LEFT(FirstName, 5) = 'Paul'` não são sargables, pois envolvem uma função aplicada à coluna, impedindo o uso eficiente de um índice¹².

### 3. **Benefícios**:
   - Consultas sargables são mais rápidas, pois minimizam o acesso ao disco.
   - Otimizam o uso de índices, reduzindo o número de leituras de disco.

Em resumo, ao escrever consultas SQL, é importante considerar a sargabilidade dos predicados para obter melhor desempenho nas operações de busca e filtragem de dados.

Para saber mais sobre SARGABLE e como otimizar consultas no SQL Server, você pode consultar os seguintes links:
- [Você sabe a diferença entre uma consulta Sargable e non-Sargable? | iMasters](https://imasters.com.br/banco-de-dados/voce-sabe-a-diferenca-entre-uma-consulta-sargable-e-non-sargable)
- [O que é Sargable argument? - Stack Overflow em Português](https://pt.stackoverflow.com/questions/21793/o-que-%C3%A9-sargable-argument)
- [Dicas de T-SQL – SARGable - Agilidata](https://agilidata.com.br/2021/02/08/dicas-de-t-sql-sargable/)

