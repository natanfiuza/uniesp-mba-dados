import apache_beam as beam

p1 = beam.Pipeline()

palavras=['STEREO','DIAMANTES','MERCEARIA','DROGARIA']


def encontrarPalavras(i):
    """
    Econtra o valor de palavras igual a qualquer campo e exibe o mesmo
    """
    if i in palavras:
        return True

def encontrarPalavras_linha(record):
    """
    Encontra o valor de palavra igual a qualquer campo da linha e retorna a linha
    """
    return any(palavra in record for palavra in palavras)

def encontrarPalavras_linha_like(record):
    """
    Função para verificar se qualquer parte de um campo na linha contém uma das palavras
    """
    return any(palavra in field for field in record for palavra in palavras)

def encontrarPalavras_linha_like_2fields(record):
    """
       Se alguma palavra for encontrada, retorna apenas os campos 1 e 3
    """
    if any(palavra in field for field in record for palavra in palavras):
        return [record[0], record[2]]
    else:
        return []  # Retorna uma lista vazia se nenhuma palavra for encontrada

def formatar_cnpj(cnpj):
    # Remove caracteres não numéricos
    cnpj = ''.join(filter(str.isdigit, cnpj))
    
    # Formata o CNPJ com pontos e barras
    cnpj_formatado = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

    # Retorna o CNPJ formatado
    return cnpj_formatado

def formatar_cep(cep):
    # Verifica se o CEP possui exatamente 8 dígitos
    if len(cep) == 8:
        # Formata o CEP com hífen
        cep_formatado = f"{cep[:5]}-{cep[5:]}"
        return cep_formatado
    else:
        # Retorna None se o CEP não tiver 8 dígitos
        return None

file_path = 'dados_empresas.csv'
encoding = 'latin1'  # Substitua pelo encoding correto

with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
    lines = file.readlines()

Collection = (
    p1
    | 'Create' >> beam.Create(lines)   
    |"Separar por vírgula" >> beam.Map(lambda record: record.replace('"', '').split(';'))
    |"Filtrar palavras" >> beam.Filter(encontrarPalavras_linha_like_2fields)
    #| 'Remover Linhas Vazias' >> beam.Filter(lambda record: len(record) > 0)  # Filtra linhas vazias
    #| 'Formatar Saída' >> beam.Map(lambda record: ', '.join(record))  # Formata a saída para imprimir
    | 'Mostrar Dados' >> beam.Map(lambda record: print("\x1b[36m",
            formatar_cnpj('-'.join(
                [
                    '/'.join([record[0],record[1]]),
                    record[2]
                ])),"\x1b[32m",record[4],
                "\x1b[33mEndereço:\x1b[35m",
                record[13],
                ','.join([record[14],record[15]]),
                ', '.join([record[16],record[17],formatar_cep(record[18]),record[19]])
                ,"\x1b[0m")) #
    )

p1.run()
