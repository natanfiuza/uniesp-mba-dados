# O uso de JOIN no MySQL

Os joins no MySQL são utilizados para combinar linhas de duas ou mais tabelas com base em uma condição especificada. Vou explicar os tipos mais comuns de joins no MySQL: INNER JOIN, LEFT JOIN, RIGHT JOIN e FULL JOIN.

## Tipos de JOIN

### 1. INNER JOIN:

O INNER JOIN retorna apenas as linhas que têm correspondência em ambas as tabelas.

**Exemplo:**
```sql
SELECT customers.id, customers.name, orders.order_number
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id;
```

- **Documentação:**
   - [INNER JOIN](https://dev.mysql.com/doc/refman/8.0/en/join.html)

### 2. LEFT JOIN (ou LEFT OUTER JOIN):

O LEFT JOIN retorna todas as linhas da tabela à esquerda e as linhas correspondentes da tabela à direita. Se não houver correspondência, as colunas da tabela à direita conterão NULL.

**Exemplo:**
```sql
SELECT customers.id, customers.name, orders.order_number
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;
```

- **Documentação:**
   - [LEFT JOIN](https://dev.mysql.com/doc/refman/8.0/en/join.html)

### 3. RIGHT JOIN (ou RIGHT OUTER JOIN):

O RIGHT JOIN é o oposto do LEFT JOIN. Ele retorna todas as linhas da tabela à direita e as linhas correspondentes da tabela à esquerda. Se não houver correspondência, as colunas da tabela à esquerda conterão NULL.

**Exemplo:**
```sql
SELECT customers.id, customers.name, orders.order_number
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id;
```

- **Documentação:**
   - [RIGHT JOIN](https://dev.mysql.com/doc/refman/8.0/en/join.html)

### 4. FULL JOIN (ou FULL OUTER JOIN):

O FULL JOIN retorna todas as linhas quando há uma correspondência em uma das tabelas. Se não houver correspondência, as colunas sem correspondência conterão NULL.

**Exemplo:**
```sql
SELECT customers.id, customers.name, orders.order_number
FROM customers
FULL JOIN orders ON customers.id = orders.customer_id;
```

- **Documentação:**
   - [FULL JOIN](https://dev.mysql.com/doc/refman/8.0/en/join.html)

Estes são os tipos básicos de joins no MySQL. Vale a pena explorar a documentação oficial para obter informações mais detalhadas e exemplos adicionais.

## Uso de ALIAS e condicionais AND e OR a clausula ON

No MySQL, ao usar a cláusula `JOIN`, você pode adicionar condições `AND` ou `OR` à cláusula `ON` para especificar critérios adicionais para a junção. Além disso, o uso de alias para tabelas pode tornar a consulta mais legível. Aqui está um exemplo:

Suponha que temos duas tabelas, `customers` e `orders`, e queremos combinar registros onde o ID do cliente é igual ao ID do cliente na tabela `orders` e a quantidade do pedido é maior que 100.

**Exemplo com ALIAS:**
```sql
SELECT c.id AS customer_id, c.name AS customer_name, o.order_number, o.amount
FROM customers AS c
JOIN orders AS o ON c.id = o.customer_id AND o.amount > 100;
```

Neste exemplo:

- `c` e `o` são alias para as tabelas `customers` e `orders`, respectivamente.
- `c.id = o.customer_id` especifica a condição de junção principal.
- `o.amount > 100` é uma condição adicional usando `AND` na cláusula `ON`.

Você também pode usar `OR` para adicionar condições alternativas. Vamos dizer que queremos incluir pedidos com uma quantidade igual a 50:

```sql
SELECT c.id AS customer_id, c.name AS customer_name, o.order_number, o.amount
FROM customers AS c
JOIN orders AS o ON c.id = o.customer_id AND (o.amount > 100 OR o.amount = 50);
```

Neste exemplo, a condição `(o.amount > 100 OR o.amount = 50)` usa `OR` para incluir pedidos com quantidade superior a 100 ou quantidade igual a 50.

Essas condições adicionais ajudam a refinar as junções e a obter resultados mais específicos com base nos critérios desejados. Certifique-se de ajustar as condições de acordo com os requisitos específicos do seu caso de uso.