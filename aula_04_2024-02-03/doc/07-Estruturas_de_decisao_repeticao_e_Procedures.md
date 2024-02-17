# Estrutura de decisão e repetição e Procedures


## IF... ELSE

Impõe condições na execução de uma instrução Transact-SQL. A instrução Transact-SQL que aparece depois de uma palavra-chave IF e a condição dela será executada se a condição for satisfeita: a expressão booliana retorna TRUE. A palavra-chave opcional `ELSE` introduz outra instrução Transact-SQL que será executada quando a condição IF não for atendida: a expressão booliana retorna `FALSE`.

Veja: [Convenções de sintaxe de Transact-SQL](https://learn.microsoft.com/pt-br/sql/t-sql/language-elements/transact-sql-syntax-conventions-transact-sql?view=sql-server-ver16)

Sintaxe:

```sql

IF Boolean_expression   
     { sql_statement | statement_block }   
[ ELSE   
     { sql_statement | statement_block } ]   

```
### Argumentos

*`Boolean_expression`*

É uma expression que retorna `TRUE` ou `FALSE`. Se a expressão booliana contiver uma instrução `SELECT`, a instrução `SELECT` deverá ser incluída entre parênteses.

*`{ sql_statement| statement_block }`*

É qualquer instrução ou agrupamento de instruções Transact-SQL, conforme definido por meio de um bloco de instruções. A menos que um bloco de instruções seja usado, a condição `IF` ou `ELSE` poderá afetar o desempenho de somente uma instrução Transact-SQL.

Para definir um bloco de instruções, use as palavras-chave `BEGIN` e `END` de controle de fluxo.

### Comentários

Uma construção `IF...ELSE` pode ser usada em lotes, em procedimentos armazenados e em consultas ad hoc. Quando essa construção é usada em um procedimento armazenado, ela normalmente é usada para testar a existência de algum parâmetro.

Os testes `IF` podem ser aninhados depois de outro `IF` ou seguindo um `ELSE`. O limite do número de níveis aninhados depende da memória disponível.

Exemplo:

```sql

IF DATENAME(weekday, GETDATE()) IN (N'Saturday', N'Sunday')
       SELECT 'Weekend';
ELSE 
       SELECT 'Weekday';

```
> Para obter mais exemplos, confira [ELSE (IF...ELSE) (Transact-SQL)](https://learn.microsoft.com/pt-br/sql/t-sql/language-elements/else-if-else-transact-sql?view=sql-server-ver16).

## WHILE

Define uma condição para a execução repetida de uma instrução ou um bloco de instruções SQL. As instruções serão executadas repetidamente desde que a condição especificada seja verdadeira. A execução de instruções no loop `WHILE` pode ser controlada internamente ao loop com as palavras-chave `BREAK` e `CONTINUE`.

[Convenções de sintaxe de Transact-SQL](https://learn.microsoft.com/pt-br/sql/t-sql/language-elements/transact-sql-syntax-conventions-transact-sql?view=sql-server-ver16)

Sintaxe:

```sql

-- Syntax for SQL Server and Azure SQL Database and Microsoft Fabric
  
WHILE Boolean_expression   
     { sql_statement | statement_block | BREAK | CONTINUE }  

-- Syntax for Azure Azure Synapse Analytics and Parallel Data Warehouse  
  
WHILE Boolean_expression   
     { sql_statement | statement_block | BREAK }  


```
```
ℹ️ Observação

Para exibir a sintaxe do Transact-SQL para o SQL 
Server 2014 (12.x) e versões anteriores, confira 
a [Documentação das versões anteriores](https://learn.microsoft.com/pt-br/sql/sql-server/previous-versions-sql-server?view=sql-server-ver16#offline-documentation).

```
### Argumentos

*`Boolean_expression`*
É uma expression que retorna `TRUE` ou `FALSE`. Se a expressão booliana contiver uma instrução `SELECT`, a instrução `SELECT` deverá ser incluída entre parênteses.

*`{sql_statement | statement_block}`*
É qualquer instrução Transact-SQL ou agrupamento de instruções, conforme definido com um bloco de instruções. Para definir um bloco de instruções, use as palavras-chave `BEGIN` e `END` de controle de fluxo.

*`BREAK`*
Provoca uma saída do loop `WHILE` mais interno. Todas as instruções que apareçam depois da palavra-chave `END`, que marca o final do loop, serão executadas.

*`CONTINUE`*
Faz com que o loop `WHILE` seja reiniciado, ignorando todas as instruções depois da palavra-chave `CONTINUE`.

### Comentários

Se dois ou mais loops `WHILE` estiverem aninhados, o `BREAK` interno será encerrado para o próximo loop mais externo. Todas as instruções após o fim da primeira execução do loop interno e o loop mais externo seguinte serão reiniciadas.

## Exemplos 

### a. Usando BREAK e CONTINUE com IF...ELSE e WHILE aninhados

No exemplo a seguir, se o preço médio de tabela de um produto for menor que `$300`, o loop `WHILE` dobrará os preços e selecionará o preço máximo. Se o preço máximo for menor ou igual a `$500`, o loop `WHILE` será reiniciado e dobrará novamente os preços. Esse loop continuará dobrando os preços até que o preço máximo seja maior que `$500`; em seguida, sairá do loop `WHILE` e imprimirá uma mensagem.

```sql
USE AdventureWorks2022;  
GO  
WHILE (SELECT AVG(ListPrice) FROM Production.Product) < $300  
BEGIN  
   UPDATE Production.Product  
      SET ListPrice = ListPrice * 2  
   SELECT MAX(ListPrice) FROM Production.Product  
   IF (SELECT MAX(ListPrice) FROM Production.Product) > $500  
      BREAK  
   ELSE  
      CONTINUE  
END  
PRINT 'Too much for the market to bear';  

```
### B. Usando WHILE em um cursor

O exemplo a seguir usa `@@FETCH_STATUS` para controlar atividades de cursor em um loop `WHILE`.

```sql

DECLARE @EmployeeID as NVARCHAR(256)
DECLARE @Title as NVARCHAR(50)

DECLARE Employee_Cursor CURSOR FOR  
SELECT LoginID, JobTitle   
FROM AdventureWorks2022.HumanResources.Employee  
WHERE JobTitle = 'Marketing Specialist';  
OPEN Employee_Cursor;  
FETCH NEXT FROM Employee_Cursor INTO @EmployeeID, @Title;  
WHILE @@FETCH_STATUS = 0  
   BEGIN  
      Print '   ' + @EmployeeID + '      '+  @Title 
      FETCH NEXT FROM Employee_Cursor INTO @EmployeeID, @Title;  
   END;  
CLOSE Employee_Cursor;  
DEALLOCATE Employee_Cursor;  
GO 

```
## Procedure

Cria um procedimento armazenado de Transact-SQL ou CLR (Common Language Runtime) no SQL Server, no Banco de Dados SQL do Azure e no Analytics Platform System (PDW). Procedimentos armazenados são semelhantes a procedimentos em outras linguagens de programação no sentido de que podem:

- Aceitar parâmetros de entrada e retornar vários valores no formulário de parâmetros de saída para o procedimento de chamada ou lote.
- Conter instruções de programação que executam operações no banco de dados, inclusive chamar outros procedimentos.
- Retornar um valor de status a um procedimento de chamada ou lote para indicar êxito ou falha (e o motivo da falha).

Use esta instrução para criar um procedimento permanente no banco de dados atual ou um procedimento temporário no banco de dados `tempdb`.

### Sintaxe

Sintaxe Transact-SQL para procedimentos armazenados no SQL Server e no Banco de Dados SQL do Azure:

```sql

CREATE [ OR ALTER ] { PROC | PROCEDURE }
    [schema_name.] procedure_name [ ; number ]
    [ { @parameter_name [ type_schema_name. ] data_type }
        [ VARYING ] [ NULL ] [ = default ] [ OUT | OUTPUT | [READONLY]
    ] [ ,...n ]
[ WITH <procedure_option> [ ,...n ] ]
[ FOR REPLICATION ]
AS { [ BEGIN ] sql_statement [;] [ ...n ] [ END ] }
[;]

<procedure_option> ::=
    [ ENCRYPTION ]
    [ RECOMPILE ]
    [ EXECUTE AS Clause ]


```
Sintaxe Transact-SQL para procedimentos armazenados CLR:

```sql

CREATE [ OR ALTER ] { PROC | PROCEDURE }
    [schema_name.] procedure_name [ ; number ]
    [ { @parameter_name [ type_schema_name. ] data_type }
        [ = default ] [ OUT | OUTPUT ] [READONLY]
    ] [ ,...n ]
[ WITH EXECUTE AS Clause ]
AS { EXTERNAL NAME assembly_name.class_name.method_name }
[;]


```
Sintaxe Transact-SQL para procedimentos armazenados nativamente compilados:

```sql

CREATE [ OR ALTER ] { PROC | PROCEDURE } [schema_name.] procedure_name
    [ { @parameter data_type } [ NULL | NOT NULL ] [ = default ]
        [ OUT | OUTPUT ] [READONLY]
    ] [ ,... n ]
  WITH NATIVE_COMPILATION, SCHEMABINDING [ , EXECUTE AS clause ]
AS
{
  BEGIN ATOMIC WITH ( <set_option> [ ,... n ] )
sql_statement [;] [ ... n ]
[ END ]
}
[;]

<set_option> ::=
    LANGUAGE = [ N ] 'language'
  | TRANSACTION ISOLATION LEVEL = { SNAPSHOT | REPEATABLE READ | SERIALIZABLE }
  | [ DATEFIRST = number ]
  | [ DATEFORMAT = format ]
  | [ DELAYED_DURABILITY = { OFF | ON } ]

```
Veja os [Argumentos aqui](https://learn.microsoft.com/pt-br/sql/t-sql/statements/create-procedure-transact-sql?view=sql-server-ver16#arguments)


----

## Querys usadas na aula

```sql

USE DISCIPLINA02
GO

--ESTRUTURA DE DECISÃO
DECLARE @BIT BIT
SET @BIT = -1;
select @bit

IF @BIT = 1
	PRINT 'POSITIVO'
ELSE
	PRINT 'NEGATIVO';
GO


--ESTRUTURAS DE REPETIÇÃO
DECLARE @CONTADOR TINYINT, @FIM TINYINT
SELECT @CONTADOR = 1, @FIM = 5;
WHILE @CONTADOR <= @FIM
BEGIN
	PRINT @CONTADOR;

	SET @CONTADOR+=1;
END;
GO

--CRIE UMA PROCEDURE QUE LISTE O NOME E O VALOR DOS 10 PRODUTOS MAIS CAROS
CREATE PROCEDURE USP_LISTA_10_MAIS_CAROS
AS
BEGIN
	SET NOCOUNT ON;  --EVITA O RETORNO DE "(N row(s) affected)"

	SELECT TOP 10 PRODUTO, VALOR
	FROM PRODUTOS
	ORDER BY VALOR DESC;
END;
GO

EXEC USP_LISTA_10_MAIS_CAROS;
GO


--CRIE UMA PROCEDURE QUE AUMENTE EM 5% O VALOR DE TODOS OS PRODUTOS
drop PROCEDURE USP_AUMENTA_EM_5_PORCENTO_VAL_PRODUTOS
AS
BEGIN
	SET NOCOUNT ON;

	UPDATE PRODUTOS
	SET VALOR = VALOR * 1.05;
END;
GO

EXEC USP_AUMENTA_EM_5_PORCENTO_VAL_PRODUTOS;
GO

--CRIE UMA PROCEDURE QUE LISTE OS 10 PRODUTOS MAIS VENDIDOS E A RESPECTIVA QUANTIDADE DE VENDAS DE CADA UM
CREATE PROCEDURE USP_LISTA_10_PRODUTOS_MAIS_VENDIDOS
AS
BEGIN

	SET NOCOUNT ON;

	SELECT TOP 10 P.IDPRODUTO, COUNT(*) AS QTDE
	FROM PRODUTOS P
	INNER JOIN ITENS_VENDAS IV ON (P.IDPRODUTO = IV.IDPRODUTO)
	GROUP BY P.IDPRODUTO
	ORDER BY COUNT(*) DESC;

END;
GO

EXEC USP_LISTA_10_PRODUTOS_MAIS_VENDIDOS;
GO


--CRIE UMA PROCEDURE QUE RECEBA UM PARÂMETRO INTEIRO N E QUE LISTE OS N PRODUTOS MAIS CAROS
CREATE PROCEDURE USP_N_PRODUTOS_MAIS_CAROS(@N SMALLINT)
AS
BEGIN

	SET NOCOUNT ON;

	SELECT TOP(@N) PRODUTO, VALOR
	FROM PRODUTOS
	ORDER BY VALOR DESC;
END;
GO

EXEC USP_N_PRODUTOS_MAIS_CAROS 10;
GO

EXEC USP_N_PRODUTOS_MAIS_CAROS @N = 5;
GO

--CRIE UMA PROCEDURE QUE RECEBA O ID DE UM PRODUTO E UMA PORCENTAGEM INTEIRA PARA ATUALIZAR O VALOR DESSE PRODUTO
CREATE PROCEDURE USP_ATUALIZA_VALOR_PRODUTO(@ID INT, @PERCENT TINYINT)
AS
BEGIN
	SET NOCOUNT ON;

	UPDATE PRODUTOS
	SET VALOR = VALOR + ((VALOR * @PERCENT)/100)
	WHERE IDPRODUTO = @ID;
END;
GO

SELECT *
FROM PRODUTOS
WHERE IDPRODUTO = 10;
GO

EXEC USP_ATUALIZA_VALOR_PRODUTO @ID = 10, @PERCENT = 1;
GO

SELECT *
FROM PRODUTOS
WHERE IDPRODUTO = 10;
GO

EXEC USP_ATUALIZA_VALOR_PRODUTO 10, 1;
GO

SELECT *
FROM PRODUTOS
WHERE IDPRODUTO = 10;
GO

--CRIE UMA PROCEDURE COM O CÓDIGO CRIPTOGRAFADO
CREATE PROCEDURE UPS_CRIPTOGRAFADA
WITH ENCRYPTION
AS
BEGIN
	SET NOCOUNT ON;

	SELECT 1;
END;
GO

EXEC UPS_CRIPTOGRAFADA;
GO

EXEC sp_helptext 'dbo.UPS_CRIPTOGRAFADA';
GO




------EXEMPLOS "EXTRAS"

--CRIE UMA PROCEDURE QUE RECEBA UM VALOR LIMITE E QUE LISTE TODOS OS PRODUTOS (NOME E VALOR) ABAIXO DESSE LIMITE DE VALOR
CREATE PROCEDURE dbo.USP_PRODUTO_ABAIXO_DE_VALOR
      @Limite Numeric(6,2) 
    , @Valor Numeric(6,2) OUTPUT
    , @Produto VARCHAR(100) OUT
AS
BEGIN
    SET NOCOUNT ON;

	SELECT @VALOR = VALOR, @PRODUTO = PRODUTO  --COMO ESTOU JOGANDO O RESULTADO DENTRO DE VARIÁVEIS, APENAS O -PRIMEIRO- REGISTRO SERÁ OBTIDO
	FROM PRODUTOS
	WHERE VALOR < @Limite
	ORDER BY VALOR DESC;

END;
GO

DECLARE @VALOR NUMERIC(6,2), @PRODUTO VARCHAR(100);
EXEC USP_PRODUTO_ABAIXO_DE_VALOR 10, @VALOR OUTPUT, @PRODUTO OUTPUT;
SELECT @VALOR, @PRODUTO;


--CRIE UMA PROCEDURE QUE AUMENTE EM 5% O VALOR DE TODOS OS PRODUTOS, COM TRATAMENTO DE ERROS
CREATE PROCEDURE USP_AUMENTA_EM_5_PORCENTO_VAL_PRODUTOS_COM_TRATAMENTO_ERROS
AS
BEGIN
	SET NOCOUNT ON;

	BEGIN TRY
		UPDATE PRODUTOS
		SET VALOR = VALOR * 1.05;
	END TRY
	BEGIN CATCH

	  IF @@TRANCOUNT > 0
		 ROLLBACK

		DECLARE @ErrorMessage nvarchar(4000),  @ErrorSeverity int;
		SELECT @ErrorMessage = 'O erro foi: ' + ERROR_MESSAGE(), @ErrorSeverity = ERROR_SEVERITY();
		RAISERROR(@ErrorMessage, @ErrorSeverity, 1);

	END CATCH;
END;
GO

EXEC USP_AUMENTA_EM_5_PORCENTO_VAL_PRODUTOS_COM_TRATAMENTO_ERROS;
GO



CREATE PROCEDURE dbo.USP_PRODUTO_ABAIXO_DE_VALOR_COM_TRATAMENTO_DE_ERROS
      @Limite Numeric(6,2) 
    , @Valor Numeric(6,2) OUTPUT
    , @Produto VARCHAR(100) OUT
AS
BEGIN
    SET NOCOUNT ON;

	IF @Limite < 0  --SE A VARIÁVEL @LIMITE TIVER VALOR MENOR QUE 0
		THROW 51000, 'VALOR ABAIXO DE 0!',1;  --VAI GERAR UMA MENSAGEM DE ERRO, SIMILAR AO QUE FAZ O RAISERROR

	BEGIN TRY

		SELECT @VALOR = VALOR, @PRODUTO = PRODUTO  --COMO ESTOU JOGANDO O RESULTADO DENTRO DE VARIÁVEIS, APENAS O -PRIMEIRO- REGISTRO SERÁ OBTIDO
		FROM PRODUTOS
		WHERE VALOR < @Limite
		ORDER BY VALOR DESC;
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
			ROLLBACK;
	END CATCH
END;
GO

DECLARE @VALOR NUMERIC(6,2), @PRODUTO VARCHAR(100);
EXEC USP_PRODUTO_ABAIXO_DE_VALOR_COM_TRATAMENTO_DE_ERROS -1, @VALOR OUTPUT, @PRODUTO OUTPUT;
GO

```