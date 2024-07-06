# Coluna `SORTKEY` da tabela `pg_table_def`

Na tabela `pg_table_def` do Amazon Redshift, a coluna `sortkey` indica a ordem das colunas na chave de classificação de uma tabela. Essa chave é usada para ordenar os dados físicos da tabela em disco, o que pode ter um impacto significativo no desempenho das consultas.

## Pontos importantes sobre a coluna `sortkey`

* **Valores positivos:** Se a coluna `sortkey` tiver um valor positivo, isso indica que a coluna faz parte da chave de classificação. A ordem do valor positivo indica a posição da coluna na chave. Por exemplo, se a coluna `sortkey` for 1, isso significa que a coluna é a primeira coluna na chave de classificação.
* **Valores intercalados:** Para chaves de classificação compostas, as colunas `sortkey` podem ter valores positivos e negativos alternados. Isso indica que as colunas são intercaladas na chave, o que pode melhorar o desempenho para consultas que envolvem vários campos de classificação.
* **Chave de distribuição:** A coluna `sortkey` não tem relação direta com a chave de distribuição da tabela. A chave de distribuição é definida usando a cláusula `DISTKEY` na instrução `CREATE TABLE`, enquanto a chave de classificação é definida usando a cláusula `SORTKEY`.
* **Benefícios do uso da chave de classificação:** A ordenação dos dados em disco de acordo com a chave de classificação pode otimizar o desempenho de consultas que:
    * Fazem varreduras completas da tabela.
    * Usam a cláusula `ORDER BY` para classificar os resultados da consulta por colunas que fazem parte da chave de classificação.
    * Usam junções que combinam dados de várias tabelas com base em colunas que fazem parte da chave de classificação.

## Exemplo

Considere uma tabela `orders` com as colunas `order_id`, `customer_id` e `order_date`. Se a tabela for definida com a seguinte instrução `CREATE TABLE`:

```sql

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  DISTKEY (customer_id),
  SORTKEY (order_date)
);

```

* A chave de distribuição da tabela será `customer_id`.
* A chave de classificação será `order_date`.
* A coluna `sortkey` terá o valor `1` para `order_date`, indicando que essa é a única coluna na chave de classificação.

Nesse caso, a ordenação dos dados em disco por `order_date` pode melhorar o desempenho de consultas que:

* Selecionam todos os pedidos para um determinado cliente ordenados por data do pedido.
* Une a tabela `orders` com outra tabela com base em `customer_id` e ordena os resultados pela data do pedido.

## Recomendações

* Defina uma chave de classificação para tabelas que serão frequentemente consultadas por colunas específicas.
* Escolha uma chave de classificação que resulte em uma distribuição uniforme dos dados na tabela.
* Evite usar chaves de classificação com muitas colunas, pois isso pode diminuir o desempenho.
* Monitore o desempenho das consultas para garantir que a chave de classificação escolhida esteja proporcionando o efeito desejado.

## Recursos adicionais

* [Documentação do Amazon Redshift sobre PG_TABLE_DEF](https://docs.aws.amazon.com/pt_br/redshift/latest/dg/r_PG_TABLE_DEF.html) 
* Documentação do Amazon Redshift sobre DISTSTYLE, DISTKEY e SORTKEY [URL inválido removido]
* Melhores práticas para dimensionamento e desempenho no Amazon Redshift [URL inválido removido]
