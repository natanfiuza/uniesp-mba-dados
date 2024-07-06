# O que e um `DISTSTYLE`

No Amazon Redshift, o `DISTSTYLE` de uma tabela define como os dados da tabela são distribuídos entre os nós de computação do cluster. Isso pode ter um impacto significativo no desempenho das consultas, especialmente para consultas que envolvem grandes conjuntos de dados.

Existem três estilos de distribuição principais no Redshift:

* **KEY:** Neste estilo, os dados são distribuídos uniformemente entre os nós de computação com base em uma coluna específica (chamada de chave de distribuição). Isso é útil para consultas que filtram ou agregam dados por essa coluna.
* **ALL:** Neste estilo, todos os dados são armazenados em todos os nós de computação. Isso pode ser útil para consultas que acessam aleatoriamente qualquer parte dos dados, mas geralmente não é recomendado para grandes conjuntos de dados, pois pode resultar em pontos de acesso e gargalos.
* **EVEN:** Neste estilo, os dados são distribuídos uniformemente entre os nós de computação sem usar uma chave de distribuição específica. Isso pode ser útil para consultas que não têm um padrão de acesso claro, mas geralmente é menos eficiente do que usar o estilo `KEY` com uma chave de distribuição bem escolhida.

A escolha do estilo de distribuição correto para uma tabela depende de vários fatores, como o padrão de acesso aos dados, o tamanho da tabela e o tipo de consultas que serão executadas na tabela. É importante avaliar cuidadosamente esses fatores antes de escolher um estilo de distribuição.

A tabela `pg_table_def` no Redshift armazena informações sobre as tabelas no banco de dados, incluindo o estilo de distribuição de cada tabela. Você pode consultar essa tabela para ver o estilo de distribuição de qualquer tabela no seu cluster.

Aqui está um exemplo de como consultar a tabela `pg_table_def` para ver o estilo de distribuição da tabela `mytable`:

```sql
SELECT diststyle
FROM pg_table_def
WHERE tablename = 'mytable';
```

Este consulta retornará um dos seguintes valores:

* `KEY` se a tabela for distribuída por uma chave
* `ALL` se a tabela for distribuída para todos os nós
* `EVEN` se a tabela for distribuída uniformemente sem uma chave

Você também pode usar a instrução `CREATE TABLE` para especificar o estilo de distribuição de uma nova tabela. Por exemplo, o seguinte comando cria uma tabela chamada `mytable` que é distribuída por uma coluna chamada `customer_id`:

```sql
CREATE TABLE mytable (
  customer_id int DISTKEY,
  name varchar(255),
  email varchar(255)
);
```

## Veja também 

- [Distribution styles](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html)


