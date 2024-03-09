# Índices clusterizados e não clusterizados

Um índice é uma estrutura em disco associada a uma tabela ou exibição, que agiliza a recuperação das linhas de uma tabela ou exibição. Um índice contém chaves criadas de uma ou mais colunas da tabela ou exibição. Essas chaves são armazenadas em uma estrutura (árvore B) que habilita o SQL Server a localizar a linha ou as linhas associadas aos valores de chave de forma rápida e eficaz.

```
 ℹ️ Observação

A documentação do SQL Server usa o termo árvore B geralmente em referência a índices. Em índices de rowstore, o SQL Server implementa uma árvore B+. Isso não se aplica a índices columnstore ou armazenamentos de dados na memória. Para obter mais informações, confira o Guia de arquitetura e design do índice do SQL Server e SQL do Azure.
```
Tabelas ou exibições podem conter os seguintes tipos de índices:

- Clusterizado
  - Os índices clusterizados classificam e armazenam as linhas de dados da tabela ou exibição com base em seus valores de chave. Esses valores principais são as colunas incluídas na definição do índice. Pode haver apenas um índice clusterizado por tabela, pois as linhas de dados podem ser classificadas somente em uma única ordem. 
  - O único momento em que as linhas de dados de uma tabela são armazenadas na ordem de classificação é quando a tabela contém um índice clusterizado. Se a tabela contiver um índice clusterizado, será denominada tabela clusterizada. Se a tabela não possuir nenhum índice clusterizado, suas linhas de dados ficarão armazenadas em uma estrutura não ordenada denominada heap.
- Não clusterizado
  - Os índices não clusterizados têm uma estrutura distinta das linhas de dados. O índice não clusterizado contém os valores de chave de índice não clusterizado e cada entrada de valor de chave tem um ponteiro para a linha de dados que contém o valor de chave.
  - O ponteiro de uma linha de índice em um índice não clusterizado de uma linha de dados é denominado localizador de linhas. A estrutura do localizador de linhas depende de as páginas de dados serem armazenadas em um heap ou em uma tabela clusterizada. Para o heap, o localizador de linhas é um ponteiro para a linha. Para a tabela clusterizada, o localizador de linhas é a chave de índice clusterizado.
  - Você pode adicionar colunas não chave ao nível folha do índice não clusterizado para ignorar os limites de chave de índice existente e executar consultas completamente abrangidas e indexadas. Para obter mais informações, confira Criar índices com colunas inclusas. Para obter detalhes sobre os principais limites do índice, veja Especificações de capacidade máxima do SQL Server.

Tanto os índices clusterizados quanto os não clusterizados podem ser exclusivos. Com um índice exclusivo, duas linhas não podem ter o mesmo valor que a chave de índice. Caso contrário, o índice não será exclusivo e várias linhas poderão compartilhar o mesmo valor de chave. Para obter mais informações, confira Criar índices exclusivos.

Os índices são mantidos automaticamente para uma tabela ou exibição sempre que os dados da tabela são modificados.

Veja [Índices](https://learn.microsoft.com/pt-br/sql/relational-databases/indexes/indexes?view=sql-server-ver16) para obter mais tipos de índices de uso especial.

## Índices e restrições

O SQL Server cria índices automaticamente quando as restrições PRIMARY KEY e UNIQUE são definidas em colunas de tabelas. Por exemplo, quando você criar uma tabela com uma restrição UNIQUE, o mecanismo de banco de dados criará automaticamente um índice não clusterizado. Se você configurar uma PRIMARY KEY, o mecanismo de banco de dados criará automaticamente um índice clusterizado, a menos que já exista um. Quando você tentar impor uma restrição PRIMARY KEY em uma tabela existente e já houver um índice clusterizado nessa tabela, o SQL Server irá impor a chave primária usando um índice não clusterizado.

Para obter mais informações, confira [Criar chaves primárias](https://learn.microsoft.com/pt-br/sql/relational-databases/tables/create-primary-keys?view=sql-server-ver16) e [Criar restrições exclusivas](https://learn.microsoft.com/pt-br/sql/relational-databases/tables/create-unique-constraints?view=sql-server-ver16).

## Como os índices são usados pelo otimizador de consulta

Índices bem projetados podem reduzir as operações de E/S de disco e consumir menos recursos de sistema. Portanto, esses índices melhoram o desempenho da consulta. Os índices podem ser úteis para uma série de consultas que contêm instruções SELECT, UPDATE, DELETE ou MERGE. Considere a consulta `SELECT JobTitle, HireDate FROM HumanResources.Employee WHERE BusinessEntityID = 250` no banco de dados AdventureWorks2022 . Quando essa consulta é executada, o otimizador de consulta avalia cada método disponível para recuperar os dados e seleciona o mais eficaz. O método pode ser uma verificação de tabela ou verificação de um ou mais índices, se houver.

Durante uma verificação de tabela, o otimizador de consulta lê todas as linhas da tabela e extrai as linhas que atendem os critérios da consulta. Uma verificação de tabela gera várias operações de E/S de disco e pode utilizar muitos recursos. No entanto, a verificação de tabela poderá ser o método mais eficaz se, por exemplo, o conjunto de resultados da consulta contiver um alto percentual de linhas da tabela.

Quando o otimizador de consulta utiliza um índice, ele pesquisa as colunas de chave do índice, encontra o local de armazenamento das linhas necessárias à consulta e extrai as linhas que correspondem àquele local. Geralmente, pesquisar o índice é muito mais rápido do que pesquisar a tabela. Ao contrário de uma tabela, um índice frequentemente contém muito poucas colunas por linha e as linhas estão em ordem de classificação.

Normalmente, o otimizador de consulta seleciona o método mais eficaz ao executar consultas. No entanto, se não houver índices disponíveis, o otimizador de consulta precisará usar uma verificação de tabela. Sua tarefa é criar índices mais adequados ao seu ambiente, para que o otimizador de consulta tenha uma seleção de índices eficientes da qual selecionar. O SQL Server fornece o [Orientador de Otimização do Mecanismo de Banco de Dados](https://learn.microsoft.com/pt-br/sql/relational-databases/performance/database-engine-tuning-advisor?view=sql-server-ver16) para ajudar com a análise de seu ambiente de banco de dados e na seleção de índices apropriados.

```
ℹ️ Importante

Para obter mais informações sobre as diretrizes de design de índice e operações internas, veja o [Guia de design da arquitetura do índice do SQL Server e do SQL do Azure](https://learn.microsoft.com/pt-br/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver16).

```

