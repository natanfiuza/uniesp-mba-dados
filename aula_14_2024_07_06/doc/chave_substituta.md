# Chave substituta

Uma chave substituta (ou chave surrogate) é um identificador único usado como a chave primária em uma tabela de banco de dados, que não possui significado de negócio ou aplicação fora do contexto do banco de dados. Ela é gerada pelo sistema de gerenciamento de banco de dados (SGBD) e é geralmente um número sequencial ou um UUID (Universally Unique Identifier). A principal característica de uma chave substituta é que ela não tem relação direta com os dados que descreve; sua única função é identificar de forma única cada registro na tabela.

## Benefícios das Chaves Substitutas

1. **Simplicidade**: Como são geradas pelo sistema, elas garantem unicidade de forma simples e direta.
2. **Estabilidade**: Mudanças nos dados reais não afetam a chave substituta, o que mantém a integridade referencial.
3. **Independência do Negócio**: Elas não carregam significado de negócio, evitando ambiguidades e mantendo a independência dos dados.
4. **Consistência**: Facilita a consistência na modelagem de dados e relacionamentos entre tabelas.

## Exemplos de Chaves Substitutas

- **Números sequenciais**: Um contador que incrementa automaticamente para cada novo registro, como 1, 2, 3, etc.
- **UUIDs**: Identificadores únicos globais que são gerados de forma aleatória, garantindo unicidade mesmo em sistemas distribuídos.

## Quando Usar Chaves Substitutas

1. **Quando os dados possuem chaves naturais complexas**: Se a chave natural é composta por múltiplas colunas ou possui valores que podem mudar com frequência, uma chave substituta é preferível.
2. **Para garantir unicidade global**: Em sistemas distribuídos ou quando há a necessidade de integração de dados entre diferentes sistemas.
3. **Para evitar problemas de alteração**: Se a chave natural pode mudar, usar uma chave substituta evita problemas de atualização.

## Exemplo em SQL

Suponha uma tabela `Clientes`:

```sql
CREATE TABLE Clientes (
    ClienteID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Email VARCHAR(100)
);
```

Neste exemplo, `ClienteID` é a chave substituta. Ela é um número inteiro que é incrementado automaticamente pelo SGBD cada vez que um novo registro é inserido. Este identificador não tem significado fora da tabela `Clientes`, mas garante que cada cliente tenha um identificador único.