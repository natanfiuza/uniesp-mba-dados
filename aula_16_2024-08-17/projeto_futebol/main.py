import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mplsoccer import Pitch, VerticalPitch

df_statistics = pd.read_html('https://fbref.com/pt/partidas/d3926429/Corinthians-Atletico-Mineiro-2024Abril14-Serie-A', attrs={'id':'stats_bf4acd28_possession'})[0]
df_statistics.columns = ['_'.join(col).strip() for col in df_statistics.columns.values]
df_estatisticas = df_statistics.drop(16)

print("\n\n\x1b[32m ######### ESTATISTICAS #########")
print("\x1b[34m")
print(df_estatisticas)
inpu = input("\n\x1b[33mPressione uma tecla para continuar..\x1b[0m")
print("\n\n\x1b[32m ######### ESTATISTICAS #########")
print(" ######### COLUNAS #########")
print("\x1b[36m")

for coluna in df_estatisticas.columns:
    print(f" Coluna: \x1b[33m{coluna}\x1b[34m ")

inpu = input("\n\x1b[33mPressione uma tecla para continuar..\x1b[0m")
posicionamento = {'posicao': ['Goleiro', 'Ataque', 'Meio-atacante-esquerda', 'Meio-atacante-direta', 'Meio-atacante-meia', 'Meio-defensor-direita',
                              'Meio-defensor-centro' ,'Meio-defensor-esquerda' ,
                              'Defesa-centro', 'Defesa-esquerda', 'Defesa-direta','Lateral-esquerdo', 'Lateral-direito'],
                  'y':[2, 90, 85, 85, 70, 44, 44, 44, 30, 24, 24, 55, 55],
                  'x':[40, 40, 15, 65, 40, 60, 40, 20, 40, 30, 50, 10, 70]}

jogadores = {'nome': ['Yuri Alberto', 'Wesley Ribeiro', 'Ángel Romero', 'Pedro Raul', 'Rodrigo Garro', 'Igor Coronado',
                      'Fausto Vera', 'Maycon', 'Raniele', 'Hugo', 'Gustavo Henrique', 'Paulinho', 'Félix Torres Caicedo', 'Fagner', 'Matheuzinho', 'Cássio'],
             'posicao':['Ataque', 'Meio-atacante-esquerda', 'Meio-atacante-direta', 'Meio-atacante-direta', 'Meio-atacante-meia', 'Meio-atacante-meia',
                        'Meio-defensor-direita','Meio-defensor-direita','Meio-defensor-esquerda', 'Defesa-direta','Defesa-centro', 'Meio-atacante-meia',
                        'Defesa-esquerda', 'Lateral-esquerdo', 'Lateral-direito', 'Goleiro']}

df_jogadores = pd.DataFrame(jogadores)
df_posicionamento = pd.DataFrame(posicionamento)


df_jogadores = pd.merge(df_jogadores, df_posicionamento, on='posicao', how='outer')

print("\n\n\x1b[32m ######### JOGADORES #########")
print("\x1b[34m")
print(df_jogadores)
inpu = input("\n\x1b[33mPressione uma tecla para continuar..\x1b[0m")

df_estatisticas['%Conducoes'] = ((df_estatisticas['Conduções_Conduções']/df_estatisticas['Conduções_Conduções'].sum())*100).round(2)
df_estatisticas['%DistTotal'] = ((df_estatisticas['Conduções_DistTot']/df_estatisticas['Conduções_DistTot'].sum())*100).round(2)
df_estatisticas['%DistAtaque'] = ((df_estatisticas['Conduções_DistPrg']/df_estatisticas['Conduções_DistPrg'].sum())*100).round(2)
df_estatisticas['%ProjAtaque9m'] = ((df_estatisticas['Conduções_PrgC']/df_estatisticas['Conduções_PrgC'].sum())*100).round(2)
df_estatisticas['%PerdaDomínio'] = ((df_estatisticas['Conduções_Perda de Domínio']/df_estatisticas['Conduções_Perda de Domínio'].sum())*100).round(2)
df_estatisticas['%Desarmes'] = ((df_estatisticas['Conduções_Dis']/df_estatisticas['Conduções_Dis'].sum())*100).round(2)
df_estatisticas['%minutos'] = ((df_estatisticas['Unnamed: 5_level_0_Min.']/90)*100).round(2)
df_estatisticas = (pd.merge(df_jogadores, df_estatisticas, left_on='nome', right_on='Unnamed: 0_level_0_Jogador'))
     

df_estatisticas['inicio_ataque_x'] = (df_estatisticas['x'])
df_estatisticas['inicio_ataque_y'] = (df_estatisticas['y'])
df_estatisticas['fim_ataque_y'] = (df_estatisticas['y']+((df_estatisticas['%DistAtaque'])*120)/100)
df_estatisticas['fim_ataque_x'] = (40)


colunas_conducao = df_estatisticas.loc[:,['Unnamed: 0_level_0_Jogador','%minutos','%Conducoes','%DistTotal','%DistAtaque','%ProjAtaque9m','%PerdaDomínio','%Desarmes',
                                          'x','y','inicio_ataque_x','inicio_ataque_y','fim_ataque_x','fim_ataque_y']].round(2)
print("\n\n\x1b[32m ######### COLUNAS CONDUCAO #########")
print("\x1b[34m")
print(colunas_conducao)
inpu = input("\n\x1b[33mPressione uma tecla para continuar..\x1b[0m")

print("\n\n\x1b[32m ######### TITULARES #########")
print("\x1b[34m")                                                                                        
df_titulares = colunas_conducao.loc[colunas_conducao['Unnamed: 0_level_0_Jogador'].isin(['Cássio','Fagner','Félix Torres Caicedo','Hugo','Gustavo Henrique',
 'Fausto Vera','Raniele','Rodrigo Garro','Ángel Romero','Yuri Alberto','Wesley Ribeiro'])]
print(df_titulares)
inpu = input("\n\x1b[33mPressione uma tecla para continuar..\x1b[0m")

pitch = VerticalPitch(positional=False, pitch_color='#333333', axis=True, label=True, tick=True)
fig, ax = pitch.draw()


x = df_titulares['x']
y = df_titulares['y']


ax.scatter(x, y, c='white', linewidth=3, s=50)


pitch.arrows(df_titulares['y'], df_titulares['x'], df_titulares['fim_ataque_y'], df_titulares['fim_ataque_x'],
             ax=ax, zorder=1, color='#990000')

print("\n\x1b[36m Exibindo imagem\n")
plt.show()

inpu = input("\n\x1b[33mPressione uma tecla para continuar..\x1b[0m")

print("\n\n\n\x1b[31m ######### FIM #########\n\n")
print("\x1b[0m")     