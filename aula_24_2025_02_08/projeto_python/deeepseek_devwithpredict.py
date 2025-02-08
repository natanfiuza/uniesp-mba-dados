import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Carregar o arquivo CSV
df = pd.read_csv('devswithpredict.csv')

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