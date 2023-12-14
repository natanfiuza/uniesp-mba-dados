# Normalização de Banco de Dados

A normalização de banco de dados é um processo que organiza as tabelas de um banco de dados relacional para reduzir a redundância e a dependência de dados. Isso ajuda a evitar problemas como a inserção, atualização e exclusão de anomalias. Existem várias formas normais (1NF, 2NF, 3NF, etc.) que guiam o processo de normalização. Aqui está uma explicação e exemplos de cada uma:

## Introdução

A normalização de banco de dados é o processo de organizar os dados em uma estrutura que evita a redundância e a dependência de dados. Isso é feito dividindo as tabelas em partes menores e mais gerenciáveis e definindo as relações entre elas.

### 1ª Forma Normal (1NF)
Uma tabela está na 1ª Forma Normal quando todos os seus atributos são atômicos, ou seja, indivisíveis. Por exemplo, uma tabela de clientes deve ter colunas separadas para o primeiro nome e o sobrenome, em vez de uma coluna para o nome completo.
Exemplo:
ID	Nome	Sobrenome	Telefone
1	João	Silva	123-4567
2	Maria	Santos	987-6543
### 2ª Forma Normal (2NF)
Uma tabela está na 2ª Forma Normal se estiver na 1ª Forma Normal e se todos os seus atributos não chave dependerem totalmente da chave primária. Em outras palavras, cada coluna não chave deve depender da chave primária.
Exemplo:
ID	Título	Autor	Editora
1	Aprendendo SQL	João	ABC Livros
2	Python Básico	Maria	XYZ Editora
Neste exemplo, "Autor" e "Editora" dependem da chave primária "ID".
### 3ª Forma Normal (3NF)
Uma tabela está na 3ª Forma Normal se estiver na 2ª Forma Normal e se todos os seus atributos não chave são independentes entre si. Em outras palavras, não deve haver dependências transitivas.
Exemplo:
ID	Nome	Endereço	Cidade	CEP
1	João	Rua das Flores, 1	São Paulo	12345
2	Maria	Av. Principal, 100	Rio de Janeiro	54321
Neste exemplo, "Cidade" e "CEP" dependem do "Endereço", criando uma dependência transitiva.
Conclusão
A normalização de banco de dados é essencial para garantir a integridade e a eficiência dos dados. Seguindo as formas normais, é possível projetar um banco de dados que evita problemas comuns e é mais fácil de manter e consultar.


Sources
https://dev.to/gabrielgcj/o-que-e-normalizacao-em-um-banco-de-dados-e-por-que-e-tao-importante-31ni 

https://learn.microsoft.com/pt-br/office/troubleshoot/access/database-normalization-description 

## Quais são os benefícios da normalização de banco de dados

A normalização de banco de dados oferece diversos benefícios, tais como:

**Redução de Redundância:** A normalização elimina a repetição desnecessária de dados, o que reduz o espaço de armazenamento e evita a inconsistência dos dados

**Integridade de Dados:** Ao seguir as regras de normalização, a integridade dos dados é mantida e a probabilidade de ocorrerem inconsistências é reduzida

**Melhor Desempenho de Consulta:** Um banco de dados normalizado pode ter um desempenho de consulta melhor, pois as tabelas são organizadas de forma eficiente e as operações são mais eficientes

**Facilidade de Manutenção:** Um banco de dados normalizado é mais fácil de manter e atualizar, já que as informações estão organizadas e relacionadas de maneira lógica


**Flexibilidade e Escalabilidade:** A normalização garante que o banco de dados seja mais flexível e escalável, facilitando a adição de novos dados e a modificação da estrutura do banco de dados


Em resumo, a normalização de banco de dados é essencial para garantir a integridade, eficiência e flexibilidade dos sistemas de gerenciamento de dados, proporcionando uma série de benefícios importantes para a gestão de dados

**Fonte:**

https://www.ehow.com.br/vantagens-desvantagens-normalizar-base-dados-info_38217/ 

https://www.dio.me/articles/normalizacao-de-banco-de-dados-por-que-organizacao-e-fundamental 


# Quais são as desvantagens da normalização de banco de dados

Embora a normalização de banco de dados ofereça muitos benefícios, ela também apresenta algumas desvantagens, tais como:

**Desempenho:** A normalização pode afetar o desempenho do banco de dados, especialmente em grandes bancos de dados, devido ao aumento do número de tabelas e relações




**Complexidade:** A normalização pode tornar o banco de dados mais complexo e difícil de entender, especialmente para usuários que não estão familiarizados com o modelo relacional



**Custo de Armazenamento:** A normalização pode aumentar o custo de armazenamento, pois pode ser necessário armazenar mais tabelas e relações



**Dificuldade de Modificação:** A normalização pode tornar a modificação do banco de dados mais difícil, pois pode ser necessário modificar várias tabelas e relações


**Requer Análise Detalhada:** A normalização requer uma análise detalhada do banco de dados e pode ser um processo complexo e demorado


Em resumo, a normalização de banco de dados pode apresentar algumas desvantagens, como o aumento do custo de armazenamento e a complexidade do banco de dados. No entanto, essas desvantagens podem ser minimizadas com um planejamento cuidadoso e uma análise detalhada do banco de dados

**Fonte:**
https://dev.to/gabrielgcj/o-que-e-normalizacao-em-um-banco-de-dados-e-por-que-e-tao-importante-31ni 

https://appmaster.io/pt/blog/normalizacao-em-bancos-de-dados-relacionais 

## Como a normalização de banco de dados afeta a simplicidade de operações de manutenção

A normalização de banco de dados afeta positivamente a simplicidade das operações de manutenção. Ao manter um banco de dados normalizado, as operações de atualização e modificação são simplificadas, pois as alterações precisam ser feitas em um único local, evitando a propagação de alterações em várias tabelas


* Isso reduz a probabilidade de erros e torna a manutenção do banco de dados mais eficiente e menos propensa a inconsistências

* Portanto, a normalização contribui para a integridade e a qualidade dos dados, facilitando as operações de manutenção e garantindo que o banco de dados seja mais fácil de gerenciar e entender

