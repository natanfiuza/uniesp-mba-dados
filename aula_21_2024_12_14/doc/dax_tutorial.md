# Tutorial DAX para Power BI

DAX (Data Analysis Expressions) permite que você desbloqueie todo o potencial dos seus dados no Power BI. Imagine calcular sem esforço o crescimento de vendas ano a ano, criar segmentação dinâmica de clientes ou construir modelos financeiros complexos com apenas algumas linhas de código. Essa é a mágica do DAX, uma linguagem de expressão de fórmulas que transforma dados brutos em insights acionáveis. Este tutorial abrangente irá guiá-lo pelos fundamentos do DAX, equipando você com o conhecimento e as habilidades para realizar cálculos avançados e análise de dados no Power BI.

## O que é DAX?

DAX, ou Data Analysis Expressions, é uma linguagem de expressão de fórmulas usada no Power BI Desktop, Analysis Services e Power Pivot no Excel. Ele fornece uma vasta biblioteca de funções e operadores que podem ser combinados para construir fórmulas e expressões para modelagem e análise de dados. DAX é uma linguagem funcional, o que significa que todo o código é mantido dentro de funções [1, 2, 3].

Pense no DAX como um conjunto de instruções que dizem ao Power BI como manipular e analisar seus dados. Com o DAX, você pode:

*   Executar cálculos complexos que vão além das funções internas do Power BI.
*   Criar novas medidas e dimensões adaptadas às suas necessidades específicas.
*   Descobrir padrões e tendências ocultas em seus dados.
*   Criar relatórios interativos e dinâmicos que respondem às interações do usuário [4].

### Tipos de dados DAX

DAX usa principalmente dois tipos de dados principais:

*   **Numérico:** Esta categoria inclui inteiros, moeda e números decimais.
*   **Outro:** Esta categoria abrange strings (texto) e objetos binários [3].

### Colunas calculadas vs. medidas

DAX permite que você crie dois tipos principais de cálculos: colunas calculadas e medidas [3].

*   **Colunas calculadas:** Adicionam uma nova coluna a uma tabela existente, com cada linha na coluna contendo um valor calculado usando uma fórmula DAX. Essas colunas se comportam como qualquer outro campo em seu modelo de dados. Para criar uma coluna calculada no Power BI, navegue até a guia "Modelagem" e clique em "Nova coluna". Isso abre a barra de fórmulas onde você pode inserir sua fórmula DAX. Você também pode renomear a coluna diretamente na barra de fórmulas [3]. Por exemplo, você pode criar uma coluna calculada chamada "Nome completo" combinando as colunas "Nome" e "Sobrenome" em uma tabela de clientes.

*   **Medidas:** Calculam um único valor agregado para um conjunto selecionado de dados. As medidas são dinâmicas e recalculadas com base no contexto de filtro atual. Para criar uma medida, vá para a guia "Modelagem" e clique em "Nova Medida". Isso adiciona uma nova medida ao seu modelo de dados e você pode definir sua fórmula na barra de fórmulas. Por exemplo, você pode criar uma medida chamada "Vendas totais" que soma os valores na coluna "Valor das vendas" [3].

### Linguagem M vs. DAX

Embora o DAX seja usado para análise de dados e cálculos dentro do modelo de dados do Power BI, a linguagem M é usada no Power Query para transformação e preparação de dados antes de serem carregados no modelo. M está focado principalmente em processos ETL (Extrair, Transformar, Carregar), enquanto DAX é usado para análise de dados e cálculos dentro do modelo [5].

## Sintaxe DAX

As fórmulas DAX seguem uma sintaxe estruturada, semelhante às fórmulas do Excel, mas com algumas diferenças importantes. Uma fórmula DAX sempre começa com um sinal de igual (=) seguido por uma expressão que é avaliada como um valor escalar. Esta expressão pode incluir:

*   **Constantes escalares:** São valores fixos como números (10, 3,14), strings de texto ("Olá") ou datas.
*   **Referências a colunas ou tabelas:** Você pode se referir a colunas dentro de tabelas usando a sintaxe `Tabela`, por exemplo, `Vendas`.
*   **Operadores:** DAX suporta vários operadores para aritmética (+, -, \*, /), comparação (=, >, <, >=, <=, <>), concatenação de texto (&) e operações lógicas (&& para AND, || para OR) [1, 6].
*   **Funções:** DAX fornece uma rica biblioteca de funções para realizar vários cálculos, que exploraremos em detalhes mais tarde [1].

DAX tem a inteligência para identificar automaticamente os tipos de dados dos elementos em suas fórmulas e realizar conversões implícitas quando necessário. Por exemplo, se você tentar adicionar um número a uma data, o DAX entenderá o contexto e converterá o número em um deslocamento de data [7].

## Funções DAX

DAX oferece uma ampla gama de funções para realizar vários cálculos e manipulações de dados. Essas funções são os blocos de construção de suas expressões DAX, permitindo que você obtenha insights significativos de seus dados. Aqui está um vislumbre de algumas das principais categorias de funções:

| Categoria de função    | Descrição                                   | Funções de exemplo                 |
| ---------------------- | ------------------------------------------- | ---------------------------------- |
| Funções de agregação   | Realizar cálculos em um conjunto de valores | `SUM`, `AVERAGE`, `MIN`, `MAX`     |
| Funções de contagem    | Contar linhas ou valores distintos          | `COUNT`, `DISTINCTCOUNT`, `COUNTA` |
| Funções de filtro      | Filtrar dados com base em condições         | `CALCULATE`, `FILTER`, `ALL`       |
| Funções lógicas        | Realizar operações lógicas                  | `IF`, `AND`, `OR`                  |
| Funções de texto       | Manipular strings de texto                  | `LEFT`, `RIGHT`, `MID`             |
| Funções de data e hora | Trabalhar com datas e horas                 | `TODAY`, `NOW`, `YEAR`, `DATEADD`  |
| Funções de informação  | Retornar informações sobre dados e usuários | `USERNAME`, `USERPRINCIPALNAME`    |
| Funções de iterador    | Iterar sobre tabelas e realizar cálculos    | `SUMX`, `AVERAGEX`, `COUNTX`       | [2, 8] |

### Funções de filtro

*   **`CALCULATE`:** Esta poderosa função modifica o contexto de filtro de um cálculo. Ele permite que você aplique filtros específicos aos seus dados antes de realizar o cálculo. Por exemplo, você pode usar `CALCULATE` para calcular o total de vendas para uma região ou categoria de produto específica [9].

*   **`ALL`:** Esta função remove todos os filtros de uma tabela ou coluna, permitindo que você execute cálculos em todo o conjunto de dados, independentemente de quaisquer filtros existentes. Isso é útil quando você precisa comparar um valor filtrado com o total geral [10].

    Por exemplo, a tabela a seguir mostra como a função `ALL` pode ser usada para controlar a interação entre medidas e segmentações de dados:

 | Medida                                                                                                                                                             | Segmentação de dados |
 | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
 | `Vendas com filtro de data = CALCULATE(SUM(Vendas), FILTER(ALL(Datas), Datas = SELECTEDVALUE(Datas)))`                                                             | Data                 |
 | `Vendas com filtro de produto = CALCULATE(SUM(Vendas), FILTER(ALL(Produtos), Produtos = SELECTEDVALUE(Produtos)))`                                                 | Produto              |
 | `Vendas com filtro múltiplo = CALCULATE(SUM(Vendas), FILTER(ALL(Datas), Datas = SELECTEDVALUE(Datas)), FILTER(ALL(Produtos), Produtos = SELECTEDVALUE(Produtos)))` | Data e Produto       | [10] |

### Funções de iterador

As funções de iterador, como `SUMX`, `AVERAGEX` e `COUNTX`, são incrivelmente poderosas para realizar cálculos complexos que exigem avaliação linha por linha. Essas funções iteram sobre uma tabela, avaliam uma expressão para cada linha e, em seguida, agregam os resultados [4, 11].

Por exemplo, `SUMX(Vendas, Vendas * Vendas[Preço unitário])` calcula o valor total das vendas iterando sobre cada linha na tabela `Vendas`, multiplicando a quantidade pelo preço unitário e, em seguida, somando os resultados.

### Funções de inteligência de tempo

DAX fornece um conjunto abrangente de funções de inteligência de tempo que permitem analisar tendências e padrões ao longo do tempo. Essas funções permitem que você execute cálculos como totais do ano até a data, médias móveis e comparações período a período [2].

Por exemplo, a função `SAMEPERIODLASTYEAR` permite comparar os números de vendas do período atual com o mesmo período do ano anterior. Isso pode ser usado para identificar tendências e sazonalidade em seus dados [12].

### Função `RELATED`

A função `RELATED` permite buscar dados de uma tabela relacionada com base em um relacionamento existente entre as tabelas em seu modelo de dados. Isso é particularmente útil para criar colunas calculadas que incorporam informações de várias tabelas [13].

Por exemplo, se você tiver uma tabela `Vendas` e uma tabela `Produtos` vinculadas por um `ID do produto`, você pode usar `RELATED` para adicionar uma coluna "Nome do produto" à tabela `Vendas` buscando o nome do produto correspondente na tabela `Produtos`.

## Operadores DAX

DAX usa uma variedade de operadores para realizar cálculos e comparações em suas fórmulas. Esses operadores incluem:

*   **Operadores aritméticos:** `+` (adição), `-` (subtração), `*` (multiplicação), `/` (divisão) [1]
*   **Operadores de comparação:** `=` (igual a), `>` (maior que), `<` (menor que), `>=` (maior ou igual a), `<=` (menor ou igual a), `<>` (diferente de) [1]
*   **Operador de concatenação de texto:** `&` (concatena duas ou mais strings de texto) [1]
*   **Operadores lógicos:** `&&` (AND), `||` (OR) [6]

## Contexto DAX

Compreender o contexto é crucial para escrever fórmulas DAX eficazes. Contexto se refere ao ambiente no qual uma expressão DAX é avaliada. Existem dois tipos principais de contexto em DAX:

*   **Contexto de linha:** Refere-se à linha atual em uma tabela ao avaliar uma fórmula de coluna calculada.
*   **Contexto de filtro:** Refere-se aos filtros aplicados a uma tabela ou coluna ao avaliar uma fórmula de medida [14].

As fórmulas DAX usam o contexto para determinar quais linhas ou valores devem ser incluídos em um cálculo. Por exemplo, uma fórmula de coluna calculada é avaliada no contexto da linha atual, enquanto uma fórmula de medida é avaliada no contexto de filtro da seleção atual [4].

## Consultas DAX

Além de fórmulas, DAX também suporta consultas, que são semelhantes às consultas SQL. As consultas DAX permitem que você recupere dados do seu modelo de dados e os explore de diferentes maneiras. Eles são usados principalmente para exploração e análise de dados, não para criar novos objetos no modelo ou visuais no relatório [15].

As consultas DAX consistem em duas partes principais:

*   **Instrução `DEFINE`:** Define medidas ou variáveis que podem ser usadas na consulta.
*   **Instrução `EVALUATE`:** Especifica a expressão da tabela que recupera os dados [15].

As fórmulas DAX também podem ser usadas para definir a segurança de funções no Power BI. Isso permite que você controle quais usuários têm acesso a dados específicos em seus relatórios [15].

## Casos de uso para DAX no Power BI

DAX é uma ferramenta versátil que pode ser aplicada a uma ampla gama de cenários de negócios no Power BI. Aqui estão alguns casos de uso comuns:

*   **Calculando porcentagens e totais:** DAX permite calcular porcentagens, como a porcentagem do total de vendas contribuída por cada região ou a porcentagem de clientes que fizeram uma compra no último mês [16].

*   **Criando agregações personalizadas:** Você pode usar DAX para criar agregações personalizadas que vão além de somas e médias simples. Por exemplo, você pode calcular o valor médio da vida útil do cliente ou o valor médio das vendas para uma categoria de produto específica [16].

*   **Filtrando e classificando dados:** DAX oferece recursos poderosos de filtragem e classificação. Você pode usar fórmulas DAX para filtrar dados com base em critérios complexos, como vendas que excedem um determinado limite ou clientes que compraram produtos específicos [16].

*   **Compreendendo os dados do cliente para impulsionar o marketing:** DAX pode ser usado para analisar os dados do cliente para entender seu comportamento, preferências e padrões de compra. Essas informações podem ser usadas para segmentar clientes, personalizar campanhas de marketing e melhorar a satisfação do cliente [16].

*   **Criando visuais e relatórios personalizados:** DAX permite que você crie visuais e relatórios personalizados que são adaptados às suas necessidades específicas. Você pode usar DAX para definir cálculos personalizados, criar visualizações dinâmicas e construir painéis interativos [16].

*   **Executando cálculos de inteligência de tempo:** DAX fornece um rico conjunto de funções de inteligência de tempo que permitem analisar tendências e padrões ao longo do tempo. Você pode usar essas funções para calcular as vendas do ano até a data, médias móveis e comparações período a período [12].

## Exemplos de fórmulas DAX

Aqui estão alguns exemplos de fórmulas DAX que demonstram seus recursos:

*   **Calcular o valor total das vendas:**

```dax
Vendas Totais = SUM(Vendas)
```

*   **Calcular o valor médio das vendas:**

```dax
Média de vendas = AVERAGE(Vendas)
```

*   **Calcular o número de transações de vendas:**

```dax
Número de vendas = COUNTROWS(Vendas)
```

*   **Calcular o valor das vendas para um produto específico:**

```dax
Vendas do produto = CALCULATE(SUM(Vendas), Produtos = "Produto A")
```

*   **Calcular as vendas do ano até a data:**

```dax
Vendas YTD = TOTALYTD(SUM(Vendas), 'Data')
```

## Exemplos DAX do mundo real

Vamos explorar alguns cenários do mundo real onde o DAX pode ser aplicado para resolver problemas de negócios:

*   **Comparando vendas entre períodos:** Um varejista pode usar DAX para comparar vendas entre diferentes períodos, como o trimestre atual versus o mesmo trimestre do ano passado, para identificar tendências e sazonalidade. Isso pode ser alcançado usando funções de inteligência de tempo como `SAMEPERIODLASTYEAR` [12].

*   **Calculando as vendas do ano até a data com filtros:** DAX permite calcular as vendas do ano até a data, mesmo quando os filtros são aplicados aos dados. Isso é útil para rastrear o desempenho de vendas ao longo do ano, enquanto analisa segmentos ou categorias de produtos específicos [17].

*   **Codificação de cores dinâmica com base no desempenho:** Você pode usar DAX para codificar dinamicamente as cores dos visuais com base em comparações de desempenho. Por exemplo, você pode comparar as vendas do mês atual com as vendas do mês anterior e codificar as cores dos valores de acordo para destacar tendências positivas ou negativas [18].

## Práticas recomendadas de otimização DAX

Para garantir que suas fórmulas DAX tenham um desempenho eficiente e que seus relatórios sejam carregados rapidamente, considere estas práticas recomendadas:

*   **Use medidas em vez de colunas calculadas:** As medidas são calculadas dinamicamente, consumindo menos memória do que as colunas calculadas, que armazenam valores para cada linha da tabela [4].
*   **Evite iterações aninhadas:** Minimize o uso de funções aninhadas complexas como `SUMX` e `AVERAGEX` para evitar gargalos de desempenho [4].
*   **Filtre cedo:** Aplique filtros na fonte de dados ou em suas fórmulas DAX para reduzir o número de linhas processadas [4].
*   **Aproveite as variáveis:** Use a palavra-chave `VAR` para armazenar resultados intermediários e evitar cálculos redundantes em uma fórmula [4].
*   **Simplifique os relacionamentos:** Certifique-se de que seu modelo de dados tenha relacionamentos claros e bem definidos entre as tabelas e use a indexação apropriada para um processamento mais rápido [4].
*   **Otimizar cardinalidade:** Reduza o número de valores exclusivos em colunas usadas para filtrar ou juntar para melhorar o desempenho [4].

## Solução de problemas DAX

Embora DAX seja uma linguagem poderosa, às vezes pode ser desafiador escrever fórmulas corretas e eficientes. Aqui estão alguns erros comuns e técnicas de solução de problemas:

*   **Erros de sintaxe:** Verifique cuidadosamente suas fórmulas quanto a erros de digitação, parênteses ausentes ou nomes de função incorretos.
*   **Tipos de dados incorretos:** Certifique-se de que os tipos de dados de suas colunas e valores sejam compatíveis com as funções que você está usando.
*   **Resultados inesperados:** Use o recurso "Avaliar Fórmula" no Power BI para percorrer sua fórmula e entender como ela está sendo avaliada.
*   **Problemas de desempenho:** Se suas fórmulas DAX estiverem lentas, tente otimizá-las usando as práticas recomendadas mencionadas anteriormente.

## Exercícios e Desafios

Pronto para colocar suas habilidades DAX à prova? Aqui estão alguns exercícios e desafios para ajudá-lo a praticar e solidificar sua compreensão:

*   **Calcule a margem de lucro:** Crie uma medida que calcule a margem de lucro como uma porcentagem da receita.
*   **Calcule a taxa de crescimento das vendas:** Crie uma medida que calcule a taxa de crescimento das vendas em comparação com o ano anterior.
*   **Crie uma segmentação de clientes:** Crie uma coluna calculada que segmenta os clientes com base em seu histórico de compras.
*   **Analise as tendências de vendas ao longo do tempo:** Use funções de inteligência de tempo para analisar as tendências de vendas ao longo do tempo, como crescimento mês a mês ou ano a ano.
*   **Divida uma coluna por outra, evitando erros de divisão por zero.** [19]
*   **Use funções condicionais como `IF` e `SWITCH` para adicionar colunas calculadas a um modelo de dados de edifícios mais altos.** [19]
*   **Use a função `RELATED` para criar uma coluna calculada para adicionar rótulos a um gráfico.** [19]
*   **Crie duas novas colunas calculadas, uma usando transição de contexto e outra não.** [19]
*   **Procure colunas de outra tabela usando a função `RELATED`.** [19]
*   **Use funções condicionais como `IF`, `SWITCH`, `ISBLANK` e `AND` para criar colunas calculadas em um relatório sobre turnês musicais.** [19]
*   **Crie uma medida que calcula o valor das vendas multiplicando `Quantidade` e `Preço unitário`.** [9]
*   **Crie uma medida que soma a coluna `Valor das vendas`.** [9]
*   **Conte o número de clientes que compraram mais do que a média dos clientes.** [9]
*   **Classifique os números de visualização usando a função `RANKX`.** [19]
*   **Use a função `CALCULATE` para aplicar filtros às medidas.** [19]
*   **Crie uma medida DAX para referenciar uma segmentação de dados desconectada.** [19]

## Conclusão

DAX é uma linguagem poderosa que libera todo o potencial do Power BI para análise e visualização de dados. Ao dominar o DAX, você pode transformar dados brutos em insights significativos, criar relatórios atraentes e tomar decisões orientadas por dados. Este tutorial forneceu uma visão geral abrangente do DAX, cobrindo sua sintaxe, funções, operadores e aplicações práticas. Lembre-se de que a prática é a chave para se tornar proficiente em DAX. Explore os exemplos fornecidos, experimente diferentes fórmulas e resolva os exercícios para solidificar sua compreensão.

Para aprimorar ainda mais suas habilidades DAX, considere explorar os seguintes recursos:

*   **Microsoft Learn:** A Microsoft oferece extensa documentação e caminhos de aprendizado para Power BI e DAX.
*   **Comunidades online DAX:** Envolva-se com outros usuários DAX em fóruns online e comunidades para compartilhar conhecimento, fazer perguntas e aprender com especialistas.
*   **Livros e cursos DAX:** Numerosos livros e cursos online estão disponíveis para aprofundar sua compreensão dos conceitos e técnicas DAX.

Com dedicação e prática, você pode se tornar um especialista em DAX e liberar todo o poder do Power BI para suas necessidades de análise de dados.

1. [DAX overview - DAX | Microsoft Learn, accessed December 14, 2024,](https://learn.microsoft.com/en-us/dax/dax-overview)
2. [Data Analysis Expressions (DAX) Reference - Microsoft Learn, accessed December 14, 2024,](https://learn.microsoft.com/en-us/dax/)
3. [Power BI - DAX Basics - TutorialsPoint, accessed December 14, 2024,](https://www.tutorialspoint.com/power_bi/dax_basics_in_power_bi.htm)
4. [Power BI DAX Tutorial for Beginners - DataCamp, accessed December 14, 2024,](https://www.datacamp.com/tutorial/power-bi-dax-tutorial-for-beginners)
5. [I am confused between M and DAX : r/PowerBI - Reddit, accessed December 14, 2024,](https://www.reddit.com/r/PowerBI/comments/r1ybr8/i_am_confused_between_m_and_dax/)
6. [DAX Cheat Sheet - Power BI - DataCamp, accessed December 14, 2024,](https://www.datacamp.com/cheat-sheet/dax-cheat-sheet)
7. [DAX syntax - Microsoft Learn, accessed December 14, 2024,](https://learn.microsoft.com/en-us/dax/dax-syntax-reference)
8. [DAX Functions and Formulas in Power BI - AlmaBetter, accessed December 14, 2024,](https://www.almabetter.com/bytes/tutorials/power-bi/dax-functions-and-formulas)
9. [Most Commonly Used 10 DAX Functions in Power BI - Analytics Vidhya, accessed December 14, 2024,](https://www.analyticsvidhya.com/blog/2024/07/dax-functions-in-power-bi/)
10. [Now You See Me! Use cases of ALL DAX Function in Power BI - RADACAD, accessed December 14, 2024,](https://radacad.com/now-you-see-me-use-cases-of-all-dax-function-in-power-bi)
11. [25 Powerful Power BI DAX Formulas and Functions for Beginners - Beehexa, accessed December 14, 2024,](https://www.beehexa.com/blog/25-power-bi-dax-formulas-n-functions/)
12. [Exploring Power BI's DAX for Advanced Analytics - JourneyTeam, accessed December 14, 2024,](https://www.journeyteam.com/resources/blog/exploring-power-bis-dax-for-advanced-analytics/)
13. [Power BI RELATED DAX Function: Introduction and Use Cases - DataCamp, accessed December 14, 2024,](https://www.datacamp.com/tutorial/power-bi-related-dax-function)
14. [Mastering DAX Functions in Power BI - Dataddo Blog, accessed December 14, 2024,](https://blog.dataddo.com/mastering-dax-functions-in-power-bi)
15. [DAX query view - Power BI - Microsoft Learn, accessed December 14, 2024,](https://learn.microsoft.com/en-us/power-bi/transform-model/dax-query-view)
16. [www.upwork.com, accessed December 14, 2024,](https://www.upwork.com/resources/what-is-dax-in-power-bi)
17. [Power BI DAX Funtions: Explained with Examples - BI connector Blog, accessed December 14, 2024,](https://www.biconnector.com/blog/power-bi-dax-functions-explained-with-examples/)
18. [Mastering Power BI DAX Functions: From Basics to Real-World Cases - Medium, accessed December 14, 2024,](https://medium.com/microsoft-power-bi/power-bi-dax-functions-with-basic-case-real-case-5bc29b66ad47)
19. [Free DAX exercises - Wise Owl Training, accessed December 14, 2024,](https://www.wiseowl.co.uk/power-bi/exercises/dax/)
20. [Mastering DAX Exercise Book - Amazon S3, accessed December 14, 2024,](https://s3.amazonaws.com/thinkific-import/10921/MasteringDAXExercises-1465072340720.pdf)