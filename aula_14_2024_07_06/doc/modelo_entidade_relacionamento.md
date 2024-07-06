# O Modelo de Entidade-Relacionamento (ER)

O **Modelo de Entidade-Relacionamento (ER)**, proposto por Peter Chen em 1976, é uma ferramenta fundamental para a modelagem conceitual de bancos de dados. Ele fornece uma maneira abstrata e visual de representar os elementos básicos de um sistema de informação, facilitando a comunicação entre os stakeholders e a identificação de falhas na modelagem.

## Componentes principais do Modelo ER

* **Entidades** 

    Representam objetos ou conceitos do mundo real que possuem uma existência independente e podem ser distinguidos de outros objetos. São geralmente representadas por retângulos nos diagramas ER. Exemplos de entidades incluem clientes, produtos, pedidos e departamentos.

* **Atributos** 

    Descrevem as características ou propriedades das entidades. Cada entidade possui um conjunto de atributos que a definem e diferenciam de outras entidades. Os atributos são representados por ovais dentro dos retângulos das entidades nos diagramas ER. Exemplos de atributos incluem nome, endereço, preço, data e hora.

* **Relacionamentos** 

    Representam as associações entre as entidades. Eles definem como as entidades se conectam e interagem entre si. Os relacionamentos são geralmente representados por diamantes nos diagramas ER. Exemplos de relacionamentos incluem "um cliente compra vários produtos", "um departamento possui vários funcionários" e "um pedido possui vários itens".

## Tipos de Relacionamentos

* **1:1** 
    
    Uma entidade está associada a no máximo uma instância de outra entidade. Exemplo: Um professor tem no máximo um orientador.

* **1:N** 
    
    Uma entidade está associada a zero ou mais instâncias de outra entidade. Exemplo: Um professor pode ter zero ou mais alunos.

* **N:N** 
    
    Uma entidade está associada a zero ou mais instâncias de outra entidade, e vice-versa. Exemplo: Um aluno pode ter zero ou mais professores, e um professor pode ter zero ou mais alunos.

## Cardinalidade

A cardinalidade define o número máximo de instâncias de uma entidade que podem se relacionar com uma instância de outra entidade em um relacionamento. Ela é representada por números nos diagramas ER.

## Chaves

Uma chave primária é um atributo ou conjunto de atributos que identifica unicamente uma instância de uma entidade. Uma chave estrangeira é um atributo ou conjunto de atributos em uma entidade que faz referência à chave primária de outra entidade.

Veja [Chave Natural](./chave_natural.md)

Veja [Chave substituta](./chave_substituta.md)

## Diagramas de Entidade-Relacionamento (DER)

Os DERs são representações gráficas do modelo ER. Eles utilizam símbolos padronizados para representar entidades, atributos, relacionamentos e cardinalidade. Os DERs são ferramentas valiosas para comunicar e analisar a estrutura de um sistema de informação.

Veja também 

## Aplicações do Modelo ER

O modelo ER é amplamente utilizado em diversas áreas, incluindo:

* **Projeto de bancos de dados** 

    O modelo ER serve como base para o projeto de bancos de dados relacionais, ajudando a definir a estrutura das tabelas, colunas e relações entre elas.

* **Análise de sistemas** 

    O modelo ER pode ser utilizado para analisar os requisitos de um sistema de informação e identificar as entidades, atributos e relacionamentos relevantes.

* **Documentação de sistemas** 
    
    Os DERs podem ser utilizados para documentar a estrutura de um sistema de informação, facilitando a compreensão e a manutenção do sistema.

O modelo ER, com sua simplicidade e expressividade, tornou-se uma ferramenta essencial para a modelagem de sistemas de informação. Sua aplicação contribui para o desenvolvimento de bancos de dados eficientes, bem estruturados e fáceis de manter.

## Recursos adicionais

* [https://www.youtube.com/watch?v=cLC-fFeOuqE](https://www.youtube.com/watch?v=cLC-fFeOuqE)
* [https://miro.com/pt/modelos/diagrama-entidades-relacionamento/](https://miro.com/pt/modelos/diagrama-entidades-relacionamento/)
* [https://www.devmedia.com.br/mer-e-der-modelagem-de-bancos-de-dados/14332](https://www.devmedia.com.br/mer-e-der-modelagem-de-bancos-de-dados/14332)
* [https://www.youtube.com/watch?v=IvrSP_VHP-c](https://www.youtube.com/watch?v=IvrSP_VHP-c)
* [A Abordagem Entidade-Relacionamento (E-R) | by Célio Normando - Medium medium.com](https://medium.com/@celionormando/a-abordagem-entidade-relacionamento-e-r-8fb72c73f260)
