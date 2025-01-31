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
