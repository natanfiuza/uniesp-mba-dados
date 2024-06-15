import apache_beam as beam
#DEFINIR A PIPELINE
p1 = beam.Pipeline()

voos = (
    p1
    #LER ARQUIVO E EXCLUIR CABEÇALHO
    #AS PIPES >> SIGNIFICAM QUE UM COMANDO É USADO COMO INPUT DO OUTRO
    |"Importar dados" >> beam.io.ReadFromText('voos_sample.csv', skip_header_lines = 0)
    #aplicando a função lambda a cada elemento do PCollection (coleção de dados)
    #representada por record.
    #A função lambda record.split(',') está dividindo cada registro por vírgulas, criando assim uma lista de valores.
    |"Separar por vírgula" >> beam.Map(lambda record: record.split(','))
    |"Mostrar resultados" >> beam.Map(print)
)

p1.run()