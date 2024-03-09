# NESTED LOPP JOIN

O `NESTED LOOP JOIN` é um tipo de operação de junção no Microsoft SQL Server. Ele é frequentemente usado quando uma das tabelas na junção é pequena e a outra tabela é grande. Este método de junção usa um loop aninhado para comparar cada linha da tabela externa com todas as linhas da tabela interna.

Vamos considerar um exemplo usando duas tabelas, `Orders` e `Customers`, onde queremos obter informações sobre pedidos e clientes combinando os registros com base no `CustomerID`:

```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
```

Neste exemplo, se o otimizador de consultas decidir usar um `NESTED LOOP JOIN`, ele escolherá uma das tabelas como a tabela externa (normalmente a menor) e a outra como a tabela interna. O loop aninhado percorrerá cada linha da tabela externa e comparará com todas as linhas da tabela interna.

Você pode verificar o plano de execução para ver qual tipo de junção está sendo usado e outras estatísticas relacionadas. O plano de execução pode ser visualizado usando o comando `EXPLAIN` ou `SHOWPLAN` no SQL Server Management Studio (SSMS).

Aqui estão alguns links para a documentação oficial do Microsoft SQL Server que fornecem informações adicionais sobre os tipos de junção e o plano de execução:

1. Documentação sobre `NESTED LOOP JOIN`:
   - [NESTED LOOP JOIN (Transact-SQL)](https://docs.microsoft.com/en-us/sql/relational-databases/performance/joins/nested-loops-joins)

2. Documentação sobre planos de execução:
   - [Displaying Graphical Execution Plans (SQL Server Management Studio)](https://docs.microsoft.com/en-us/sql/relational-databases/performance/displaying-graphical-execution-plans-sql-server-management-studio)
   - [Showplan Logical and Physical Operators Reference](https://docs.microsoft.com/en-us/sql/relational-databases/performance/showplan-logical-and-physical-operators-reference)


-----

[Home 🏠](../README.md) | [Indice 📇](README.md)