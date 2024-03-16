# Modelo Dimensional no Data Warehouse

## História:
O modelo dimensional é uma abordagem de design de data warehouse popularizada por Ralph Kimball e outros profissionais da área. Surgiu como uma resposta à necessidade de estruturas de dados mais simples e eficientes para análise de negócios. 

Ela foi desenvolvida como uma alternativa aos modelos de banco de dados relacionais tradicionais, que eram complexos e difíceis de entender para análise de negócios.

## Conceitos Principais:
1. **Dimensões e Fatoss:**
   - No modelo dimensional, os dados são organizados em torno de duas entidades principais: dimensões e fatos.
   - Dimensões representam as características pelas quais os dados serão analisados, como tempo, localização, produto ou cliente.
   - Fatos representam as métricas ou medidas numéricas que estão sendo analisadas, como vendas, receitas ou estoques.

2. **Granularidade:**
   - A granularidade refere-se ao nível de detalhe dos dados em um modelo dimensional. É importante determinar a granularidade correta para garantir que os dados sejam úteis e significativos para as análises.

3. **Esquemas Dimensionais:**
   - Os esquemas dimensionais, como o esquema estrela e o esquema de floco de neve, são comuns no modelo dimensional.
   - No esquema estrela, as dimensões são conectadas diretamente à tabela de fatos. No esquema de floco de neve, as dimensões podem ser normalizadas em várias tabelas.

## Analogias:
Podemos comparar o modelo dimensional a uma estante de livros em uma biblioteca:
- As dimensões são como as diferentes categorias de livros (por exemplo, ficção, não-ficção, gênero).
- Os fatos são como os próprios livros, cada um contendo informações específicas que podem ser analisadas.

## Cases de Uso:
- **Case 1: Varejo:**
  - Uma empresa de varejo pode usar um modelo dimensional para analisar as vendas por produto, localização e tempo, permitindo identificar tendências de compra e sazonalidade.

- **Case 2: Saúde:**
  - Um sistema de saúde pode usar um modelo dimensional para analisar os custos de tratamento por paciente, diagnóstico e departamento, ajudando a identificar áreas de eficiência e oportunidades de economia.

## Governança de Dados e Metodologias:
Para criar um modelo dimensional usando governança de dados do negócio, é essencial envolver os seguintes atores:

1. **Equipe de Data Governance:**
   - Responsável por estabelecer políticas, procedimentos e padrões para a gestão dos dados.
2. **Analistas de Negócios:**
   - Responsáveis por entender os requisitos de negócio e traduzi-los em elementos do modelo dimensional.
3. **Arquitetos de Dados:**
   - Responsáveis por projetar e implementar a estrutura técnica do data warehouse, incluindo o modelo dimensional.

Algumas metodologias comuns para criação de modelos dimensionais incluem:

- **Metodologia Kimball:**
  - Desenvolvida por Ralph Kimball, essa metodologia enfatiza a entrega iterativa e incremental de componentes do data warehouse, começando com a identificação das dimensões e fatos principais. Veja mais [aqui](./ralph_kimball_de_baixo_para_cima.md).

- **Metodologia Inmon:**
  - Proposta por Bill Inmon, essa metodologia defende uma abordagem mais top-down, onde o foco inicial é na criação de um data warehouse corporativo completo antes de construir os Data Marts específicos. Veja mais [aqui](./bill_inmon_top_down.md)



## Referências:
- Livro: ["The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling"](./doc/The_Data_Warehouse_Toolkit.pdf) por Ralph Kimball e Margy Ross
- Livro: "Building the Data Warehouse" por William H. Inmon


-----

[Home 🏠](../README.md) | [Indice 📇](README.md)