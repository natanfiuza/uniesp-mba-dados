# Analise de dados de uma empresa de desenvolvimento

## O problema
O turnover elevado na área de desenvolvimento da empresa está prejudicando a produtividade e a moral da equipe. Sem clareza sobre as causas, os líderes não conseguem formular estratégias efetivas de retenção. Este projeto buscará identificar os fatores principais que influenciam essa alta rotatividade, permitindo o desenvolvimento de soluções focadas para melhorar a retenção de talentos.

## Os dados

Dados sinteticos de uma empresa de desenvolvimento.

Os campos

| Campo                            | Descrição                                                                                                              | Tipo de Dado         | Exemplo                                     | Observações                                                                                                     |
| :------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :------------------- | :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------- |
| **Matricula**                    | Número único de identificação do funcionário.                                                                          | Inteiro (ou String)  | 12345, A9876                                | Chave primária, não deve ter valores duplicados.                                                                |
| **Idade**                        | Idade do funcionário em anos completos.                                                                                | Inteiro              | 30, 45, 28                                  |                                                                                                                 |
| **Gênero**                       | Gênero do funcionário.                                                                                                 | Categórico           | Masculino, Feminino, Outro                  | Pode ser codificado como: Masculino (0), Feminino (1), Outro (2) para análise.                                  |
| **Departamento**                 | Área da empresa onde o funcionário trabalha.                                                                           | Categórico           | Desenvolvimento, Vendas, Marketing, RH      | Pode ser codificado numericamente para análise (Desenvolvimento = 0, Vendas = 1, etc.)                          |
| **Cargo**                        | Cargo ocupado pelo funcionário.                                                                                        | Categórico           | Analista, Desenvolvedor, Gerente, Diretor   | Pode ser codificado numericamente para análise.                                                                 |
| **Banda Salarial**               | Faixa salarial do funcionário, indicando o nível de remuneração.                                                       | Categórico (Ordinal) | Nível 1, Nível 2, Nível 3                   | Ordinal, pois indica uma ordem hierárquica. Deve ser codificado numericamente respeitando a ordem (1, 2, 3...). |
| **Status**                       | Situação atual do funcionário na empresa (Ativo ou Desligado).                                                         | Categórico (Binário) | Ativo, Desligado                            | Variável *target* para análise de turnover. Codificação comum: Ativo (0), Desligado (1).                        |
| **Motivo do Desligamento**       | Razão pela qual o funcionário saiu da empresa (se aplicável).                                                          | Categórico           | Demissão, Pedido de Demissão, Aposentadoria | Só deve ter valor se `Status` for "Desligado". Pode ser codificado numericamente.                               |
| **Escolaridade**                 | Nível de escolaridade mais alto alcançado pelo funcionário.                                                            | Categórico (Ordinal) | Ensino Médio, Graduação, Pós-Graduação      | Ordinal, pois indica níveis de progressão. Deve ser codificado numericamente respeitando a ordem.               |
| **Estado Civil**                 | Estado civil do funcionário.                                                                                           | Categórico           | Solteiro, Casado, Divorciado, Viúvo         | Pode ser codificado numericamente para análise.                                                                 |
| **Última Promoção (anos)**       | Tempo decorrido (em anos) desde a última promoção do funcionário.                                                      | Numérico (Contínuo)  | 2.5, 5, 0.8                                 | Valores decimais representam frações de ano (meses).                                                            |
| **Horas-extras (média)**         | Média de horas extras trabalhadas pelo funcionário por mês.                                                            | Numérico (Contínuo)  | 10.2, 5.5, 0                                | Valores decimais representam frações de hora.                                                                   |
| **Tempo de Empresa**             | Tempo de serviço do funcionário na empresa (em anos).                                                                  | Numérico (Contínuo)  | 8, 3.2, 12.5                                | Valores decimais representam frações de ano.                                                                    |
| **Engajamento**                  | Nível de engajamento do funcionário, geralmente medido por pesquisa interna.                                           | Numérico (Escala)    | 4.2, 3.8, 4.9                               | Normalmente uma escala de 1 a 5 ou 1 a 10.                                                                      |
| **Satisfação**                   | Nível de satisfação do funcionário, geralmente medido por pesquisa interna.                                            | Numérico (Escala)    | 3.5, 4.1, 2.8                               | Normalmente uma escala de 1 a 5 ou 1 a 10.                                                                      |
| **Desempenho**                   | Avaliação de desempenho do funcionário, geralmente atribuída por um gestor ou por um sistema de avaliação.             | Numérico (Escala)    | 4.0, 3.2, 4.8                               | Normalmente uma escala de 1 a 5 ou 1 a 10.                                                                      |
| **Apoio da Liderança**           | Percepção do funcionário sobre o nível de apoio recebido de seus líderes/gestores.                                     | Numérico (Escala)    | 4.5, 3.0, 4.2                               | Normalmente uma escala de 1 a 5 ou 1 a 10.                                                                      |
| **Percepção de Desenvolvimento** | Percepção do funcionário sobre as oportunidades de desenvolvimento e crescimento profissional oferecidas pela empresa. | Numérico (Escala)    | 3.7, 4.6, 2.5                               | Normalmente uma escala de 1 a 5 ou 1 a 10.                                                                      |


Os dados: [dados_rh.csv](./dados_rh.csv)

## Uso do método .describe() do Pandas

Uma amostra do uso da do método .describe() para os campos `Horas-extras (média)`,`Tempo de Empresa`,`Engajamento`,`Satisfação`

```
       Horas-extras (média)  Tempo de Empresa  Engajamento   Satisfação  \
count           2005.000000       2005.000000  1967.000000  1967.000000
mean               0.737157          4.947132     2.221149     2.209456
std                0.890312          3.178206     0.846512     0.835901
min                0.000000          0.000000     1.000000     1.000000
25%                0.000000          2.000000     1.000000     1.000000
50%                1.000000          5.000000     2.000000     2.000000
75%                1.000000          8.000000     3.000000     3.000000
max                3.000000         10.000000     3.000000     3.000000
```

### Explicação
A tabela de exemplo acima, apresentou é o resultado da função `describe()` do pandas aplicada a um DataFrame, filtrado para as colunas `` "Horas-extras (média)"`, `"Tempo de Empresa"`, `"Engajamento"` e `"Satisfação". Ela fornece estatísticas descritivas para essas quatro variáveis numéricas. Vamos analisar cada linha:

#### **Linhas e seus Significados**

*   **`count`:** Número de observações (linhas) válidas, ou seja, sem valores nulos (NaN), para cada coluna.
    *   `Horas-extras (média)` e `Tempo de Empresa`: 2005 observações válidas.
    *   `Engajamento` e `Satisfação`: 1967 observações válidas. Isso indica que existem alguns valores nulos nessas colunas (2005 - 1967 = 38 valores nulos em cada).

*   **`mean`:** Média aritmética dos valores em cada coluna.
    *   `Horas-extras (média)`: 0.737 - Em média, os funcionários fazem 0.737 horas extras por mês.
    *   `Tempo de Empresa`: 4.947 - Em média, os funcionários estão na empresa há 4.947 anos.
    *   `Engajamento`: 2.221 - Em uma escala de 1 a 3 (conforme indicado pelo `min` e `max` abaixo), o engajamento médio é de 2.221.
    *   `Satisfação`: 2.209 - Em uma escala de 1 a 3, a satisfação média é de 2.209.

*   **`std`:** Desvio padrão, que mede a dispersão dos dados em torno da média. Quanto maior o desvio padrão, maior a variabilidade dos dados.
    *   `Horas-extras (média)`: 0.890 - Indica uma variação considerável na quantidade de horas extras feitas pelos funcionários.
    *   `Tempo de Empresa`: 3.178 - Mostra uma grande variação no tempo de empresa dos funcionários, indicando que há tanto funcionários novos quanto antigos na empresa.
    *   `Engajamento`: 0.847 - Sugere uma variabilidade moderada nos níveis de engajamento.
    *   `Satisfação`: 0.836 - Também indica uma variabilidade moderada nos níveis de satisfação.

*   **`min`:** Valor mínimo observado em cada coluna.
    *   `Horas-extras (média)`: 0 - Alguns funcionários não fazem nenhuma hora extra.
    *   `Tempo de Empresa`: 0 - Existem funcionários com menos de um ano de empresa (o valor 0 pode representar funcionários que estão na empresa há menos de um mês ou que acabaram de ser contratados).
    *   `Engajamento`: 1 - O nível mínimo de engajamento na escala é 1.
    *   `Satisfação`: 1 - O nível mínimo de satisfação na escala é 1.

*   **`25%` (Primeiro Quartil):** Valor que separa os 25% menores valores dos 75% maiores.
    *   `Horas-extras (média)`: 0 - 25% dos funcionários fazem 0 horas extras.
    *   `Tempo de Empresa`: 2 - 25% dos funcionários estão na empresa há 2 anos ou menos.
    *   `Engajamento`: 1 - 25% dos funcionários têm um nível de engajamento de 1 ou menos.
    *   `Satisfação`: 1 - 25% dos funcionários têm um nível de satisfação de 1 ou menos.

*   **`50%` (Segundo Quartil ou Mediana):** Valor que separa os 50% menores valores dos 50% maiores. É o valor central dos dados.
    *   `Horas-extras (média)`: 1 - Metade dos funcionários faz 1 hora extra ou menos, e a outra metade faz 1 hora extra ou mais.
    *   `Tempo de Empresa`: 5 - Metade dos funcionários estão na empresa há 5 anos ou menos, e a outra metade há 5 anos ou mais.
    *   `Engajamento`: 2 - Metade dos funcionários tem um nível de engajamento de 2 ou menos.
    *   `Satisfação`: 2 - Metade dos funcionários tem um nível de satisfação de 2 ou menos.

*   **`75%` (Terceiro Quartil):** Valor que separa os 75% menores valores dos 25% maiores.
    *   `Horas-extras (média)`: 1 - 75% dos funcionários fazem 1 hora extra ou menos.
    *   `Tempo de Empresa`: 8 - 75% dos funcionários estão na empresa há 8 anos ou menos.
    *   `Engajamento`: 3 - 75% dos funcionários têm um nível de engajamento de 3 ou menos.
    *   `Satisfação`: 3 - 75% dos funcionários têm um nível de satisfação de 3 ou menos.

*   **`max`:** Valor máximo observado em cada coluna.
    *   `Horas-extras (média)`: 3 - O máximo de horas extras feitas por um funcionário é 3.
    *   `Tempo de Empresa`: 10 - O funcionário mais antigo está na empresa há 10 anos.
    *   `Engajamento`: 3 - O nível máximo de engajamento na escala é 3.
    *   `Satisfação`: 3 - O nível máximo de satisfação na escala é 3.

#### **Insights e Interpretação**

*   **Horas Extras:** A maioria dos funcionários faz poucas ou nenhuma hora extra (mediana de 1 e média de 0.737). No entanto, existe uma variabilidade considerável, com alguns funcionários fazendo até 3 horas extras em média por mês.
*   **Tempo de Empresa:** Há uma grande variação no tempo de empresa, com uma mediana de 5 anos e um máximo de 10 anos. Isso sugere uma mistura de funcionários novos e experientes.
*   **Engajamento e Satisfação:** As escalas para essas variáveis parecem ser de 1 a 3. Os valores médios estão ligeiramente acima do ponto médio da escala (2), indicando níveis moderados de engajamento e satisfação. A variabilidade também é moderada.
*   **Valores Nulos:** As colunas "Engajamento" e "Satisfação" têm 38 valores nulos cada. É importante investigar esses valores faltantes antes de realizar análises mais aprofundadas. Pode ser necessário imputar esses valores (preenchê-los com estimativas) ou remover as linhas correspondentes, dependendo do contexto e do impacto na análise.

**Em resumo, essa visão dos dados fornece uma boa compreensão inicial da distribuição e das características das variáveis "Horas-extras (média)", "Tempo de Empresa", "Engajamento" e "Satisfação". Ela destaca a variabilidade nos dados, os níveis médios e a presença de valores nulos em "Engajamento" e "Satisfação". Essa informação é fundamental para guiar as próximas etapas da análise exploratória e a formulação de hipóteses sobre o turnover.**
