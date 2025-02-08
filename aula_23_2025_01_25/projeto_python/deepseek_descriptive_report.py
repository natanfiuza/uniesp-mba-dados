"""
Análise de Turnover em Departamento de Desenvolvimento

Gera um relatório de Analise Descritiva

"""

# Importação de bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from scipy.stats import chi2_contingency, ttest_ind

# Configuração de visualização
plt.style.use('ggplot')
sns.set_palette("husl")
#%matplotlib inline

# 1. Carregamento e Inspeção Inicial dos Dados
try:
    df = pd.read_csv('dados_rh.csv')
    print("✅ Arquivo carregado com sucesso!")
except FileNotFoundError:
    print("❌ Arquivo não encontrado!")

def generate_descriptive_report(df):
    """
    Gera um relatório descritivo dos dados com base na tabela fornecida.
    """
    # Cálculo das estatísticas descritivas
    desc_stats = df.describe(include='all').T

    # Inicializa o relatório
    report = "# 📊 **Relatório de Análise Descritiva dos Dados** 📊\n\n"

    # 1. Dados Demográficos
    report += "### 1. Dados Demográficos\n"
    report += f"- **Idade**:\n"
    report += f"  - Média: {desc_stats.loc['Idade', 'mean']:.1f} anos\n"
    report += f"  - Mediana: {desc_stats.loc['Idade', '50%']:.1f} anos\n"
    report += f"  - Faixa: {desc_stats.loc['Idade', 'min']:.1f} a {desc_stats.loc['Idade', 'max']:.1f} anos\n"
    report += f"- **Gênero**:\n"
    report += f"  - Mais frequente: {desc_stats.loc['Gênero', 'top']}\n"
    report += f"- **Estado Civil**:\n"
    report += f"  - Mais frequente: {desc_stats.loc['Estado Civil', 'top']}\n"
    report += f"- **Escolaridade**:\n"
    report += f"  - Mais frequente: {desc_stats.loc['Escolaridade', 'top']}\n\n"

    # 2. Turnover
    report += "### 2. Turnover\n"
    turnover_rate = df['Status'].value_counts(normalize=True).get('Desligado', 0)
    report += f"- **Taxa de Turnover**: {turnover_rate:.1%}\n"
    report += f"- **Motivo de Desligamento mais comum**: {desc_stats.loc['Motivo do Desligamento', 'top']}\n\n"

    # 3. Fatores de Engajamento e Satisfação
    report += "### 3. Fatores de Engajamento e Satisfação\n"
    report += f"- **Engajamento**:\n"
    report += f"  - Mediana: {desc_stats.loc['Engajamento', '50%']:.1f}\n"
    report += f"  - Máximo: {desc_stats.loc['Engajamento', 'max']:.1f}\n"
    report += f"- **Satisfação**:\n"
    report += f"  - Mediana: {desc_stats.loc['Satisfação', '50%']:.1f}\n"
    report += f"  - Máximo: {desc_stats.loc['Satisfação', 'max']:.1f}\n"
    report += f"- **Percepção de Desenvolvimento**:\n"
    report += f"  - Mediana: {desc_stats.loc['Percepção de Desenvolvimento', '50%']:.1f}\n"
    report += f"  - Máximo: {desc_stats.loc['Percepção de Desenvolvimento', 'max']:.1f}\n\n"

    # 4. Promoções
    report += "### 4. Promoções\n"
    report += f"- **Última Promoção (anos)**:\n"
    report += f"  - Mediana: {desc_stats.loc['Última Promoção (anos)', '50%']:.1f} anos\n"
    report += f"  - Máximo: {desc_stats.loc['Última Promoção (anos)', 'max']:.1f} anos\n"
    report += f"  - Observação: {desc_stats.loc['Última Promoção (anos)', 'count']:.0f} registros válidos\n\n"

    # 5. Horas Extras
    report += "### 5. Horas Extras\n"
    report += f"- **Horas-extras (média)**:\n"
    report += f"  - Mediana: {desc_stats.loc['Horas-extras (média)', '50%']:.1f} horas\n"
    report += f"  - Máximo: {desc_stats.loc['Horas-extras (média)', 'max']:.1f} horas\n\n"

    # 6. Apoio da Liderança
    report += "### 6. Apoio da Liderança\n"
    report += f"- **Apoio da Liderança**:\n"
    report += f"  - Mediana: {desc_stats.loc['Apoio da Liderança', '50%']:.1f}\n"
    report += f"  - Máximo: {desc_stats.loc['Apoio da Liderança', 'max']:.1f}\n\n"

    # 7. Tempo de Empresa
    report += "### 7. Tempo de Empresa\n"
    report += f"- **Tempo de Empresa**:\n"
    report += f"  - Mediana: {desc_stats.loc['Tempo de Empresa', '50%']:.1f} anos\n"
    report += f"  - Máximo: {desc_stats.loc['Tempo de Empresa', 'max']:.1f} anos\n\n"

    # 8. Banda Salarial
    report += "### 8. Banda Salarial\n"
    report += f"- **Banda Salarial**:\n"
    report += f"  - Mediana: {desc_stats.loc['Banda Salarial', '50%']:.1f}\n"
    report += f"  - Máximo: {desc_stats.loc['Banda Salarial', 'max']:.1f}\n\n"

    # 9. Desempenho
    report += "### 9. Desempenho\n"
    report += f"- **Desempenho**:\n"
    report += f"  - Mediana: {desc_stats.loc['Desempenho', '50%']:.1f}\n"
    report += f"  - Máximo: {desc_stats.loc['Desempenho', 'max']:.1f}\n\n"

    # Conclusão
    report += "### Conclusão\n"
    report += "Este relatório fornece uma visão geral dos dados, destacando padrões e possíveis problemas, como baixo engajamento, falta de promoções e insatisfação. Esses insights são fundamentais para identificar as causas do turnover e propor soluções eficazes.\n"

    return report


def save_report_to_md(report, filename="descriptive_report.md"):
    """
    Salva o relatório descritivo em um arquivo Markdown (.md).

    Parâmetros:
        report (str): O relatório descritivo gerado.
        filename (str): Nome do arquivo de saída (padrão: 'descriptive_report.md').
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)
        print(f"✅ Relatório salvo com sucesso em '{filename}'!")
    except Exception as e:
        print(f"❌ Erro ao salvar o relatório: {e}")

# Exemplo de uso
# Gera o relatório descritivo
descriptive_report = generate_descriptive_report(df)

# Salva o relatório em um arquivo .md
save_report_to_md(descriptive_report, filename="descriptive_report.md")