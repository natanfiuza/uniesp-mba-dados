# Normalização em Banco de Dados

Normalização em banco de dados é o processo de organizar os dados em tabelas e relações de forma a evitar redundância, inconsistência e dependência funcional entre os dados. O objetivo da normalização é tornar o banco de dados mais eficiente, flexível e fácil de manter. A normalização segue uma série de regras chamadas de formas normais, que definem os critérios para que uma tabela esteja bem estruturada. Existem pelo menos cinco formas normais, mas as mais usadas são as três primeiras. Cada forma normal depende da anterior, ou seja, para que uma tabela esteja na segunda forma normal, ela deve estar na primeira forma normal, e assim por diante. A normalização de banco de dados é um conceito importante para quem trabalha com modelagem, projeto e desenvolvimento de sistemas de banco de dados relacionais¹².

A primeira forma normal (1FN) exige que todos os atributos de uma tabela sejam atômicos, ou seja, indivisíveis e mínimos. Além disso, a tabela deve ter uma chave primária única, que identifica cada registro, e não deve ter colunas repetidas ou variáveis. A primeira forma normal elimina os grupos repetidos de dados e cria tabelas separadas para cada grupo de dados relacionados¹².

A segunda forma normal (2FN) exige que todos os atributos não primários de uma tabela dependam totalmente da chave primária, ou seja, não haja dependência parcial. A segunda forma normal elimina as redundâncias de dados e cria tabelas separadas para os grupos de dados que se aplicam a vários registros, relacionando-as por meio de chaves estrangeiras¹².

A terceira forma normal (3FN) exige que todos os atributos não primários de uma tabela dependam apenas da chave primária, ou seja, não haja dependência transitiva. A terceira forma normal elimina as inconsistências de dados e cria tabelas separadas para os grupos de dados que dependem de outros atributos não primários, relacionando-as por meio de chaves estrangeiras¹².

Para ilustrar o processo de normalização, vamos usar um exemplo de uma tabela que armazena dados sobre pedidos de clientes de uma loja online. A tabela original é a seguinte:

| Número do pedido | Data do pedido | CPF do cliente | Nome do cliente | Endereço do cliente | Código do produto | Nome do produto | Quantidade | Preço unitário | Preço total |
|------------------|----------------|----------------|-----------------|---------------------|-------------------|-----------------|------------|----------------|-------------|
| 1001             | 01/01/2023    | 123.456.789-00 | Ana             | Rua A, 10, Centro   | P001              | Camiseta        | 2          | 50,00          | 100,00      |
| 1002             | 02/01/2023    | 234.567.890-11 | Bruno           | Rua B, 20, Bairro   | P002              | Calça           | 1          | 80,00          | 80,00       |
| 1003             | 03/01/2023    | 123.456.789-00 | Ana             | Rua A, 10, Centro   | P003              | Jaqueta         | 1          | 120,00         | 120,00      |
| 1004             | 04/01/2023    | 345.678.901-22 | Carlos          | Rua C, 30, Zona     | P001              | Camiseta        | 3          | 50,00          | 150,00      |
| 1005             | 05/01/2023    | 234.567.890-11 | Bruno           | Rua B, 20, Bairro   | P004              | Tênis           | 1          | 200,00         | 200,00      |

Essa tabela não está normalizada, pois apresenta vários problemas, como:

- Repetição de dados sobre os clientes e os produtos em vários registros;
- Dependência parcial dos atributos nome do cliente, endereço do cliente, nome do produto e preço unitário em relação à chave primária composta por número do pedido e código do produto;
- Dependência transitiva do atributo preço total em relação aos atributos quantidade e preço unitário;
- Possibilidade de inconsistência ou perda de dados se houver alteração ou exclusão de algum registro.

Para normalizar essa tabela, devemos aplicar as regras das formas normais. Começando pela primeira forma normal, devemos eliminar os grupos repetidos de dados e criar tabelas separadas para cada grupo de dados relacionados. Assim, teremos as seguintes tabelas:

| Número do pedido | Data do pedido | CPF do cliente |
|------------------|----------------|----------------|
| 1001             | 01/01/2023    | 123.456.789-00 |
| 1002             | 02/01/2023    | 234.567.890-11 |
| 1003             | 03/01/2023    | 123.456.789-00 |
| 1004             | 04/01/2023    | 345.678.901-22 |
| 1005             | 05/01/2023    | 234.567.890-11 |

| CPF do cliente | Nome do cliente | Endereço do cliente |
|----------------|-----------------|---------------------|
| 123.456.789-00 | Ana             | Rua A, 10, Centro   |
| 234.567.890-11 | Bruno           | Rua B, 20, Bairro   |
| 345.678.901-22 | Carlos          | Rua C, 30, Zona     |

| Código do produto | Nome do produto | Preço unitário |
|-------------------|-----------------|----------------|
| P001              | Camiseta        | 50,00          |
| P002              | Calça           | 80,00          |
| P003              | Jaqueta         | 120,00         |
| P004              | Tênis           | 200,00         |

| Número do pedido* | Código do produto* | Quantidade | Preço total |
|------------------|-------------------|------------|-------------|
| 1001             | P001              | 2          | 100,00      |
| 1002             | P002              | 1          | 80,00       |
| 1003             | P003              | 1          | 120,00      |
| 1004             | P001              | 3          | 150,00      |
| 1005             | P004              | 1          | 200,00      |

Nessas tabelas, cada atributo é atômico e mínimo, e cada tabela tem uma chave primária única, que é sublinhada. Além disso, não há colunas repetidas ou variáveis. As tabelas estão relacionadas por meio de chaves estrangeiras, que são indicadas por asteriscos. Assim, concluímos a primeira forma normal.

Passando para a segunda forma normal, devemos eliminar as dependências parciais dos atributos não primários em relação à chave primária. Nesse caso, a única tabela que tem uma chave primária composta é a última, que relaciona os pedidos com os produtos. Os atributos preço total e quantidade dependem totalmente da chave primária, mas os atributos nome do produto e preço unitário dependem apenas do código do produto, que é parte da chave primária. Portanto, devemos separar esses atributos em outra tabela, ficando assim:

| Número do pedido* | Código do produto* | `Quantidade` | `Preço total` |
|------------------|-------------------|------------|-------------|
| 1001             | P001              | 2          | 100,00      |
| 1002             | P002              | 1          | 80,00       |
| 1003             | P003              | 1          | 120,00      |
| 1004             | P001              | 3          | 150,00      |
| 1005             | P004              | 1          | 200,00      |

| Código do produto | `Nome do produto` | `Preço unitário` |
|-------------------|-----------------|----------------|
| P001              | Camiseta        | 50,00          |
| P002              | Calça           | 80,00          |
| P003              | Jaqueta         | 120,00         |
| P004              | Tênis           | 200,00         |

Nessas tabelas, todos os atributos não primários dependem totalmente da chave primária, que estão em destaque. As tabelas estão relacionadas por meio de chaves estrangeiras, que são indicadas por asteriscos. Assim, concluímos a segunda forma normal.

Finalmente, para a terceira forma normal, devemos eliminar as dependências transitivas dos atributos não primários

Referencias:
1. [Normalização de banco de dados: o que é e como fazer](https://platzi.com.br/blog/normalizacao-de-banco-de-dados/)
2. [Normalização em Banco de Dados - Estrutura | Alura](https://www.alura.com.br/artigos/normalizacao-banco-de-dados-estrutura)
3. [Descrição da normalização do banco de dados - Microsoft 365 Apps](https://learn.microsoft.com/pt-br/office/troubleshoot/access/database-normalization-description)
4. [Normalização de Bancos de Dados: Explicação e Benefícios](https://blogdosql.com.br/normalizacao-de-bancos-de-dados-explicacao-e-beneficios/)


----------

[Home](../README.md) | [Indice](README.md)