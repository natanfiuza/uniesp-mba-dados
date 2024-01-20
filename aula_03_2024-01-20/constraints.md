## CONSTRAINTS

As restrições no SQL Server são regras predefinidas que você pode impor em colunas únicas ou múltiplas. Essas restrições ajudam a manter a integridade, a confiabilidade e a precisão dos valores armazenados nessas colunas. Você pode criar restrições usando instruções CREATE TABLE ou ALTER Table. Se você usar a instrução ALTER TABLE, o SQL Server verificará os dados da coluna existente antes de criar a restrição.

Se você inserir dados na coluna que atenda aos critérios da regra de restrição, o SQL Server inserirá os dados com êxito. Entretanto, se os dados violarem a restrição, a instrução insert será abortada com uma mensagem de erro.

Por exemplo, considere que você tem uma tabela **[Employees]** que armazena os dados dos funcionários da sua organização, incluindo seu salário. Existem algumas regras básicas quando se trata de valores na coluna salarial.

A coluna não pode ter valores negativos como -10.000 ou -15.000 USD.
Você também deseja especificar o valor máximo do salário. Por exemplo, o salário máximo deve ser inferior a 2.000.000 USD.
Se você inserir um novo registro com uma restrição em vigor, o SQL Server validará o valor em relação às regras definidas.

Valor inserido:

Salário 80.000: Inserido com sucesso

Salário -50.000:  Erro

Exploraremos as seguintes restrições no SQL Server neste artigo.

* NOT NULL
* UNIQUE
* CHECK
* PRIMARY KEY
* FOREIGN KEY
* DEFAULT

### NOT NULL

Por padrão, o SQL Server permite armazenar valores NULL em colunas. Esses valores NULL não representam dados válidos.

Por exemplo, cada funcionário de uma organização deve ter um Emp ID, nome, sexo e endereço. Portanto, você pode especificar uma coluna com restrições NOT NULL para garantir sempre valores válidos.

O script CREATE TABLE abaixo define restrições `NOT NULL` para colunas **[ID]**,**[FirstName]**,**[LastName]**,**[Gender]** e **[Address]**.

```sql

CREATE TABLE Employees
(
    ID INT NOT NULL,
    [FirstName] Varchar(100) NOT NULL,
    [MiddleName] Varchar(50) NULL,
    [LastName] Varchar(100) NOT NULL,
    [Gender] char(1) NOT NULL,
    [Address] Varchar(200) NOT NULL
)

```

Para validar o comportamento das restrições NOT NULL, usamos as seguintes instruções INSERT.

* Inserir valores para todas as colunas (NULL e NOT NULL)  – Inserções com sucesso

```sql

INSERT INTO Employees (ID,[FirstName],[MiddleName],[LastName],[gender],[Address]) VALUES(1,'Raj','','Gupta','M','India')

```

* Inserir valores para colunas com propriedade NOT NULL  – Inserções com sucesso

```sql
INSERT INTO Employees (ID,[FirstName],[LastName],[gender],[Address]) VALUES(2,
'Shyam','Agarwal','M','UK')
```

Ignorar a inserção de valores para a coluna [Sobrenome] com restrições NOT NULL –  Falha +

```sql
INSERT INTO Employees (ID,[FirstName],[gender],[Address]) VALUES(3,'Sneha','F','India')
```
A última instrução INSERT gerou o erro –  Não é possível inserir valores NULL na coluna.
```sql
Msg 515, Level 16, State 2, Line 11
Não é possível inserir o valor NULL na coluna 'LastName', tabela 'mba.dbo.Employees'; a coluna não permite nulos. Falha em INSERT.

```

### UNIQUE constraint

A restrição UNIQUE no SQL Server garante que você não tenha valores duplicados em uma única coluna ou combinação de colunas. Estas colunas devem fazer parte das restrições UNIQUE. O SQL Server cria automaticamente um  índice  quando restrições UNIQUE são definidas. Você pode ter apenas um valor exclusivo na coluna (incluindo NULL).

Por exemplo, crie a **[DemoTable]** com a coluna **[ID]** tendo a restrição UNIQUE.

```sql
CREATE TABLE DemoTable
(
    [ID] INT UNIQUE NOT NULL,
    [EmpName] VARCHAR(50) NOT NULL
)

```

A terceira instrução insert a seguir apresenta um erro porque tenta inserir valores duplicados da constraint `id` unique e o insert João esta usando o mesmo valor 1 para o campo id.

```sql
INSERT INTO DemoTable ([ID],[EmpName]) VALUES (1,'Carlos')
GO
INSERT INTO DemoTable ([ID],[EmpName]) VALUES (2,'Alice')
GO
INSERT INTO DemoTable ([ID],[EmpName]) VALUES (1,'Joao')
GO
```


### CHECK constraint

A restrição CHECK no SQL Server define um intervalo válido de valores que podem ser inseridos em colunas especificadas. Ele avalia cada valor inserido ou modificado e, se for satisfeito, a instrução SQL é concluída com sucesso.

O script SQL a seguir coloca uma restrição para a coluna **[Idade]**. Seu valor deve ser superior a 18 anos.


-----

[Home 🏠](../README.md) | [Indice 📇](README.md)