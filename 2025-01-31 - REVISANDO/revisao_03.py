'''
   REVISÃO 03:

   Crie um arquivos chamado 'valores_entrada.txt' e no seu conteúdo digite 10 valores 
   inteiros quaisquer separados por espaço. 
   
   Em seguida, crie um programa que leia o conteúdo do arquivo e para cada valor lido calcule 
   seu fatorial e escreva o resultado em um arquivo chamado 'valores_saida.txt'.

   O arquivo 'valores_saida.txt' deve conter em cada linha o valor lido e seu fatorial separados por ;
'''
import os, math

# Obtendo o diretório atual
strDirAtual = os.path.dirname(__file__)

# Lendo os valores do arquivo 'valores_entrada.txt'
arqEntrada = open(f'{strDirAtual}\\valores_entrada.txt', 'r')
lstValores = list(map(int, arqEntrada.read().split()))
arqEntrada.close()

# Calculando o fatorial de cada valor e escrevendo no arquivo 'valores_saida.txt'
arqSaida = open(f'{strDirAtual}\\valores_saida.txt', 'w')
for valor in lstValores:
   if valor < 0:
      arqSaida.write(f'{valor};Não existe fatorial para números negativos\n')
   else:
      fatorial = math.factorial(valor)
      arqSaida.write(f'{valor};{fatorial}\n')
arqSaida.close()

