# Cardinalidade

A cardinalidade em um modelo conceitual de banco de dados é uma forma de expressar quantas instâncias de uma entidade podem se relacionar com quantas instâncias de outra entidade. A cardinalidade pode ser representada graficamente por meio de um diagrama entidade-relacionamento (DER), que mostra as entidades, os atributos e os relacionamentos entre elas.

Existem quatro tipos principais de cardinalidade: um-para-um, um-para-muitos, muitos-para-um e muitos-para-muitos. Cada tipo de cardinalidade tem um símbolo diferente para indicar a quantidade mínima e máxima de instâncias que podem se relacionar. Uma das convenções mais usadas é a chamada "pé de galinha", que usa os seguintes símbolos:

- Um traço (-) indica que a quantidade mínima é um, ou seja, a instância deve se relacionar obrigatoriamente com outra instância.
- Um parêntesis (O) indica que a quantidade mínima é zero, ou seja, a instância pode se relacionar ou não com outra instância.
- Um traço (-) indica que a quantidade máxima é um, ou seja, a instância só pode se relacionar com uma única instância.
- Um pé de galinha (<) indica que a quantidade máxima é muitos, ou seja, a instância pode se relacionar com várias instâncias.

Veja alguns exemplos de como representar cada tipo de cardinalidade em um DER:

- Um-para-um: significa que uma instância de uma entidade só pode se relacionar com uma instância de outra entidade, e vice-versa. Por exemplo, uma pessoa só pode ter um passaporte, e um passaporte só pode pertencer a uma pessoa. Isso seria representado por um traço de ambos os lados do relacionamento, como no exemplo abaixo:

- Um-para-muitos: significa que uma instância de uma entidade pode se relacionar com várias instâncias de outra entidade, mas uma instância da outra entidade só pode se relacionar com uma instância da primeira entidade. Por exemplo, um professor pode lecionar várias disciplinas, mas uma disciplina só pode ser lecionada por um professor. Isso seria representado por um traço de um lado do relacionamento e um pé de galinha do outro lado, como no exemplo abaixo:


- Muitos-para-um: significa que várias instâncias de uma entidade podem se relacionar com uma instância de outra entidade, mas uma instância da outra entidade só pode se relacionar com várias instâncias da primeira entidade. Por exemplo, vários alunos podem cursar uma turma, mas uma turma só pode ter vários alunos. Isso seria representado por um pé de galinha de um lado do relacionamento e um traço do outro lado, como no exemplo abaixo:

- Muitos-para-muitos: significa que várias instâncias de uma entidade podem se relacionar com várias instâncias de outra entidade, e vice-versa. Por exemplo, um livro pode ter vários autores, e um autor pode escrever vários livros. Isso seria representado por um pé de galinha de ambos os lados do relacionamento, como no exemplo abaixo:

Para saber mais sobre a cardinalidade em banco de dados e como representá-la em um DER, você pode consultar os seguintes links:

- [Cardinalidade Banco de Dados: Entenda os Relacionamentos!](^5^)
- [O que é cardinalidade em bancos de dados | Mailchimp]
- [O que é o mapeamento de cardinalidades | Diagramas ER]
- [O que significa cardinalidade no banco de dados? - Você Pergunta]
- [Tipos de relacionamento ou cardinalidade do relacionamento · Banco de ...]

Origem: conversa com o Bing, 16/12/2023
(1) Cardinalidade Banco de Dados: Entenda os Relacionamentos!. https://ehgomes.com.br/modelagem-de-dados/cardinalidade-banco-de-dados-entenda-os-relacionamentos/.
(2) O que é cardinalidade em bancos de dados | Mailchimp. https://mailchimp.com/pt-br/resources/cardinality-meaning/.
(3) O que é o mapeamento de cardinalidades | Diagramas ER. https://acervolima.com/o-que-e-o-mapeamento-de-cardinalidades-diagramas-er/.
(4) O que significa cardinalidade no banco de dados? - Você Pergunta. https://vocepergunta.com/library/artigo/read/409050-o-que-significa-cardinalidade-no-banco-de-dados.
(5) Tipos de relacionamento ou cardinalidade do relacionamento · Banco de .... https://fabiojaniolima.gitbooks.io/banco-de-dados-modelagem-de-dados/content/capitulo-2/2.4-tipos-de-relacionamento-ou-cardinalidade-do-relacionamento.html.



----------
[Home 🏠](../README.md) | [Indice 📇](README.md)