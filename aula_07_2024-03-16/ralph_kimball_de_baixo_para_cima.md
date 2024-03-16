# Conceito "de baixo para cima"

No contexto do data warehousing, o conceito "de baixo para cima" refere-se à abordagem proposta por Ralph Kimball para o projeto e implementação de um Data Warehouse (DW). Aqui está uma explicação mais detalhada:

## História:
Ralph Kimball é uma figura proeminente no campo do data warehousing e é conhecido por suas contribuições significativas para o desenvolvimento de metodologias e melhores práticas nessa área. Ele desenvolveu o conceito "de baixo para cima" como parte de sua metodologia de data warehousing, que ficou conhecida como "Modelagem Dimensional".

## Conceitos Principais:
1. **Modelagem Dimensional:**
   - A abordagem "de baixo para cima" é fundamental para a modelagem dimensional proposta por Kimball. Nesse método, os dados são organizados em torno de "dimensões" e "fatos", o que facilita a análise e a consulta.

2. **Data Marts:**
   - A estratégia "de baixo para cima" frequentemente envolve a construção de pequenos [Data Marts](./data_marts.md) independentes para atender às necessidades específicas de um departamento ou equipe. Esses Data Marts são então integrados para formar um Data Warehouse corporativo.

3. **Entrega Iterativa:**
   - Em vez de adotar uma abordagem monolítica para o desenvolvimento do DW, a metodologia de Kimball preconiza a entrega iterativa e incremental, onde os Data Marts são desenvolvidos e implantados em fases.

## Analogias:
Podemos pensar na abordagem "de baixo para cima" como a construção de uma casa a partir do nível do chão. Começamos com as fundações (os Data Marts), depois construímos os andares superiores (a integração dos Data Marts para formar o DW corporativo).

## Cases de Uso:
- **Case 1: Empresa de Varejo:**
  - Uma empresa de varejo pode usar a abordagem "de baixo para cima" para construir Data Marts específicos para cada categoria de produto (por exemplo, eletrônicos, roupas, alimentos) e, em seguida, integrá-los para analisar o desempenho global das vendas.

- **Case 2: Instituição Financeira:**
  - Um banco pode implementar Data Marts separados para gerenciamento de riscos, análise de clientes e previsão de vendas, usando a metodologia "de baixo para cima" para integrar esses Data Marts em um Data Warehouse corporativo.

## Referências:
- Livro: ["The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling"](./doc/The_Data_Warehouse_Toolkit.pdf) por Ralph Kimball e Margy Ross
- Livro: "The Data Warehouse Lifecycle Toolkit" por Ralph Kimball e Margy Ross

Esses recursos fornecem uma visão abrangente da metodologia de data warehousing de Ralph Kimball, incluindo sua abordagem "de baixo para cima".