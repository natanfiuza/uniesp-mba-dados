# O uso do JOIN no MS SQL Server


No Microsoft SQL Server, a cláusula `JOIN` é usada para combinar linhas de duas ou mais tabelas com base em uma condição relacionada entre elas. Existem vários tipos de `JOIN` disponíveis, e cada um serve a um propósito específico. Vamos explorar os principais tipos de `JOIN` com exemplos práticos:

1. **INNER JOIN:**
   - Retorna apenas as linhas que têm correspondências nas duas tabelas.

Exemplo:
```sql
SELECT 
    Orders.OrderID, 
    Customers.CustomerName
FROM 
    Orders
        INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```

2. **LEFT JOIN (ou LEFT OUTER JOIN):**
   - Retorna todas as linhas da tabela à esquerda e as linhas correspondentes da tabela à direita. Se não houver correspondência, as colunas da tabela à direita conterão valores nulos.

Exemplo:
```sql
SELECT 
    Employees.EmployeeID, 
    Employees.EmployeeName, 
    Departments.DepartmentName
FROM 
    Employees
        LEFT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```

3. **RIGHT JOIN (ou RIGHT OUTER JOIN):**
   - Retorna todas as linhas da tabela à direita e as linhas correspondentes da tabela à esquerda. Se não houver correspondência, as colunas da tabela à esquerda conterão valores nulos.

Exemplo:
```sql
SELECT 
    Departments.DepartmentID, 
    Departments.DepartmentName, 
    Employees.EmployeeName
FROM 
    Departments
        RIGHT JOIN Employees ON Departments.DepartmentID = Employees.DepartmentID;
```

4. **FULL JOIN (ou FULL OUTER JOIN):**
   - Retorna todas as linhas quando há uma correspondência em uma das tabelas. Se não houver correspondência, as colunas da tabela sem correspondência conterão valores nulos.

Exemplo:
```sql
SELECT 
    Customers.CustomerID, 
    Customers.CustomerName, 
    Orders.OrderID
FROM 
    Customers
        FULL JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
```

5. **CROSS JOIN:**
   - Retorna o produto cartesiano de duas tabelas, ou seja, todas as combinações possíveis de linhas.

Exemplo:
```sql
SELECT 
    Employees.EmployeeName, 
    Departments.DepartmentName
FROM 
    Employees
        CROSS JOIN Departments;
```

6. **SELF JOIN:**
   - Uma tabela é combinada com ela mesma.

Exemplo:
```sql
SELECT 
    e1.EmployeeName 
        AS Employee1, 
    e2.EmployeeName 
        AS Employee2
FROM 
    Employees e1
        JOIN Employees e2 ON e1.ManagerID = e2.EmployeeID;
```

Esses são os principais tipos de JOIN no  Microsoft SQL Server. A escolha do tipo de JOIN depende dos requisitos específicos da consulta e da relação desejada entre as tabelas envolvidas.


Documentação:

1. **INNER JOIN (Transact-SQL):**
   - [INNER JOIN (Transact-SQL)](https://docs.microsoft.com/en-us/sql/relational-databases/performance/joins/inner-join-transact-sql)
