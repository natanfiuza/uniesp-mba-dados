# Normalização em Banco de Dados

Normalização em banco de dados é o processo de organizar os dados em tabelas e relações de forma a evitar redundância, inconsistência e dependência funcional entre os dados. O objetivo da normalização é tornar o banco de dados mais eficiente, flexível e fácil de manter. A normalização segue uma série de regras chamadas de formas normais, que definem os critérios para que uma tabela esteja bem estruturada. Existem pelo menos cinco formas normais, mas as mais usadas são as três primeiras. Cada forma normal depende da anterior, ou seja, para que uma tabela esteja na segunda forma normal, ela deve estar na primeira forma normal, e assim por diante. A normalização de banco de dados é um conceito importante para quem trabalha com modelagem, projeto e desenvolvimento de sistemas de banco de dados relacionais.

A primeira forma normal (1FN) exige que todos os atributos de uma tabela sejam atômicos, ou seja, indivisíveis e mínimos. Além disso, a tabela deve ter uma chave primária única, que identifica cada registro, e não deve ter colunas repetidas ou variáveis. A primeira forma normal elimina os grupos repetidos de dados e cria tabelas separadas para cada grupo de dados relacionados.

A segunda forma normal (2FN) exige que todos os atributos não primários de uma tabela dependam totalmente da chave primária, ou seja, não haja dependência parcial. A segunda forma normal elimina as redundâncias de dados e cria tabelas separadas para os grupos de dados que se aplicam a vários registros, relacionando-as por meio de chaves estrangeiras.Isso significa que não deve haver **dependências parciais** entre os atributos. Uma dependência parcial ocorre quando um atributo depende apenas de uma parte da chave primária. Por exemplo, considere uma tabela de alunos com as seguintes colunas: **nome**, **curso**, **professor** e **departamento**. Se o atributo **departamento** depender apenas do atributo **curso**, que por sua vez depende da chave primária **nome**, então temos uma dependência parcial. Para remover essa dependência parcial, podemos dividir a tabela em duas tabelas: uma tabela de cursos e professores e outra tabela de professores e departamentos. Dessa forma, a tabela de alunos estará na 2FN. 

A terceira forma normal (3FN) exige que todos os atributos não primários de uma tabela dependam apenas da chave primária, ou seja, não haja dependência transitiva. A terceira forma normal elimina as inconsistências de dados e cria tabelas separadas para os grupos de dados que dependem de outros atributos não primários, relacionando-as por meio de chaves estrangeiras. Ela visa eliminar redundâncias e inconsistências nos dados. Uma tabela está na 3FN se estiver na 2FN e se todos os seus atributos não chave são independentes entre si. Isso significa que não deve haver **dependências transitivas** entre os atributos. Uma dependência transitiva ocorre quando um atributo depende de outro atributo por meio de um terceiro atributo. Por exemplo, considere uma tabela de alunos com as seguintes colunas: **nome**, **curso**, **professor** e **departamento**. Se o atributo **departamento** depender do atributo **professor**, que por sua vez depende do atributo **curso**, então temos uma dependência transitiva. Para remover essa dependência transitiva, podemos dividir a tabela em duas tabelas: uma tabela de cursos e professores e outra tabela de professores e departamentos. Dessa forma, a tabela de alunos estará na 3FN. 

A forma Normal Boyce-Codd (BCNF): Uma tabela está em BCNF se estiver em 3NF, e cada determinante (um conjunto de colunas que determina exclusivamente outras colunas) é uma chave candidata. BCNF é uma forma mais forte de 3NF que aborda anomalias em certas tabelas 3NF. Elimina redundância e possíveis inconsistências devido à sobreposição de chaves candidatas.

A Quarta Forma Normal (4NF): Uma tabela está em 4NF se estiver em BCNF e não houver dependências com valores múltiplos. Isso significa que uma tabela com mais de um atributo independente com vários valores deve ser decomposta em tabelas separadas. 4NF resolve os problemas de redundância de dados e inconsistências relacionadas a dependências de múltiplos valores.

A Quinta Forma Normal (5NF): Uma tabela está na 5NF se estiver na 4NF e as chaves candidatas implicam em todas as dependências de junção. Este formulário decompõe a tabela em tabelas menores para eliminar redundância e melhorar a integridade dos dados nos casos em que os dados são representados de diversas maneiras em tabelas diferentes.

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

## Beneficios

A normalização de banco de dados oferece diversos benefícios, tais como:

1. **Redução de Redundância**: A normalização elimina a repetição desnecessária de dados, o que reduz o espaço de armazenamento e evita a inconsistência dos dados.

2. **Integridade de Dados**: Ao seguir as regras de normalização, a integridade dos dados é mantida e a probabilidade de ocorrerem inconsistências é reduzida.

3. **Melhor Desempenho de Consulta**: Um banco de dados normalizado pode ter um desempenho de consulta melhor, pois as tabelas são organizadas de forma eficiente e as operações são mais eficientes.

4. **Facilidade de Manutenção**: Um banco de dados normalizado é mais fácil de manter e atualizar, já que as informações estão organizadas e relacionadas de maneira lógica.

5. **Flexibilidade e Escalabilidade**: A normalização garante que o banco de dados seja mais flexível e escalável, facilitando a adição de novos dados e a modificação da estrutura do banco de dados.

Em resumo, a normalização de banco de dados é essencial para garantir a integridade, eficiência e flexibilidade dos sistemas de gerenciamento de dados, proporcionando uma série de benefícios importantes para a gestão de dados.

## Desvantagens

Embora a normalização de banco de dados ofereça muitos benefícios, ela também apresenta algumas desvantagens, tais como:

1. **Desempenho**: A normalização pode afetar o desempenho do banco de dados, especialmente em grandes bancos de dados, devido ao aumento do número de tabelas e relações.

2. **Complexidade**: A normalização pode tornar o banco de dados mais complexo e difícil de entender, especialmente para usuários que não estão familiarizados com o modelo relacional.

3. **Custo de Armazenamento**: A normalização pode aumentar o custo de armazenamento, pois pode ser necessário armazenar mais tabelas e relações.

4. **Dificuldade de Modificação**: A normalização pode tornar a modificação do banco de dados mais difícil, pois pode ser necessário modificar várias tabelas e relações.

5. **Requer Análise Detalhada**: A normalização requer uma análise detalhada do banco de dados e pode ser um processo complexo e demorado.

Em resumo, a normalização de banco de dados pode apresentar algumas desvantagens, como o aumento do custo de armazenamento e a complexidade do banco de dados. No entanto, essas desvantagens podem ser minimizadas com um planejamento cuidadoso e uma análise detalhada do banco de dados.

## Manutenção do banco de dados

A normalização de banco de dados afeta positivamente a simplicidade das operações de manutenção. Ao manter um banco de dados normalizado, as operações de atualização e modificação são simplificadas, pois as alterações precisam ser feitas em um único local, evitando a propagação de alterações em várias tabelas. Isso reduz a probabilidade de erros e torna a manutenção do banco de dados mais eficiente e menos propensa a inconsistências. Portanto, a normalização contribui para a integridade e a qualidade dos dados, facilitando as operações de manutenção e garantindo que o banco de dados seja mais fácil de gerenciar e entender.


## Referencias:
1. [Normalização de banco de dados: o que é e como fazer](https://platzi.com.br/blog/normalizacao-de-banco-de-dados/)
2. [Normalização em Banco de Dados - Estrutura | Alura](https://www.alura.com.br/artigos/normalizacao-banco-de-dados-estrutura)
3. [Descrição da normalização do banco de dados - Microsoft 365 Apps](https://learn.microsoft.com/pt-br/office/troubleshoot/access/database-normalization-description)
4. [Normalização de Bancos de Dados: Explicação e Benefícios](https://blogdosql.com.br/normalizacao-de-bancos-de-dados-explicacao-e-beneficios/)
5. [Normalização de Banco de Dados: Por que Organização é Fundamental](https://www.dio.me/articles/normalizacao-de-banco-de-dados-por-que-organizacao-e-fundamental)
6. [Normalização de Bancos de Dados: Explicação e Benefícios](https://blogdosql.com.br/normalizacao-de-bancos-de-dados-explicacao-e-beneficios/)
7. [O que é a normalização de bases de dados e como fazê-la?](https://ebaconline.com.br/blog/normalizacao-de-bases-de-dados)
8. [O que é normalização em um banco de dados, e por que é tão importante?](https://dev.to/gabrielgcj/o-que-e-normalizacao-em-um-banco-de-dados-e-por-que-e-tao-importante-31ni)
9. [Descrição das noções básicas de normalização do banco de dados](https://learn.microsoft.com/pt-br/office/troubleshoot/access/database-normalization-description)
10. [Normalização em bancos de dados relacionais: um mergulho profundo](https://appmaster.io/pt/blog/normalizacao-em-bancos-de-dados-relacionais)
11. [Vantagens e Desvantagens de normalizar um banco de dados](http://ptcomputador.com/Software/database-software/113954.html)
13. [Vantagens e desvantagens de normalizar uma base de dados](https://www.ehow.com.br/vantagens-desvantagens-normalizar-base-dados-info_38217/)

----------

[Home 🏠](../README.md) | [Indice 📇](README.md)
