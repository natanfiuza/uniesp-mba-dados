# HASH JOIN

O `HASH JOIN` é um método de junção utilizado no Microsoft SQL Server para combinar linhas de duas tabelas com base em uma condição de junção. Este método é especialmente útil quando as tabelas não estão ordenadas de maneira eficiente para um `MERGE JOIN` ou quando a otimização de junção necessária não é alcançada através de um `NESTED LOOP JOIN`. O `HASH JOIN` envolve a criação de tabelas hash temporárias para otimizar a junção.

Vamos considerar um exemplo de como usar o `HASH JOIN` com duas tabelas, `Orders` e `Customers`, onde queremos obter informações sobre pedidos e clientes combinando os registros com base no `CustomerID`:

```sql
SELECT 
    Orders.OrderID, 
    Customers.CustomerName
FROM 
    Orders
        JOIN Customers ON Orders.CustomerID = Customers.CustomerID
```

Quando o otimizador de consultas decide usar um `HASH JOIN` para essa consulta, ele criará uma tabela hash temporária para a tabela `Customers` e outra para a tabela `Orders`. O SQL Server calculará um hash para cada valor na coluna de junção e os armazenará nas tabelas hash temporárias.

A tabela hash é eficiente para procurar correspondências, permitindo que o SQL Server combine as linhas das duas tabelas com base nos valores hash calculados. Esse processo é particularmente útil quando as tabelas não estão ordenadas adequadamente para um `MERGE JOIN`.

É importante notar que o `HASH JOIN` pode ser eficiente para grandes conjuntos de dados, mas também requer recursos significativos de memória. O desempenho do `HASH JOIN` é impactado pela disponibilidade de recursos do sistema, tamanho das tabelas envolvidas e configurações específicas do servidor SQL.

O otimizador de consultas do SQL Server toma decisões automaticamente com base nas estatísticas e índices disponíveis, e o tipo de junção escolhido pode ser visto no plano de execução gerado pela consulta.

Documentação sobre

1. **HASH JOIN:**
   - [HASH JOIN (Transact-SQL)](https://docs.microsoft.com/en-us/sql/relational-databases/performance/joins/hash-joins)