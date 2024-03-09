# Estatísticas

No Microsoft SQL Server, as estatísticas desempenham um papel crucial no desempenho das consultas, especialmente em cláusulas `WHERE`. As estatísticas ajudam o otimizador de consultas a tomar decisões informadas sobre como acessar os dados de maneira eficiente. Vou explicar o processo geral e fornecer alguns exemplos.

## Funcionamento Geral:

1. **Coleta de Estatísticas:**
   - O SQL Server coleta automaticamente estatísticas sobre as colunas das tabelas. Essas estatísticas incluem informações como a distribuição dos valores, a cardinalidade, entre outros.

2. **Otimização da Consulta:**
   - Ao receber uma consulta, o otimizador de consultas analisa as estatísticas para determinar o plano de execução mais eficiente.

3. **Estimativa de Cardinalidade:**
   - O otimizador utiliza as estatísticas para estimar o número de linhas que serão retornadas por uma determinada operação, como uma cláusula `WHERE`.

4. **Escolha de Índices:**
   - Com base nas estatísticas, o otimizador decide se deve usar índices ou realizar uma leitura completa da tabela para satisfazer a cláusula `WHERE`.

## Exemplo:

Vamos considerar uma tabela `Clientes` com uma coluna `Idade`. O SQL Server coleta estatísticas sobre a distribuição de idades nessa coluna.

```sql
-- Exemplo de criação da tabela
CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    Nome NVARCHAR(100),
    Idade INT
);

-- Exemplo de consulta com cláusula WHERE
SELECT 
    Nome
FROM 
    Clientes
WHERE 
    Idade = 25;
```

No caso acima, as estatísticas ajudarão o otimizador a decidir se deve usar um índice na coluna `Idade` para buscar rapidamente os registros com idade 25 ou se deve realizar uma varredura completa da tabela.

## Atualização de Estatísticas:

É importante observar que as estatísticas podem ficar desatualizadas com o tempo, especialmente em tabelas que sofrem muitas alterações. Para garantir que as estatísticas estejam atualizadas, você pode programar atualizações regulares ou usar a opção `AUTO_UPDATE_STATISTICS` do SQL Server.

```sql
-- Atualização de estatísticas
UPDATE STATISTICS Clientes;
```

A atualização de estatísticas pode ser realizada de maneira manual ou automática pelo SQL Server.

Lembre-se de que o SQL Server é bastante sofisticado na otimização de consultas, e o entendimento detalhado do plano de execução e do comportamento do otimizador pode ser necessário para otimizar consultas de maneira eficaz.

## Comando DBCC SHOW_STATISTICS

O comando `DBCC SHOW_STATISTICS` é usado para exibir informações detalhadas sobre as estatísticas de índice associadas a uma tabela ou exibição no Microsoft SQL Server.

Aqui está um exemplo de uso do `DBCC SHOW_STATISTICS`:

```sql
-- Exemplo de uso do DBCC SHOW_STATISTICS
DBCC SHOW_STATISTICS('NomeDaTabela', 'NomeDoIndiceOuEstatistica');
```

Este comando exibirá informações detalhadas sobre as estatísticas associadas ao índice ou estatística especificado na tabela.

Quanto à documentação oficial, aqui está o link relevante:

- [DBCC SHOW_STATISTICS (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-show-statistics-transact-sql?view=sql-server-ver15)

Esta página fornece informações detalhadas sobre como usar o `DBCC SHOW_STATISTICS` e o significado dos resultados retornados.

## Documentação

Para obter informações detalhadas sobre estatísticas no Microsoft SQL Server, você pode consultar a documentação oficial do SQL Server. Aqui estão alguns links relevantes:

1. **Exibições de estatísticas dinâmicas (Transact-SQL):**
   - [Dynamic Management Views and Functions (Transact-SQL) - sys.dm_db_stats_properties](https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/statistical-views-transact-sql?view=sql-server-ver15#sys-dm-db-stats-properties-transact-sql)

2. **Como o Otimizador de Consultas Usa as Estatísticas:**
   - [Statistics - How the Query Optimizer Uses Statistics](https://docs.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver15)

3. **Atualização de Estatísticas:**
   - [Update Statistics](https://docs.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver15#update-statistics)

Esses links fornecerão informações abrangentes sobre como o SQL Server utiliza estatísticas para otimização de consultas, como você pode visualizar estatísticas e como realizar a atualização de estatísticas quando necessário.