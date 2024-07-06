# Chave natural

Uma chave natural é um atributo ou um conjunto de atributos em uma tabela de banco de dados que já possui significado e valor intrínseco nos dados e é usado para identificar de forma única um registro na tabela. Diferentemente das chaves substitutas, as chaves naturais têm um valor real e reconhecível que faz sentido dentro do contexto de negócio ou aplicação.

## Características de uma Chave Natural

1. **Significado de Negócio**: A chave natural tem um significado dentro do domínio de negócio. Por exemplo, um número de CPF ou um endereço de e-mail.
2. **Unicidade**: Ela deve ser única para cada registro na tabela, garantindo que não haja duplicações.
3. **Imutabilidade**: Idealmente, uma chave natural deve ser estável e não mudar ao longo do tempo.

## Exemplos de Chaves Naturais

- **CPF (Cadastro de Pessoas Físicas)** no Brasil, que é único para cada cidadão.
- **Números de matrícula** de estudantes em uma universidade.
- **Endereços de e-mail** em uma tabela de usuários.
- **Números de série** em uma tabela de produtos.

## Benefícios das Chaves Naturais

1. **Reconhecibilidade**: As chaves naturais são facilmente reconhecíveis e compreensíveis pelos usuários e desenvolvedores.
2. **Redução de Redundância**: Usar uma chave natural pode eliminar a necessidade de uma chave substituta, reduzindo a complexidade do modelo de dados.

## Desvantagens das Chaves Naturais

1. **Mudança de Valor**: Se o valor da chave natural mudar, pode causar problemas de integridade referencial e exigir atualizações complexas.
2. **Comprimento e Complexidade**: Chaves naturais podem ser compostas de múltiplos atributos ou serem longas, o que pode afetar a performance do banco de dados.
3. **Colisões**: Se a chave natural não for gerada com cuidado, pode haver colisões (duplicações).

## Exemplo em SQL

Suponha uma tabela `Funcionarios` onde o número do CPF é usado como chave natural:

```sql
CREATE TABLE Funcionarios (
    CPF CHAR(11) PRIMARY KEY,
    Nome VARCHAR(100),
    DataNascimento DATE
);
```

Neste exemplo, o `CPF` é a chave natural. Ele já é único por definição e tem significado fora do contexto do banco de dados, pois é um identificador oficial de cidadãos no Brasil.

## Comparação entre Chave Natural e Chave Substituta

- **Chave Natural**: Tem significado de negócio, é reconhecível e já existente nos dados.
- **Chave Substituta**: É gerada pelo sistema, não tem significado fora do banco de dados, e é geralmente mais simples e estável.

A escolha entre usar uma chave natural ou uma chave substituta depende dos requisitos específicos da aplicação e do modelo de dados, balanceando entre simplicidade, desempenho e a necessidade de manter o significado de negócio.