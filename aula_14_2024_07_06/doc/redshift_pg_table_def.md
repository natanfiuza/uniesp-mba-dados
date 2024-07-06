# A tabela `pg_table_def` 

Revelando o Schema das Tabelas no Amazon Redshift

A tabela de catálogo `pg_table_def` do Amazon Redshift é uma aliada valiosa para desvendar a estrutura das tabelas em seu banco de dados.  Como parte de um conjunto abrangente de tabelas de catálogo, ela oferece uma visão granular das colunas que compõem cada tabela, incluindo detalhes essenciais para o gerenciamento do schema.

Imagine `pg_table_def` como um blueprint detalhado de cada tabela.  Ao consultar essa tabela, você obtém informações cruciais sobre as colunas, tais como:

* **Nome da coluna:** Identificador único para cada coluna dentro da tabela.
* **Tipo de dado:** Define o tipo de informação que a coluna pode armazenar (por exemplo, inteiro, texto, data).
* **Nulidade:** Indica se a coluna permite valores ausentes (NULL).
* **Valor padrão:** Valor predefinido atribuído automaticamente a novas linhas se nenhum valor for especificado durante a inserção.

Além desses detalhes fundamentais, a tabela `pg_table_def` também pode revelar características como restrições e comentários associados às colunas, fornecendo uma compreensão ainda mais abrangente da estrutura da tabela.

Uma limitação importante a ter em mente é a visibilidade do usuário.  A `pg_table_def` somente retorna informações sobre tabelas acessíveis ao usuário que executa a consulta. Isso significa que, se a tabela residir em um schema que não esteja presente em seu `search_path`, ela não será listada nos resultados da consulta. Para garantir que você esteja investigando o schema correto, certifique-se de que o `search_path` esteja configurado adequadamente.

Ao contrário de algumas tabelas de catálogo do Redshift que possuem limitações de acesso devido a tipos de dados não suportados, a `pg_table_def` é totalmente acessível. Isso significa que você pode consultar essa tabela sem se preocupar com restrições de compatibilidade.

## Exemplo: Examinando a Estrutura de uma Tabela

Suponha que você tenha uma tabela chamada `customer` no schema `sales`. Para descobrir as colunas dessa tabela e seus respectivos detalhes, você pode executar a seguinte consulta:

```sql
SELECT column_name, data_type, is_nullable, default_value
FROM pg_table_def
WHERE schemaname = 'sales'
  AND table_name = 'customer';
```

Esta consulta retornará uma lista de colunas, incluindo seus nomes, tipos de dados, se aceitam valores nulos e os valores padrão definidos.

## Conclusão

A tabela `pg_table_def` desempenha um papel crucial na administração do schema do Redshift. Ao consultá-la, você obtém uma visão detalhada da estrutura das tabelas, permitindo um gerenciamento mais eficaz do seu banco de dados.

## Ver também

* [DISTKEY](./redshift_pg_table_def_distkey.md)
* [SORTKEY](./redshift_pg_table_def_sortkey.md)