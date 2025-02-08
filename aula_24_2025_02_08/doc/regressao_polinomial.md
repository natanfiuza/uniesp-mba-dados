# Regressão Polinomial

Preparem-se para ir além da linha reta e modelar relações mais complexas!

## Introdução

Na aula anterior, vimos a Regressão Linear, que funciona muito bem quando a relação entre as variáveis é, bem... linear! Mas e quando os dados não seguem uma linha reta? E se a relação se assemelhar mais a uma curva? É aí que entra a Regressão Polinomial.

A Regressão Polinomial é uma forma de regressão linear em que a relação entre a variável independente *X* e a variável dependente *Y* é modelada como um polinômio de grau *n*. Em outras palavras, em vez de uma linha reta, usamos uma curva para ajustar os dados.

## Conceitos Básicos

1.  **Polinômio:** Uma expressão matemática que consiste em variáveis (também chamadas de indeterminadas) e coeficientes, que envolve apenas as operações de adição, subtração, multiplicação e exponenciação inteira não negativa das variáveis. Exemplos:

    *   `Y = β₀ + β₁X` (Linear - grau 1)
    *   `Y = β₀ + β₁X + β₂X²` (Quadrática - grau 2)
    *   `Y = β₀ + β₁X + β₂X² + β₃X³` (Cúbica - grau 3)
    *   ... e assim por diante.

2.  **Grau do Polinômio:** O maior expoente da variável na equação. O grau determina a "curvatura" do modelo.

3.  **Equação da Regressão Polinomial:**
    `Y = β₀ + β₁X + β₂X² + ... + βₙXⁿ + ε`

    *   `Y` é a variável dependente.
    *   `X` é a variável independente.
    *   `β₀, β₁, β₂, ..., βₙ` são os coeficientes que determinam a forma da curva.
    *   `n` é o grau do polinômio.
    *   `ε` é o termo de erro.

4. **Transformação de Variáveis**: Embora a regressão polinomial modele uma relação não linear entre *X* e *Y*, ela ainda é considerada um modelo *linear* no sentido de que é linear nos coeficientes *β*. Para ajustar um modelo polinomial, frequentemente transformamos a variável independente *X* criando novas variáveis (X², X³, etc.) e, em seguida, usamos a regressão linear múltipla. É um truque inteligente!

## Exemplos Práticos

### Exemplo 1: Crescimento de uma Planta

Imagine que você está estudando o crescimento de uma planta em função do tempo. No início, o crescimento é lento, depois acelera e, eventualmente, diminui. Uma relação linear não capturaria essa dinâmica. Um modelo quadrático (grau 2) poderia ser mais apropriado:

| Tempo (dias) | Altura (cm) |
| ------------ | ----------- |
| 1            | 2           |
| 2            | 5           |
| 3            | 9           |
| 4            | 12          |
| 5            | 14          |
| 6            | 15          |
| 7            | 15          |

### Exemplo 2: Velocidade de Reação Química

A velocidade de uma reação química pode variar com a temperatura de forma não linear. Um polinômio de grau mais alto (talvez cúbico ou de grau 4) poderia modelar essa relação complexa.

## Ferramentas

As mesmas ferramentas que usamos para regressão linear podem ser usadas para regressão polinomial, já que, no fundo, estamos fazendo uma regressão linear múltipla após a transformação das variáveis:

*   **Python:**
    *   `scikit-learn`: Use `PolynomialFeatures` para criar as variáveis polinomiais e, em seguida, use `LinearRegression`.
    *   `statsmodels`: Também suporta regressão polinomial.
    *   `NumPy`: Tem `polyfit` e `polyval` para ajuste e avaliação de polinômios, mas com menos recursos estatísticos que os outros.

*   **R:**
    *   Função: `lm()` em conjunto com `poly()`.  Exemplo: `lm(Y ~ poly(X, 2), data = meus_dados)` ajusta um modelo quadrático.

## Casos de Uso

A regressão polinomial tem uma ampla gama de aplicações, especialmente quando a relação entre as variáveis não é linear:

1.  **Engenharia:** Modelagem de curvas de tensão-deformação de materiais.
2.  **Economia:** Modelagem da relação entre renda e consumo (que pode ter um ponto de saturação).
3.  **Biologia:** Modelagem do crescimento populacional, que muitas vezes segue padrões não lineares.
4.  **Química:** Modelagem da cinética de reações químicas, como mencionado anteriormente.
5.  **Ciência Ambiental:** Modelagem da relação entre a temperatura e a concentração de poluentes.
6.  **Marketing:** Modelar a relação entre investimento e retorno, que pode ter retornos decrescentes.

## Escolhendo o Grau do Polinômio

A escolha do grau do polinômio é crucial. Um grau muito baixo pode levar a *underfitting* (o modelo não captura a complexidade dos dados). Um grau muito alto pode levar a *overfitting* (o modelo se ajusta demais aos dados de treinamento, incluindo o ruído, e não generaliza bem para novos dados).

Algumas técnicas para ajudar a escolher o grau:

*   **Análise Visual:** Plote os dados e observe a forma da curva.
*   **R² Ajustado:** Medida de qualidade de ajuste que penaliza modelos com mais variáveis. Use-o para comparar modelos de diferentes graus.
*   **Validação Cruzada:** Avalie o desempenho do modelo em dados de teste para diferentes graus e escolha aquele com o melhor desempenho.
*   **Critérios de Informação (AIC, BIC):** Métricas que equilibram a qualidade do ajuste com a complexidade do modelo.

## Cuidados e Limitações

*   **Extrapolação:** Tenha extremo cuidado ao extrapolar (fazer previsões fora do intervalo dos dados originais) com modelos polinomiais. Pequenas mudanças em *X* podem levar a grandes mudanças em *Y*, especialmente com graus mais altos.
*   **Multicolinearidade:** Se você usar um grau muito alto, as variáveis polinomiais (X, X², X³, ...) podem se tornar altamente correlacionadas, o que pode causar problemas numéricos e instabilidade nos coeficientes. A regularização (que veremos em aulas futuras) pode ajudar a mitigar isso.
*   **Interpretabilidade:** Modelos polinomiais de grau alto podem ser difíceis de interpretar. Qual o significado prático de um termo X⁵?

## Próximos Passos

Parabéns por dominar a Regressão Polinomial! Agora você está equipado para modelar relações mais complexas do que apenas linhas retas. Continue explorando o mundo da regressão com tópicos como:

*   **Regressão Logística**
*   **Regularização (Ridge, Lasso, Elastic Net)**
*   **Modelos Aditivos Generalizados (GAMs)**
*   **Splines**

Até a próxima aula!

[🔙 Voltar ](./fundamentos_regressao.md)