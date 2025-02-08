#  Regressão Logística

Aprender como modelar e prever *probabilidades* e *categorias*!

## Introdução

Até agora, focamos em problemas de regressão onde a variável dependente era *contínua* (preço de uma casa, nota de um aluno). Mas e quando queremos prever algo que é *categórico*? Por exemplo:

*   Um cliente vai comprar um produto (sim/não)?
*   Um email é spam (spam/não spam)?
*   Um paciente tem uma determinada doença (doente/saudável)?
*   Qual o tipo de uma imagem, dentre 3 categorias (cachorro/gato/pássaro)

Nestes casos, a Regressão Linear não é a ferramenta adequada. Precisamos de um modelo que preveja a *probabilidade* de um evento ocorrer (ou de uma observação pertencer a uma determinada categoria). É aqui que entra a Regressão Logística!

## Conceitos Básicos

### 1.  **Variável Dependente Categórica** 

A variável que queremos prever assume um número limitado de valores (categorias). Pode ser:

    *   **Binária:** Duas categorias (sim/não, 0/1).
    *   **Multinomial:** Mais de duas categorias (cachorro/gato/pássaro).

### 2.  **Função Logística (Sigmoide)** 

A Regressão Logística utiliza uma função especial chamada *função logística* ou *sigmoide* para transformar uma combinação linear das variáveis independentes em uma probabilidade (um valor entre 0 e 1). A equação da função sigmoide é:

    `P(Y=1) = 1 / (1 + e^(-z))`

    Onde:

    *   `P(Y=1)` é a probabilidade de a variável dependente ser igual a 1 (a categoria de interesse).
    *   `e` é a base do logaritmo natural (aproximadamente 2.718).
    *   `z` é a combinação linear das variáveis independentes: `z = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ`
        *   `β₀, β₁, β₂, ..., βₙ` são os coeficientes do modelo (semelhantes aos da regressão linear).
        *   `X₁, X₂, ..., Xₙ` são as variáveis independentes.

### 3.  **Interpretação dos Coeficientes** 

Ao contrário da regressão linear, os coeficientes na regressão logística *não* representam diretamente a mudança na variável dependente. Em vez disso, eles afetam o *log-odds* (logaritmo da razão de chances).

    *   **Odds (Razão de Chances):** A razão entre a probabilidade de um evento ocorrer e a probabilidade de ele não ocorrer: `odds = P(Y=1) / (1 - P(Y=1))`.
    *   **Log-Odds:** O logaritmo natural das odds: `log(odds) = z = β₀ + β₁X₁ + ...`.
    *   Um coeficiente positivo (`βᵢ > 0`) significa que um aumento na variável independente `Xᵢ` aumenta o log-odds, e portanto aumenta a probabilidade de `Y=1`.
    *   Um coeficiente negativo (`βᵢ < 0`) significa que um aumento em `Xᵢ` diminui o log-odds e a probabilidade de `Y=1`.
    *   Um coeficiente igual a zero (`βᵢ = 0`) indica que a variável `Xᵢ` não tem efeito sobre a probabilidade.
    * Para ter uma interpretação mais direta, pode-se usar a exponencial dos coeficientes (`exp(βᵢ)`), que representa a mudança *multiplicativa* nas odds para cada unidade de aumento em `Xᵢ`.

### 4. **Estimativa dos Coeficientes (Máxima Verossimilhança)** 

Diferente da regressão linear (que usa mínimos quadrados), a regressão logística usa um método chamado *Máxima Verossimilhança* (Maximum Likelihood Estimation - MLE). O MLE busca os coeficientes que maximizam a probabilidade de observar os dados que realmente observamos. Não há uma fórmula fechada como nos mínimos quadrados; o MLE é resolvido iterativamente por algoritmos de otimização.

### 5. **Classificação** 

Uma vez que temos as probabilidades estimadas, podemos classificar as observações. Normalmente, usamos um *limiar de decisão* (threshold). Por exemplo, se a probabilidade estimada `P(Y=1)` for maior ou igual a 0.5, classificamos a observação como pertencente à categoria 1 (sim, doente, spam, etc.). Caso contrário, classificamos como categoria 0.

## Exemplos Práticos

### **Exemplo 1: Aprovação em um Exame**

Queremos prever se um aluno será aprovado em um exame (sim/não) com base em suas horas de estudo.

| Horas de Estudo | Aprovado (1=Sim, 0=Não) |
| --------------- | ----------------------- |
| 2               | 0                       |
| 4               | 0                       |
| 6               | 1                       |
| 8               | 1                       |
| 10              | 1                       |

### **Exemplo 2: Risco de Doença Cardíaca**

Queremos modelar a probabilidade de uma pessoa ter doença cardíaca com base em fatores de risco como idade, colesterol, pressão arterial, etc. A variável dependente é binária (doente/saudável).

## Ferramentas

*   **Python:**
    *   `scikit-learn`: `LogisticRegression`.
    *   `statsmodels`: `Logit` (fornece mais detalhes estatísticos).

*   **R:**
    *   `glm()` com `family = binomial(link = "logit")`.

## Casos de Uso

A regressão logística é amplamente utilizada em diversas áreas:

1.  **Medicina:** Diagnóstico de doenças, predição de risco de mortalidade, eficácia de tratamentos.
2.  **Marketing:** Previsão de churn (cancelamento de clientes), resposta a campanhas de marketing, propensão a comprar.
3.  **Finanças:** Análise de risco de crédito, detecção de fraudes.
4.  **Ciências Sociais:** Modelagem de comportamento eleitoral, análise de risco de criminalidade.
5.  **Processamento de Linguagem Natural:** Classificação de texto (análise de sentimento, detecção de spam).
6.  **Visão Computacional:** Classificação de imagens (embora redes neurais profundas sejam mais comuns hoje em dia).

## Regressão Logística Multinomial

Quando a variável dependente tem mais de duas categorias, usamos a *Regressão Logística Multinomial* (também conhecida como *Softmax Regression*). Em vez de uma única função sigmoide, usamos a função *softmax*, que generaliza a sigmoide para múltiplas categorias. A softmax produz um vetor de probabilidades, uma para cada categoria, e a soma dessas probabilidades é igual a 1.

## Avaliação do Modelo

Como a regressão logística lida com classificação, usamos métricas diferentes daquelas da regressão linear (R², RMSE). Algumas métricas comuns:

*   **Acurácia:** Proporção de classificações corretas.
*   **Precisão:** Proporção de verdadeiros positivos entre todos os classificados como positivos (quão "preciso" é o modelo ao prever a classe positiva).
*   **Recall (Revocação/Sensibilidade):** Proporção de verdadeiros positivos entre todos os que *realmente* são positivos (quão "completo" é o modelo ao identificar a classe positiva).
*   **F1-Score:** Média harmônica entre precisão e recall.
*   **Curva ROC e AUC:** Medem a capacidade do modelo de distinguir entre as classes em diferentes limiares de decisão.
*   **Matriz de Confusão:** Tabela que mostra os resultados da classificação (verdadeiros positivos, falsos positivos, verdadeiros negativos, falsos negativos).

## Próximos Passos

Agora que você conhece a Regressão Logística, pode aprofundar seus conhecimentos:

*   **Regularização (L1/Lasso e L2/Ridge):** Essencial para evitar overfitting, especialmente com muitas variáveis independentes.
*   **Seleção de Variáveis:** Métodos para escolher as variáveis mais relevantes para o modelo.
*   **Desbalanceamento de Classes:** Técnicas para lidar com situações em que uma categoria é muito mais frequente que a outra.
*   **Comparação com outros modelos de classificação:** Árvores de decisão, Random Forests, Support Vector Machines (SVMs), Redes Neurais.

A Regressão Logística é uma ferramenta poderosa e versátil para problemas de classificação. Dominá-la abre muitas portas no mundo do Machine Learning!

[🔙 Voltar ](./fundamentos_regressao.md)