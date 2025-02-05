'''
   REVISÃO 01:

   O código a seguir gera uma lista com os n primeiros números da sequência de Fibonacci.

   # ------------------------------------------------------------
   n = int(input('Digite o valor de n: '))
   
   a, b = 1, 1
   
   lstFibonacci = list()
   for _ in range(n):
      lstFibonacci.append(a)
      a, b = b, a + b

   print(lstFibonacci)
   # ------------------------------------------------------------
   
   Reescreva o código acima gerando a lista lstFibonacci utilizando List Comprehension 
   e em seguida escreva o resultado em um arquivo chamado 'fibonacci.csv' escrevendo os 
   elementos da lista de Fibonacci em uma linha apenas, separando cada um deles por ;. 
'''
import os

# Solicitando a quantidade de elementos da sequência de Fibonacci
n = int(input('Digite o valor de n: '))

# Inicializando a lista com os dois primeiros elementos da sequência de Fibonacci
lstFibonacci = [1, 1]

# Gerando a lista com os n primeiros elementos da sequência de Fibonacci
[lstFibonacci.append(lstFibonacci[-1] + lstFibonacci[-2]) for _ in range(2, n)]

# Obtendo o diretório atual
strDirAtual = os.path.dirname(__file__)

# Escrevendo a lista gerada no arquivo 'fibonacci.csv'
arqSaida = open(f'{strDirAtual}\\fibonacci.csv', 'w')
arqSaida.write(';'.join(map(str, lstFibonacci)))
arqSaida.close()

# Exibindo a lista gerada
print(lstFibonacci)





