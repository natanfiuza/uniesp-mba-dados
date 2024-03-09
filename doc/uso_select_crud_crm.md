# O uso do comando `SELECT` em um sistema CRUD de CRM

Em um sistema CRUD (Create, Read, Update, Delete) de CRM (Customer Relationship Management) voltado para clientes, o uso do comando `SELECT` no SQL é crucial para recuperar informações específicas dos clientes armazenadas no banco de dados. 

Aqui estão alguns tópicos que destacam a utilização da seleção de dados com o comando `SELECT` no contexto do desenvolvimento de um sistema CRUD de CRM:

## 1. **Recuperação de Dados Básicos:**
   - Utilize o comando `SELECT` para recuperar informações básicas dos clientes, como nome, endereço, e-mail, telefone, etc.
   - Exemplo: `SELECT Nome, Email, Telefone FROM Clientes;`

## 2. **Filtragem de Dados Específicos:**
   - Aplique a cláusula `WHERE` para filtrar dados com base em critérios específicos, como cliente ativo, tipo de indústria, etc.
   - Exemplo: `SELECT Nome, Email FROM Clientes WHERE Status = 'Ativo';`

## 3. **Ordenação de Resultados:**
   - Utilize a cláusula `ORDER BY` para ordenar os resultados com base em critérios como nome, data de registro, etc.
   - Exemplo: `SELECT Nome, DataRegistro FROM Clientes ORDER BY Nome;`

## 4. **Recuperação de Dados Relacionados:**
   - Use `JOIN` para recuperar dados relacionados de tabelas diferentes, como informações do cliente e histórico de compras.
   - Exemplo: `SELECT Clientes.Nome, Pedidos.Total FROM Clientes JOIN Pedidos ON Clientes.ID = Pedidos.ClienteID;`

## 5. **Agregação de Dados Estatísticos:**
   - Aplique funções de agregação, como `SUM`, `COUNT`, `AVG`, para calcular estatísticas sobre dados relacionados, como o total de compras de um cliente.
   - Exemplo: `SELECT ClienteID, COUNT(*) as NumeroDeCompras FROM Pedidos GROUP BY ClienteID;`

## 6. **Consulta com Junção e Filtros Complexos:**
   - Combine várias condições na cláusula `WHERE` para consultas mais complexas, como clientes ativos com mais de três compras.
   - Exemplo: 
```sql
SELECT 
    Nome, 
    Email 
FROM 
    Clientes 
WHERE 
    Status = 'Ativo' 
    AND (
        SELECT 
            COUNT(*) 			
        FROM 
            Pedidos 
        WHERE 
            cliente_id = Clientes.id
    ) > 2
```
   - Outro exemplo: 
```sql

SELECT 
	Nome,
	Email,
	COUNT(P.id) AS total_pedidos
FROM 
	Clientes 
		LEFT JOIN Pedidos AS P ON P.cliente_id = clientes.id
WHERE  
	Status = 'Ativo' 

GROUP BY 
    clientes.id
HAVING 
    total_pedidos > 2

```
## 7. **Limitação de Resultados:**
   - Utilize `LIMIT` para restringir o número de resultados retornados, o que pode ser útil para paginar grandes conjuntos de dados.
   - Exemplo: `SELECT Nome, Email FROM Clientes LIMIT 10 OFFSET 20;` (Retorna 10 registros, começando do 21º.)

## 8. **Seleção de Colunas Calculadas:**
   - Crie colunas calculadas na consulta para apresentar informações adicionais, como a idade do cliente com base na data de nascimento.
   - Exemplo: `SELECT Nome, DataNascimento, YEAR(GETDATE()) - YEAR(DataNascimento) AS Idade FROM Clientes;`
   - Exemplo usando MySQL:
```sql
SELECT Nome, Email, YEAR(NOW()) - YEAR(DataNascimento) AS Idade  FROM Clientes LIMIT 2 OFFSET 1
```
| Nome  | Email             | Idade |
| ----- | ----------------- | ----: |
| Maria | maria@example.com |    38 |
| Pedro | pedro@example.com |    23 |

## Conclusão

Ao estruturar consultas SQL para um sistema CRUD de CRM, é fundamental garantir que as consultas sejam eficientes e forneçam os dados necessários para as operações de leitura do sistema. Além disso, a compreensão de como utilizar índices, otimizar consultas e escolher as colunas corretas é crucial para garantir um desempenho adequado do sistema.