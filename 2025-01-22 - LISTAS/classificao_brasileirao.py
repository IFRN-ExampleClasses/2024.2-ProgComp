'''
   ROTEIRO:

   Criar um programa que importe a variavel clubes contida no arquivo brasileirao_serie_a.py

   Uma vez importada a variavel, criar uma lista onde cada elemento contem uma sub-lista. 
   Os dados de cada sub-lista estão organizados da seguinte forma:
   
   [clube, ano, vitorias, empates, derrotas, gols_pro, gols_contra]

   Em seguida o programa deve solicitar o ano da competição e exibir a classificação final 
   do campeonato relativo ao ano informado. 

   Lembrando que só tem informações dos campeonatos a partir de 2019 
   até 2024.

   Ao exibir a classificação, os dados devem ser exibidos da seguinte forma:

   01. [clube] [pontos] [vitorias] [empates] [derrotas] [gols_pro] [gols_contra] [saldo_gols] [aproveitamento]
   02. [clube] [pontos] [vitorias] [empates] [derrotas] [gols_pro] [gols_contra] [saldo_gols] [aproveitamento]
   ...
   20. [clube] [pontos] [vitorias] [empates] [derrotas] [gols_pro] [gols_contra] [saldo_gols] [aproveitamento]
'''
import sys

from brasileirao_serie_a import clubes

# Transformando os dados em uma lista de sublistas
# ignorando a primeira linha que contem os nomes das colunas
lstClubes = [strLinha.split(';') for strLinha in clubes.strip().split('\n')[1:]]
lstClubes = [[c[0], int(c[1]), int(c[2]), int(c[3]), int(c[4]), 
           int(c[5]), int(c[6])] for c in lstClubes]

# Solicitando o ano
intAno = int(input('Digite o ano da competição: '))

# Filtrando os clubes para o ano solicitado
lstClubesAno = list(filter(lambda c: c[1] == intAno, lstClubes))

# Verificando se o ano foi encontrado
if not lstClubesAno:
    sys.exit(f'\nNão foram encontrados dados para o ano {intAno}!\n')

# Calculando os dados adicionais: pontos, saldo de gols e aproveitamento
lstClubesAno = list(map(
    lambda c: c[:1] + [c[2] * 3 + c[3]] + c[2:] + [c[5] - c[6], (c[2] * 3 + c[3]) / 114 * 100],
    lstClubesAno))

# Ordenando os clubes por pontos, vitorias, saldo de gols
lstClubesClassificacao = sorted(lstClubesAno, key=lambda c: (c[1], c[2], c[7]), reverse=True)

# Exibindo a classificação
print(f'Classificação do Brasileirão {intAno}:')
for i, clube in enumerate(lstClubesClassificacao, 1):
    print(f'{i:02}. {clube[0]:<20} {clube[1]} {clube[2]} {clube[3]} {clube[4]} {clube[5]} {clube[6]} {clube[7]} {clube[8]:.0f}')