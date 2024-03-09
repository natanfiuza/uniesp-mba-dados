# Windows Functions no MySQL

Sim, o MySQL também oferece funções de janela, semelhantes às Windows Functions no Microsoft SQL Server. As funções de janela no MySQL são conhecidas como funções de janela ou funções de análise.

Aqui estão alguns exemplos comuns de funções de janela no MySQL:

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
   - Atribuem classificações às linhas com base em uma coluna de ordenação.

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
SELECT 
    OrderID, 
    ProductID, 
    Quantity,
    SUM(Quantity) OVER (PARTITION BY OrderID) 
        AS TotalQuantity,
    AVG(Quantity) OVER () 
        AS AvgQuantityOverall
FROM 
    OrderDetails;
```

4. **LEAD e LAG:**
   - Acessam valores em linhas subsequentes (LEAD) ou linhas anteriores (LAG) em relação à linha atual.

Exemplo:
```sql
SELECT 
    OrderID, 
    ProductID, 
    Quantity,
    LEAD(ProductID) OVER (ORDER BY OrderID) 
        AS NextProductID,
    LAG(ProductID) OVER (ORDER BY OrderID) 
        AS PreviousProductID
FROM 
    OrderDetails;
```
5. **PERCENT_RANK**

A função `PERCENT_RANK()` no MySQL é uma função de janela que calcula a posição relativa de uma linha dentro de um conjunto de dados ordenado como uma porcentagem. Essa função atribui uma classificação percentual a cada linha em relação ao total de linhas no conjunto de resultados, com base na ordem de classificação especificada.

A sintaxe básica da função `PERCENT_RANK()` é a seguinte:

```sql
PERCENT_RANK() OVER (
  [PARTITION BY partition_expression, ... ]
  ORDER BY sort_expression [ASC | DESC], ...
)
```

- `PARTITION BY`: Opcional. Divide o conjunto de resultados em partições às quais a função é aplicada separadamente.

- `ORDER BY`: Especifica a ordem das linhas dentro de cada partição.

Aqui está um exemplo simples de uso da função `PERCENT_RANK()`:

```sql
SELECT
  EmployeeID,
  Salary,
  PERCENT_RANK() OVER (ORDER BY Salary DESC) 
    AS PercentRank
FROM
  Employees;
```

Neste exemplo, a função `PERCENT_RANK()` calcula a classificação percentual com base no salário em ordem decrescente. Cada linha receberá um valor entre 0 e 1, indicando sua posição relativa em termos percentuais.

A documentação oficial do MySQL fornece mais detalhes sobre a função `PERCENT_RANK()` e outras funções de janela:

- [PERCENT_RANK()](https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html#function_percent-rank)
- [Funções de janela (funções de análise)](https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html)