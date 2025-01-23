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

from brasileirao_serie_a import clubes

print(clubes)