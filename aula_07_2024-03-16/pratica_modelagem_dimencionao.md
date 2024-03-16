# Prática Modelagem Dimencional

Aqui está uma proposta de modelagem dimensional para o Data Warehouse da empresa fictícia, abordando cada um dos itens mencionados:

## 1. **RH: Acompanhamento de Contratações**:

### Tabela de Fatos: 

Tabela: **contratacoes**
| Nome | Tipo  |
|------|-------|
| id_contratacao |  int  |
| id_funcionario |  int  |
|  data_contratacao | datetime  |
|  cargo | string   |
|  salario |  float |
        
        
### Tabelas de Dimensão: 

Tabela: **funcionarios** 
| Nome           | Tipo |
| -------------- | ---- |
| id_funcionario | int  |
| nome | string  |
| id_departamento | string  |
| cargo | string  |
| data_admissao | datetime  |

Tabela: **departamentos** 
| Nome           | Tipo |
| -------------- | ---- |
| id_departamento | int  |
| nome_departamento | string  |


## 2. **Financeiro: Contas a Pagar**:

### Tabela de Fatos: 
Tabela: **contas_pagar** 
| Nome           | Tipo |
| -------------- | ---- |
| id_conta | int  |
| id_fornecedor | int  |
| data_vencimento | datetime  |
| valor | float  |
### Tabelas de Dimensão: 
Tabela: **fornecedores** 
| Nome           | Tipo |
| -------------- | ---- |
| id_fornecedor | int  |
| nome_fornecedor | string  |
| categoria_fornecedor | string  |


## 3. **Contabilidade: Entradas e Saídas, fechamento mensal**:
### Tabela de Fatos: 
Tabela: **movimento_contabil** 
| Nome          | Tipo |
| ------------- | ---- |
| id_movimento | int  |
| data_movimento | int  |
| tipo_movimento | int  |
| valor | int  |

### Tabelas de Dimensão: 
Tabela: **contas_contabeis** 
| Nome          | Tipo |
| ------------- | ---- |
| id_conta_contabil | int  |
| nome_conta_contabil | int  |
      

Tabela: **periodos** 
| Nome         | Tipo |
| ------------ | ---- |
| id_periodo | int  |
| mes | int  |
| ano | int  |


## 4. **Vendas: Acompanhamento de vendas por vendedor**:
### Tabela de Fatos: 
Tabela: **vendas** 
| Nome         | Tipo |
| ------------ | ---- |
| id_venda | int  |
| id_vendedor | int  |
| data_venda | datetime |
| valor_venda | float |



### Tabelas de Dimensão: 

Tabela: **vendedores** 
| Nome         | Tipo |
| ------------ | ---- |
| id_vendedor | int  |
| nome_vendedor | string  |
| regiao_vendedor | string  |


Tabela: **produtos** 
| Nome         | Tipo |
| ------------ | ---- |
| id_produto | int  |
| nome_produto | string |
| categoria_produto | string  |


## 5. **Estoque: Controle de Quantidade de Produtos**:
### Tabela de Fatos: 
      Tabela: **estoque** 
      | Nome         | Tipo |
      | ------------ | ---- |
      | id_produto | int  |
      | data_movimento | datetime  |
      | tipo_movimento | string  |
      | quantidade | int  |

### Tabelas de Dimensão: 
      Tabela: **produtos** 
      | Nome         | Tipo |
      | ------------ | ---- |
      | id_produto | int  |
      | nome_produto | string  |
      | categoria_produto | string  |


## 6. **Consulta Médica: Relatório de pacientes atendidos**:
### Tabela de Fatos: 

      Tabela: **consultas** 

      | Nome         | Tipo |
      | ------------ | ---- |
      | id_consulta | int  |
      | id_paciente | int  |
      | data_consulta | int  |
      | tipo_consulta | int  |

### Tabelas de Dimensão: 

      Tabela: **pacientes** 

      | Nome        | Tipo |
      | ----------- | ---- |
      | id_paciente | int  |
      | nome_paciente | string  |
      | idade_paciente | int  |
      | sexo_paciente | string  |


      Tabela: **medicos** 

      | Nome        | Tipo |
      | ----------- | ---- |
      | id_medico | int  |
      | nome_medico | string |
      | especialidade_medico | string  |

## 7. **Setores de Internação de Paciente: Relatório de pacientes internados na UTI**:
### Tabela de Fatos: 
  
      Tabela: **internacoes** 

      | Nome        | Tipo |
      | ----------- | ---- |
      | id_internacao | int  |
      | id_paciente | int  |
      | data_entrada | datetime  |
      | data_saida | datetime |

### Tabelas de Dimensão: 

      Tabela: **setores** 

      | Nome        | Tipo |
      | ----------- | ---- |
      | id_setor | int  |
      | nome_setor | string  |


## 8. **Marketing: Quantidade de acessos por campanha**:
### Tabela de Fatos: 

      Tabela: **acessos_campanha** 

      | Nome        | Tipo |
      | ----------- | ---- |
      | id_acesso | int  |
      | id_campanha | int  |
      | data_acesso | datetime  |

### Tabelas de Dimensão: 

      Tabela: **campanhas** 

      | Nome        | Tipo |
      | ----------- | ---- |
      | id_campanha | int  |
      | nome_campanha | string  |
      | tipo_campanha | string  |


## **Explicação**:
- Cada tabela de fatos representa um evento ou transação de negócio que queremos analisar.
- As tabelas de dimensão fornecem contextos adicionais para os dados da tabela de fatos, permitindo a análise de diferentes perspectivas.
- As chaves estrangeiras nas tabelas de fatos se relacionam com as chaves primárias nas tabelas de dimensão, estabelecendo relacionamentos entre os dados.
- Esse modelo permite consultas analíticas eficientes para responder perguntas de negócios específicas e gerar insights valiosos para a empresa.


-----

[Home 🏠](../README.md) | [Indice 📇](README.md)