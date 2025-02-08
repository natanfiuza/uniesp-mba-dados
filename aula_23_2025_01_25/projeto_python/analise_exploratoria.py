import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Configurações de exibição
pd.set_option('display.max_columns', None)
plt.rcParams['figure.figsize'] = (12, 8)

# Carregamento do arquivo CSV
try:
    df = pd.read_csv('dados_rh.csv', encoding='utf-8')  # Tente carregar com UTF-8
except UnicodeDecodeError:
    df = pd.read_csv('dados_rh.csv', encoding='latin-1')  # Se UTF-8 falhar, tente Latin-1
except FileNotFoundError:
    print("Arquivo 'dados_rh.csv' não encontrado. Por favor, verifique o nome do arquivo e o diretório.")
    exit()

# --- Análise Exploratória Inicial ---

print("\n--- Visão Geral dos Dados ---")
print(df.head())
input("\n\nEnter para continuar..\n")
print("\n--- Informações do DataFrame ---")
print(df.info())
input("\n\nEnter para continuar..\n")
print("\n--- Estatísticas Descritivas ---")
print(df.describe())
input("\n\nEnter para continuar..\n")
# --- Tratamento de Dados ---

# 1. Renomear colunas para facilitar a manipulação
df.rename(columns={
    'Matricula': 'matricula',
    'Idade': 'idade',
    'Gênero': 'genero',
    'Departamento': 'departamento',
    'Cargo': 'cargo',
    'Banda Salarial': 'faixa_salarial',
    'Status': 'status',
    'Motivo do Desligamento': 'motivo_desligamento',
    'Escolaridade': 'escolaridade',
    'Estado Civil': 'estado_civil',
    'Última Promoção (anos)': 'ultima_promocao',
    'Horas-extras (média)': 'horas_extras',
    'Tempo de Empresa': 'tempo_empresa',
    'Engajamento': 'engajamento',
    'Satisfação': 'satisfacao',
    'Desempenho': 'desempenho',
    'Apoio da Liderança': 'apoio_lideranca',
    'Percepção de Desenvolvimento': 'percepcao_desenvolvimento'
}, inplace=True)

# 2. Converter colunas categóricas para numéricas usando Label Encoding (para análise de correlação e modelos)
le = LabelEncoder()
for col in ['genero', 'departamento', 'cargo', 'faixa_salarial', 'status', 'motivo_desligamento',
            'escolaridade', 'estado_civil']:
    df[col] = le.fit_transform(df[col])

# 3. Tratar valores nulos (se houver)
# Como o foco é o turnover na área de Desenvolvimento, vamos remover as linhas com NaN apenas se
# forem no departamento de Desenvolvimento de Software e se forem relevantes para a análise de turnover (Status)
df_dev = df[df['departamento'] == le.transform(['Desenvolvimento de Software'])[0]]

if df_dev['status'].isnull().any():
    print("\n--- Tratando valores nulos na coluna 'status' no departamento de Desenvolvimento ---")
    print(f"Linhas com 'status' nulo antes: {df_dev['status'].isnull().sum()}")
    df_dev.dropna(subset=['status'], inplace=True)
    df.update(df_dev)  # Atualiza o dataframe original
    print(f"Linhas com 'status' nulo depois: {df_dev['status'].isnull().sum()}")

# --- Análise Focada no Turnover em Desenvolvimento ---

# Filtrar dados para o departamento de Desenvolvimento
df_dev = df[df['departamento'] == le.transform(['Desenvolvimento'])[0]]

# 1. Taxa de Turnover em Desenvolvimento
print("\n--- Taxa de Turnover em Desenvolvimento ---")
total_dev = len(df_dev)
turnover_dev = len(df_dev[df_dev['status'] == le.transform(['Desligado'])[0]])
taxa_turnover_dev = (turnover_dev / total_dev) * 100
print(f"Taxa de Turnover em Desenvolvimento: {taxa_turnover_dev:.2f}%")

# 2. Visualizar a distribuição dos motivos de desligamento
plt.figure()
sns.countplot(x='motivo_desligamento', data=df_dev[df_dev['status'] == le.transform(['Desligado'])[0]])
plt.title('Distribuição dos Motivos de Desligamento em Desenvolvimento')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 3. Análise de Correlação (focada em 'status')
plt.figure()
correlation_matrix = df_dev.corr()
sns.heatmap(correlation_matrix[['status']], annot=True, cmap='coolwarm')
plt.title('Correlação com Status (Desligado/Ativo) em Desenvolvimento')
plt.tight_layout()
plt.show()

# 4. Análise de Faixa Salarial e Turnover
plt.figure()
sns.boxplot(x='status', y='faixa_salarial', data=df_dev)
plt.title('Relação entre Faixa Salarial e Status em Desenvolvimento')
plt.tight_layout()
plt.show()

# 5. Análise de Tempo de Empresa e Turnover
plt.figure()
sns.boxplot(x='status', y='tempo_empresa', data=df_dev)
plt.title('Relação entre Tempo de Empresa e Status em Desenvolvimento')
plt.tight_layout()
plt.show()

# 6. Análise de Última Promoção e Turnover
plt.figure()
sns.boxplot(x='status', y='ultima_promocao', data=df_dev)
plt.title('Relação entre Última Promoção e Status em Desenvolvimento')
plt.tight_layout()
plt.show()

# 7. Análise de Horas Extras e Turnover
plt.figure()
sns.boxplot(x='status', y='horas_extras', data=df_dev)
plt.title('Relação entre Horas Extras e Status em Desenvolvimento')
plt.tight_layout()
plt.show()

# 8. Análise de Engajamento, Satisfação, Desempenho, Apoio e Percepção de Desenvolvimento e Turnover
for col in ['engajamento', 'satisfacao', 'desempenho', 'apoio_lideranca', 'percepcao_desenvolvimento']:
    plt.figure()
    sns.boxplot(x='status', y=col, data=df_dev)
    plt.title(f'Relação entre {col.capitalize()} e Status em Desenvolvimento')
    plt.tight_layout()
    plt.show()

# --- Insights e Conclusões ---

print("\n--- Insights e Conclusões ---")
print("Com base na análise exploratória dos dados, podemos tirar os seguintes insights:")
print("- A taxa de turnover no departamento de Desenvolvimento é de {taxa_turnover_dev:.2f}%.")
print("- Os principais motivos de desligamento são: ... (baseado na visualização da distribuição dos motivos).")
print("- Existe uma correlação (positiva/negativa) entre 'status' e as seguintes variáveis: ... (baseado na matriz de correlação).")
print("- A faixa salarial (parece/não parece) influenciar na retenção de funcionários em Desenvolvimento.")
print("- O tempo de empresa (parece/não parece) influenciar na retenção de funcionários em Desenvolvimento.")
print("- A última promoção (parece/não parece) influenciar na retenção de funcionários em Desenvolvimento.")
print("- A quantidade de horas extras (parece/não parece) influenciar na retenção de funcionários em Desenvolvimento.")
print("- Os níveis de engajamento, satisfação, desempenho, apoio da liderança e percepção de desenvolvimento (parecem/não parecem) influenciar na retenção de funcionários em Desenvolvimento.")
print("\nRecomendações:")
print("- Investigar mais a fundo os motivos de desligamento para entender as causas raízes.")
print("- Desenvolver estratégias para melhorar os fatores que apresentam correlação com o turnover, como por exemplo...")
print("- Considerar a implementação de um programa de retenção de talentos focado em...")
print("- Realizar pesquisas de clima organizacional com maior frequência para monitorar a satisfação e o engajamento dos funcionários.")