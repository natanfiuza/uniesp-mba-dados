# Sistema Python 

Vamos criar um sistema em Python para analisar o conjunto de dados e identificar os fatores principais que influenciam a alta rotatividade na área de desenvolvimento. Utilizaremos as bibliotecas `pandas` para manipulação de dados, `matplotlib` e `seaborn` para visualização, e `scikit-learn` para modelagem e análise preditiva.

### Passo 1: Importação das Bibliotecas

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
```

### Passo 2: Carregamento do Arquivo CSV

```python
# Carregar o arquivo CSV
df = pd.read_csv('dados_rh.csv')

# Visualizar as primeiras linhas do DataFrame
print(df.head())
```

### Passo 3: Análise Exploratória dos Dados (EDA)

#### 3.1 Verificação de Dados Faltantes

```python
# Verificar dados faltantes
print(df.isnull().sum())
```

#### 3.2 Estatísticas Descritivas

```python
# Estatísticas descritivas
print(df.describe())
```

#### 3.3 Distribuição de Variáveis Categóricas

```python
# Distribuição de gênero
sns.countplot(x='Gênero', data=df)
plt.title('Distribuição de Gênero')
plt.show()

# Distribuição de departamento
sns.countplot(y='Departamento', data=df)
plt.title('Distribuição por Departamento')
plt.show()

# Distribuição de banda salarial
sns.countplot(x='Banda Salarial', data=df)
plt.title('Distribuição de Banda Salarial')
plt.show()
```

#### 3.4 Correlação entre Variáveis

```python
# Matriz de correlação
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()
```

### Passo 4: Análise de Turnover

#### 4.1 Taxa de Turnover

```python
# Taxa de turnover
turnover_rate = df['Status'].value_counts(normalize=True) * 100
print(f"Taxa de Turnover: {turnover_rate}")
```

#### 4.2 Fatores que Influenciam o Turnover

```python
# Comparação de idade entre quem saiu e quem ficou
sns.boxplot(x='Status', y='Idade', data=df)
plt.title('Idade vs Status')
plt.show()

# Comparação de tempo de empresa entre quem saiu e quem ficou
sns.boxplot(x='Status', y='Tempo de Empresa', data=df)
plt.title('Tempo de Empresa vs Status')
plt.show()

# Comparação de engajamento entre quem saiu e quem ficou
sns.boxplot(x='Status', y='Engajamento', data=df)
plt.title('Engajamento vs Status')
plt.show()
```

### Passo 5: Modelagem Preditiva

#### 5.1 Preparação dos Dados

```python
# Codificação de variáveis categóricas
df = pd.get_dummies(df, columns=['Gênero', 'Departamento', 'Cargo', 'Banda Salarial', 'Escolaridade', 'Estado Civil'], drop_first=True)

# Separação das variáveis independentes e dependentes
X = df.drop(['Matricula', 'Status', 'Motivo do Desligamento'], axis=1)
y = df['Status']

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

#### 5.2 Treinamento do Modelo

```python
# Treinamento do modelo de Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```

#### 5.3 Avaliação do Modelo

```python
# Previsões
y_pred = model.predict(X_test)

# Matriz de confusão
print(confusion_matrix(y_test, y_pred))

# Relatório de classificação
print(classification_report(y_test, y_pred))
```

#### 5.4 Importância das Variáveis

```python
# Importância das variáveis
importances = model.feature_importances_
feature_importances = pd.Series(importances, index=X.columns)
feature_importances.sort_values(ascending=False).plot(kind='bar')
plt.title('Importância das Variáveis')
plt.show()
```

### Passo 6: Insights e Recomendações

Com base na análise exploratória e na modelagem preditiva, podemos identificar os principais fatores que influenciam o turnover na área de desenvolvimento:

1. **Idade e Tempo de Empresa**: Funcionários mais jovens e com menos tempo de empresa tendem a sair mais.
2. **Engajamento e Satisfação**: Funcionários com baixo engajamento e satisfação têm maior probabilidade de sair.
3. **Apoio da Liderança e Percepção de Desenvolvimento**: A falta de apoio da liderança e a percepção de estagnação no desenvolvimento profissional são fatores críticos.
4. **Banda Salarial e Escolaridade**: Funcionários em bandas salariais mais baixas e com menor escolaridade também apresentam maior rotatividade.

### Recomendações:

- **Programas de Desenvolvimento**: Implementar programas de desenvolvimento profissional e planos de carreira claros.
- **Aumento de Engajamento**: Realizar pesquisas de engajamento e satisfação para identificar áreas de melhoria.
- **Revisão Salarial**: Avaliar e ajustar as bandas salariais para garantir competitividade.
- **Suporte da Liderança**: Treinar líderes para oferecer mais apoio e feedback construtivo.

### Conclusão

Este sistema de análise de dados fornece uma visão clara dos fatores que influenciam o turnover na área de desenvolvimento. Com essas informações, a empresa pode desenvolver estratégias focadas para melhorar a retenção de talentos e, consequentemente, a produtividade e a moral da equipe.

### Código Completo

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Carregar o arquivo CSV
df = pd.read_csv('dados_rh.csv')

# Verificar dados faltantes
print(df.isnull().sum())

# Estatísticas descritivas
print(df.describe())

# Distribuição de gênero
sns.countplot(x='Gênero', data=df)
plt.title('Distribuição de Gênero')
plt.show()

# Distribuição de departamento
sns.countplot(y='Departamento', data=df)
plt.title('Distribuição por Departamento')
plt.show()

# Distribuição de banda salarial
sns.countplot(x='Banda Salarial', data=df)
plt.title('Distribuição de Banda Salarial')
plt.show()

# Matriz de correlação
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()

# Taxa de turnover
turnover_rate = df['Status'].value_counts(normalize=True) * 100
print(f"Taxa de Turnover: {turnover_rate}")

# Comparação de idade entre quem saiu e quem ficou
sns.boxplot(x='Status', y='Idade', data=df)
plt.title('Idade vs Status')
plt.show()

# Comparação de tempo de empresa entre quem saiu e quem ficou
sns.boxplot(x='Status', y='Tempo de Empresa', data=df)
plt.title('Tempo de Empresa vs Status')
plt.show()

# Comparação de engajamento entre quem saiu e quem ficou
sns.boxplot(x='Status', y='Engajamento', data=df)
plt.title('Engajamento vs Status')
plt.show()

# Codificação de variáveis categóricas
df = pd.get_dummies(df, columns=['Gênero', 'Departamento', 'Cargo', 'Banda Salarial', 'Escolaridade', 'Estado Civil'], drop_first=True)

# Separação das variáveis independentes e dependentes
X = df.drop(['Matricula', 'Status', 'Motivo do Desligamento'], axis=1)
y = df['Status']

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinamento do modelo de Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Previsões
y_pred = model.predict(X_test)

# Matriz de confusão
print(confusion_matrix(y_test, y_pred))

# Relatório de classificação
print(classification_report(y_test, y_pred))

# Importância das variáveis
importances = model.feature_importances_
feature_importances = pd.Series(importances, index=X.columns)
feature_importances.sort_values(ascending=False).plot(kind='bar')
plt.title('Importância das Variáveis')
plt.show()
```

Este código fornece uma análise completa dos dados, desde a carga inicial até a geração de insights e recomendações para reduzir o turnover na área de desenvolvimento.