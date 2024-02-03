# Functions

As funções do servidor SQL são ações pré-construídas que realizam cálculos, manipulam dados e retornam resultados. No nível mais fundamental, essas funções simplificam consultas complexas e automatizam tarefas repetitivas.

As funções SQL comuns incluem funções de string, numéricas, de data/hora, condicionais e agregadas. Essas funções oferecem aos usuários a capacidade de extrair e analisar dados de enormes bancos de dados de forma eficiente e eficaz.

Cria uma função definida pelo usuário. Uma função definida pelo usuário é uma rotina Transact-SQL ou CLR (Common Language Runtime) que aceita parâmetros, executa uma ação, como um cálculo complexo, e retorna o resultado dessa ação como um valor. O valor de retorno pode ser um valor escalar (único) ou uma tabela. 

Use essa instrução para criar uma rotina reutilizável que possa ser usada destas maneiras:

* Em instruções Transact-SQL, como SELECT

* Em aplicativos que chamam a função

* Na definição de outra função definida pelo usuário

* Para parametrizar uma exibição ou aprimorar a funcionalidade de uma exibição indexada

* Para definir uma coluna em uma tabela

* Para definir uma restrição CHECK em uma coluna

* Para substituir um procedimento armazenado

* Usar uma função embutida como um predicado de filtro para uma política de segurança
  
### Limitações e restrições

* Funções definidas pelo usuário não podem ser usadas para executar ações que modifiquem o estado do banco de dados.

* Funções definidas pelo usuário não podem conter uma cláusula `OUTPUT INTO` que tenha uma tabela como destino.

* Funções definidas pelo usuário não podem retornar vários conjuntos de resultados. Use um procedimento armazenado se precisar retornar vários conjuntos de resultados.

* O tratamento de erros é restrito a uma função definida pelo usuário. Uma UDF não oferece suporte a `TRY...CATCH`, `@ERROR` ou `RAISERROR`.

* As funções definidas pelo usuário não podem chamar um procedimento armazenado, mas podem chamar um procedimento armazenado estendido.

* As funções definidas pelo usuário não podem usar SQL dinâmico ou tabelas temporárias. Variáveis de tabela são permitidas.

* Instruções `SET` não são permitidas em uma função definida pelo usuário.

* A cláusula `FOR XML` não é permitida.

* Funções definidas pelo usuário podem ser aninhadas; isto é, uma função definida pelo usuário pode chamar outra. O nível de aninhamento é incrementado quando a função chamada inicia a execução e decrementado quando a função chamada termina a execução. As funções definidas pelo usuário podem ser aninhadas em até 32 níveis. Exceder os níveis máximos de aninhamento causa falha em toda a cadeia de funções de chamada. Qualquer referência ao código gerenciado de uma função definida pelo usuário do `Transact-SQL` conta como um nível em relação ao limite de aninhamento de 32 níveis. Os métodos invocados de dentro do código gerenciado não contam nesse limite.

As seguintes instruções do `Service Broker` não podem ser incluídas na definição de uma função Transact-SQL definida pelo usuário:

* BEGIN DIALOG CONVERSATION
* END CONVERSATION
* GET CONVERSATION GROUP
* MOVE CONVERSATION
* RECEIVE
* SEND


### Função `scalar`

Funções `scalar` retornam um unico valor inteiro, string.


```sql

-- Transact-SQL Scalar Function Syntax
CREATE [ OR ALTER ] FUNCTION [ schema_name. ] function_name
( [ { @parameter_name [ AS ][ type_schema_name. ] parameter_data_type [ NULL ]
 [ = default ] [ READONLY ] }
    [ ,...n ]
  ]
)
RETURNS return_data_type
    [ WITH <function_option> [ ,...n ] ]
    [ AS ]
    BEGIN
        function_body
        RETURN scalar_expression
    END
[ ; ]

```

Exemplo: 

```sql

IF OBJECT_ID (N'dbo.ufnGetInventoryStock', N'FN') IS NOT NULL
    DROP FUNCTION ufnGetInventoryStock;
GO
CREATE FUNCTION dbo.ufnGetInventoryStock(@ProductID int)
RETURNS int
AS
-- Returns the stock level for the product.
BEGIN
    DECLARE @ret int;
    SELECT @ret = SUM(p.Quantity)
    FROM Production.ProductInventory p
    WHERE p.ProductID = @ProductID
        AND p.LocationID = '6';
     IF (@ret IS NULL)
        SET @ret = 0;
    RETURN @ret;
END;


```

## Função com valor de tabela embutida (TVF)
Retorna um valor como uma tabela ou tambem chamada de função de tabulação


```sql

IF OBJECT_ID (N'Sales.ufn_SalesByStore', N'IF') IS NOT NULL
    DROP FUNCTION Sales.ufn_SalesByStore;
GO
CREATE FUNCTION Sales.ufn_SalesByStore (@storeid int)
RETURNS TABLE
AS
RETURN
(
    SELECT P.ProductID, P.Name, SUM(SD.LineTotal) AS 'Total'
    FROM Production.Product AS P
    JOIN Sales.SalesOrderDetail AS SD ON SD.ProductID = P.ProductID
    JOIN Sales.SalesOrderHeader AS SH ON SH.SalesOrderID = SD.SalesOrderID
    JOIN Sales.Customer AS C ON SH.CustomerID = C.CustomerID
    WHERE C.StoreID = @storeid
    GROUP BY P.ProductID, P.Name
);


```

Uso da função

```sql

SELECT * FROM Sales.ufn_SalesByStore(602);

```
---

## Funções de sistema 

Algumas funções que já existem no MS SQL Server

### Função da parte da data: DATEPART()

A função de parte de data extrai uma parte especificada de uma data, como ano, mês ou dia.

Exemplo de parte de data:

```sql
SELECT DATEPART( year , '2023-05-05' );   
```

Saída:

```
2023
```

### Função: GETDATE()

Retorna o carimbo de data/hora do sistema do banco de dados atual como um valor de datetime sem o deslocamento de fuso horário do banco de dados. Esse valor é derivado do sistema operacional do computador no qual a instância do SQL Server está sendo executada.

```sql

SELECT GETDATE() AS data_atual;

```
Saída:

| data_atual |
| -- | 
| 2024-02-03 14:13:47.643 | 

### Função  CAST()

A função `cast` converte um tipo de dados em outro tipo de dados.

Exemplo de uso 

```sql
SELECT CAST(10 AS VARCHAR) AS numero; 
```

Saída:

| numero |
| --- |
| '10' |


### Função SUM()

Retorna a soma de todos os valores ou somente os valores `DISTINCT` na expressão. `SUM` pode ser usado exclusivamente com colunas numéricas. 
Valores nulos são ignorados.

Sintaxe

```sql

-- Aggregate Function Syntax    
SUM ( [ ALL | DISTINCT ] expression )  

-- Analytic Function Syntax   
SUM ([ ALL ] expression) OVER ( [ partition_by_clause ] order_by_clause)  

```
#### Tipos de retorno

Retorna o somatório de todos os valores de `expression` no tipo de dados de `expression` mais preciso.


| Resultado da expressão |	Tipo de retorno |
| --- | --- | 
| tinyint | 	int| 
| smallint |	int |
| int	| int |
| bigint	| bigint
| Categoria decimal (p, s)	| decimal(38, s) | 
| Categorias money e smallmoney |	money |
| Categorias float e real	 | float | 


#### Exemplos

O exemplo a seguir mostra como usar a função `SUM()` para retornar dados resumidos.

```sql

SELECT Color, SUM(ListPrice) AS ListPrice, SUM(StandardCost) AS StandardCost  
FROM Production.Product  
WHERE Color IS NOT NULL   
    AND ListPrice != 0.00   
    AND Name LIKE 'Mountain%'  
GROUP BY Color  
ORDER BY Color;  
GO


```

Retorno

| Color | ListPrice | StandardCost |
| --- | --- | --- |
| Black    |       27404.84   | 5214.9616 |
| Silver    |      26462.84  | 14665.6792 |
| White   |   19.00   |    6.7926 |

---

## Query da aula sobre Functions

Segue abaixo as querys da aula sobre Functions.

```sql


USE DISCIPLINA02
GO

--Função escalar
CREATE FUNCTION dbo.fn_Semestre(@data DATETIME)
RETURNS INT
AS
BEGIN
	DECLARE @semestre TINYINT
	SELECT @semestre =
		CASE
			WHEN DATEPART(mm,@data) > 6 THEN 2
			ELSE 1
		END

	RETURN(@SEMESTRE)
END;
GO

SELECT dbo.fn_Semestre(GETDATE());
GO
SELECT dbo.fn_Semestre('20150601');
GO

SELECT V.DATA, 'A compra foi realizada no semestre: ' + CAST(dbo.fn_Semestre(V.DATA) AS CHAR(1)) AS MSG
FROM VENDAS AS V;
GO

--Listar as compras do 1o semestre
SELECT V.*
FROM VENDAS AS V
WHERE dbo.fn_Semestre(V.DATA) = 1;
GO

--Função tabular (inline)
CREATE FUNCTION dbo.fn_totalCompras(@IDCLIENTE INT)
RETURNS TABLE
AS
RETURN
(
	SELECT V.IDCLIENTE, SUM(IV.VALOR) AS TOTAL
	FROM CLIENTES AS C
	INNER JOIN VENDAS AS V ON (V.IDCLIENTE = C.IDCLIENTE)
	INNER JOIN ITENS_VENDAS IV ON (IV.IDVENDA = V.IDVENDA)
	WHERE V.IDCLIENTE = @IDCLIENTE
	GROUP BY V.IDCLIENTE
);
GO

SELECT *
FROM dbo.fn_totalCompras(1);
GO


--Função tabular (multi-statement)
CREATE FUNCTION dbo.fn_UltimaCompraMelhoresClientes()
RETURNS @VENDAS TABLE(
	IDCLIENTE INT,
	DATA DATETIME
)
AS
BEGIN
	DECLARE @CLIENTES TABLE(
		IDCLIENTE INT
	)

	INSERT INTO @CLIENTES
	SELECT TOP 3 C.IDCLIENTE
	FROM CLIENTES AS C
	INNER JOIN VENDAS AS V ON (V.IDCLIENTE = C.IDCLIENTE)
	GROUP BY C.IDCLIENTE
	ORDER BY COUNT(*) DESC;

	INSERT INTO @VENDAS
	SELECT C.IDCLIENTE, MAX(V.DATA) AS DATA
	FROM CLIENTES AS C
	INNER JOIN VENDAS AS V ON (C.IDCLIENTE = V.IDCLIENTE)
	WHERE EXISTS(
		SELECT 1
		FROM @CLIENTES AS CLI
		WHERE CLI.IDCLIENTE = C.IDCLIENTE
	)
	GROUP BY C.IDCLIENTE;


	RETURN;
END;
GO

SELECT U.IDCLIENTE, U.DATA, C.NOME
FROM dbo.fn_UltimaCompraMelhoresClientes() as U
INNER JOIN CLIENTES AS C ON (C.IDCLIENTE = U.IDCLIENTE);
GO


--FUNÇOES COM CROSS APPLY
CREATE FUNCTION dbo.fn_primeira_venda(@IDCLIENTE INT)
RETURNS TABLE
AS
RETURN
(
	SELECT TOP 1 V.DATA
	FROM VENDAS AS V
	WHERE V.IDCLIENTE = @IDCLIENTE
	ORDER BY V.DATA ASC
);
GO

SELECT C.NOME, PV.DATA AS DT_PRIMEIRA_VENDA
FROM CLIENTES AS C
CROSS APPLY dbo.fn_primeira_venda(C.IDCLIENTE) as PV
ORDER BY 1, 2;
GO


--TRATAMENTO DE NULOS
SELECT dbo.fn_Semestre(NULL);
GO

ALTER FUNCTION dbo.fn_Semestre(@data DATETIME)
RETURNS INT
WITH RETURNS NULL ON NULL INPUT
AS
BEGIN
	DECLARE @semestre TINYINT
	SELECT @semestre =
		CASE
			WHEN DATEPART(mm,@data) > 6 THEN 2
			ELSE 1
		END

	RETURN(@SEMESTRE)
END;
GO

SELECT dbo.fn_Semestre(NULL);
GO

--Funções em Constraints
CREATE TABLE EXEMPLO(
	ID INT NOT NULL,
	DATA DATETIME NOT NULL
);
GO


ALTER TABLE EXEMPLO
ADD CONSTRAINT CHK_EXEMPLO_DATA CHECK(dbo.fn_Semestre(DATA) = 1);
GO

INSERT INTO EXEMPLO
SELECT 1, '20150101';
GO

SELECT *
FROM EXEMPLO;
GO

INSERT INTO EXEMPLO
SELECT 1, '20150701';
GO

SELECT *
FROM EXEMPLO;
GO

--Funções em colunas computadas
ALTER TABLE EXEMPLO
ADD Semestre AS dbo.fn_Semestre(DATA);
GO

SELECT * FROM EXEMPLO;
GO

DROP FUNCTION dbo.fn_Semestre;
GO


--Performance: Escalar x Tabular inline x Tabular multi-statement - Aguarde o módulo de tunning :D

```