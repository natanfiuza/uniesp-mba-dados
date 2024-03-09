# Heap 

Heap é uma tabela sem índice clusterizado. Podem ser criados um ou mais índices não clusterizados em tabelas armazenadas como um heap. Dados são armazenados no heap sem especificar uma ordem. Normalmente, os dados são armazenados inicialmente na ordem em que as linhas são inseridas na tabela, mas o mecanismo de banco de dados pode mover os dados no heap para armazenar as linhas de forma eficaz; portanto, a ordem de dados não pode ser prevista. Para garantir a ordem de linhas retornadas de um heap, você deve usar a cláusula ORDER BY. Para especificar uma ordem lógica permanente para armazenar as linhas, crie um índice clusterizado na tabela, de modo que a tabela não seja um heap.

## Quando usar um heap

Quando uma tabela é armazenada como heap, linhas individuais são identificadas por referência a um RID (identificador de linha) de 8 bytes, que é composto pelo número do arquivo, pelo número da página de dados e pelo local na página (FileID:PageID:SlotID). A ID da linha é uma estrutura pequena e eficiente.

Os heaps podem ser usados como tabelas de preparo para operações de inserção grandes e não ordenadas. Como os dados são inseridos sem impor uma ordem estrita, a operação de inserção é geralmente mais rápida do que a inserção equivalente em um índice clusterizado. Se os dados do heap forem lidos e processados em um destino final, talvez seja útil criar um índice não clusterizado estreito que aborde o predicado de pesquisa usado pela consulta de leitura.

```

ℹ️ Observação

Os dados são recuperados de um heap na ordem das 
páginas de dados, mas não necessariamente a ordem 
na qual os dados foram inseridos.

```

Às vezes, os profissionais de dados também usam heaps quando os dados são sempre acessados por índices não clusterizados e o RID é menor que uma chave de índice clusterizado.

Se uma tabela for um heap e não tiver um índice clusterizado, a tabela inteira deverá ser lida (uma verificação de tabela) para localizar as linhas. O SQL Server não pode buscar um RID diretamente no heap. Isso pode ser aceitável quando a tabela é pequena.

## Quando não usar um heap

Não use um heap quando os dados são retornados frequentemente em uma ordem classificada. Um índice clusterizado na coluna de classificação pode evitar a operação de classificação.

Não use um heap quando os dados forem agrupados com frequência. Os dados devem ser classificados antes de serem agrupados, e um índice clusterizado na coluna de classificação pode evitar a operação de classificação.

Não use um heap quando intervalos de dados são consultados frequentemente na tabela. Um índice clusterizado na coluna de intervalo pode evitar a classificação do heap inteiro.

Não use um heap quando não houver índice não clusterizado e a tabela for grande, a menos que você pretenda retornar o conteúdo da tabela inteira sem nenhuma ordem especificada. Em um heap, todas as linhas do heap devem ser lidas para localizar qualquer linha.

Não use um heap se os dados forem atualizados com frequência. Se você atualizar um registro e a atualização usar mais espaço nas páginas de dados do que está sendo usando no momento, o registro precisará ser movido para uma página de dados que tenha espaço livre suficiente. Isso cria um registro encaminhado apontando para o novo local dos dados, e o ponteiro de encaminhamento precisa ser escrito na página que mantinha esses dados anteriormente, para indicar o novo local físico. Isso introduz fragmentação no heap. Ao verificar um heap, esses ponteiros precisam ser seguidos, o que limita o desempenho leitura adiante e pode incorrer em E/S adicional, o que reduz o desempenho da verificação.

## Gerenciando heaps

Para criar um heap, crie uma tabela sem um índice clusterizado. Se uma tabela já tiver um índice clusterizado, descarte o índice clusterizado para retornar a tabela a um heap.

Para remover um heap, crie um índice clusterizado no heap.

Para recompilar um heap para recuperar o espaço desperdiçado:

- Crie um índice clusterizado no heap e descarte esse índice clusterizado.
- Use o comando `ALTER TABLE ... REBUILD` para recompilar o heap.

```
 Aviso

Criar ou descartar índices clusterizados requer 
a regravação da tabela inteira. Se a tabela tiver 
índices não clusterizados, todos os índices não 
clusterizados deverão ser recriados sempre que o 
índice clusterizado for alterado. Portanto, mudar 
de um heap para uma estrutura de índice clusterizado 
ou vice-versa pode demorar muito e exigir espaço em 
disco para reorganizar os dados em tempdb.

```

## Estruturas de heap

Heap é uma tabela sem índice clusterizado. Heaps têm uma linha em [`sys.partitions`](https://learn.microsoft.com/pt-br/sql/relational-databases/system-catalog-views/sys-partitions-transact-sql?view=sql-server-ver16), com `index_id = 0` para cada particionamento usado pelo heap. Por padrão, um heap tem um único particionamento. Quando um heap tem particionamentos múltiplos, cada particionamento tem uma estrutura de heap que contém os dados para aquele específico. Por exemplo, se um heap tiver quatro particionamentos, haverá quatro estruturas de heap; uma em cada particionamento.

Dependendo dos tipos de dados no heap, cada estrutura de heap terá uma ou mais unidades de alocação para armazenar e gerenciar os dados de um particionamento específico. No mínimo, cada heap terá uma `IN_ROW_DATA` unidade de alocação por particionamento. O heap também terá uma `LOB_DATA` unidade de alocação por particionamento, caso tenha colunas LOB (objetos grandes). Também terá uma `ROW_OVERFLOW_DATA` unidade de alocação por particionamento, se tiver colunas de comprimento variável excedendo o limite de tamanho de linha de 8.060 bytes.

A coluna `first_iam_page` no modo de exibição do sistema `sys.system_internals_allocation_units` aponta para a primeira página IAM na cadeia de páginas IAM, que gerencia o espaço alocado no heap em uma partição específica. SQL Server usa as páginas IAM para percorrer o heap. As páginas de dados e as linhas dentro delas não estão em nenhuma ordem específica e não estão vinculadas. A única conexão lógica entre as páginas de dados são as informações registradas nas páginas IAM.
```
ℹ️ Importante

O `sys.system_internals_allocation_units` no modo de exibição 
do sistema é reservado somente para uso interno do SQL Server. 
A compatibilidade futura não está garantida.
```
Os exames de tabela ou as leituras consecutivas de um heap podem ser executados examinando as páginas IAM para localizar as extensões que estão mantendo páginas do heap. Como o IAM representa extensões na mesma ordem que elas existem nos arquivos de dados, isso significa que esses exames de heap consecutivo progridem sequencialmente em cada arquivo. O uso das páginas IAM para definir a sequência de exame também significa que as linhas do heap não são retornadas normalmente na ordem em que foram inseridas.

A ilustração a seguir mostra como o Mecanismo de Banco de Dados do SQL Server usa páginas IAM para recuperar linhas de dados em um único heap de particionamento.

![](../img/iam-heap.gif)