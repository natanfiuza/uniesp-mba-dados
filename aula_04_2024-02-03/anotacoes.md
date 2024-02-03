# Aula 04


[Usando views](./doc/04-Views.md)

## O Comando `SELECT INTO`

O comando `SELECT INTO` copia dados de uma tabela para um nova tabela.

```sql

SELECT NOME, NULL AS campo_nulo
INTO CLIENTES2
FROM CLIENTES;

```

Consultando 5 registros da nova tabela;

```sql
SELECT TOP 5 * FROM clientes2;
```


| # |NOME | campo_nulo |
| --- | --- | --- | 
| 1| CLIENTE1 | NULL|
| 2| CLIENTE1 | NULL|
| 3| CLIENTE1 | NULL|
| 4| CLIENTE1 | NULL|
| 5| CLIENTE1 | NULL|

---

## O comando `CASE`

Avalia uma lista de condições e retorna uma das diversas expressões de resultados possíveis.

A expressão `CASE` tem dois formatos:

* A expressão simples CASE compara uma expressão a um conjunto de expressões simples para determinar o resultado.

* A CASEexpressão pesquisada avalia um conjunto de expressões booleanas para determinar o resultado.

Ambos os formatos suportam um argumento ELSE opcional.

CASEpode ser usado em qualquer instrução ou cláusula que permita uma expressão válida. Por exemplo, você pode usar CASEinstruções como SELECT, UPDATE, DELETE e SET, e em cláusulas como <select_list> , IN, WHERE, ORDER BY e HAVING.

Sintaxe`:

```sql

CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;

``` 

### Exemplo

#### Tabela

| OrderDetailID	| OrderID |	ProductID |	Quantity |
| --- | --- | --- | --- |
|1|	10248 |	11 |	12 |
|2|	10248 |	42 |	10 |
|3|	10248 |	72 |	5 |
|4|	10249 |	14 |	9 |
|5|	10249 |	51 |	40 |

#### Usando no `SELECT`

```sql

SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;

```
#### Usando no `ORDER BY`

```sql

SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    WHEN City IS NULL THEN Country
    ELSE City
END);

```
---

## Fotos


![](./img/20240203_085435.jpg)

---

[Home 🏠](../README.md) | [Indice 📇](README.md)