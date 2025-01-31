'''
   REVISÃO 01:

   O código a seguir gera uma lista com os n primeiros números da sequência de Fibonacci.

   # ------------------------------------------------------------
   n = int(input('Digite o valor de n: '))
   
   lstFibonacci = [0, 1]
   
   for i in range(2, n):
      lstFibonacci.append(fib[i-1] + fib[i-2])
   
   print(lstFibonacci)
   # ------------------------------------------------------------
   
   Reescreva o código acima gerando a lista lstFibonacci utilizando List Comprehension 
   e em seguida escreva o resultado em um arquivo chamado 'fibonacci.csv' escrevendo os 
   elementos da lista de Fibonacci em uma linha apenas, separando cada um deles por ;. 
'''
