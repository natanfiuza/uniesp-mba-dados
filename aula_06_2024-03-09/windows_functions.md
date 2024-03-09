# Uso de Windows Functions

As funções de janela (Window Functions) no Microsoft SQL Server são uma categoria de funções analíticas que operam em um "conjunto de janelas" de dados. Essas funções permitem realizar cálculos e análises em grupos específicos de linhas, definidos por uma cláusula OVER.

Aqui estão alguns exemplos comuns de funções de janela:

1. **ROW_NUMBER:**
   - Atribui um número único para cada linha dentro de uma partição ordenada.

Exemplo:
```sql
SELECT 
    EmployeeID, 
    FirstName, 
    LastName, 
    ROW_NUMBER() OVER (ORDER BY LastName, FirstName) 
        AS RowNum
FROM 
    Employees;
```

2. **RANK e DENSE_RANK:**
   - Atribuem classificações às linhas com base em uma coluna de ordenação. `RANK` permite que as classificações sejam iguais para valores iguais, enquanto `DENSE_RANK` não.

Exemplo:
```sql
SELECT 
    ProductName, 
    Price,
    RANK() OVER (ORDER BY Price DESC) 
        AS Rank,
    DENSE_RANK() OVER (ORDER BY Price DESC) 
        AS DenseRank
FROM 
    Products;
```

3. **SUM, AVG, MAX, MIN:**
   - Calculam a soma, a média, o máximo ou o mínimo ao longo de uma janela especificada.

Exemplo:
```sql
SELECT OrderID, ProductID, Quantity,
        SUM(Quantity) OVER (PARTITION BY OrderID) AS TotalQuantity,
        AVG(Quantity) OVER () AS AvgQuantityOverall
FROM OrderDetails;
```

4. **LEAD e LAG:**
   - Acessam valores em linhas subsequentes (LEAD) ou linhas anteriores (LAG) em relação à linha atual.

   Exemplo:
   ```sql
   SELECT OrderID, ProductID, Quantity,
          LEAD(ProductID) OVER (ORDER BY OrderID) AS NextProductID,
          LAG(ProductID) OVER (ORDER BY OrderID) AS PreviousProductID
   FROM OrderDetails;
   ```

Esses são apenas alguns exemplos e há muitas outras funções de janela disponíveis. A documentação oficial do Microsoft SQL Server fornece informações detalhadas sobre o uso e a sintaxe dessas funções:

- [Funções de janela (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/functions/window-functions-transact-sql)

-----

[Home 🏠](../README.md) | [Indice 📇](README.md)