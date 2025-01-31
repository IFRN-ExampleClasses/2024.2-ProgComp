'''
   REVISÃO 02:

   Considerando a equação padrão de uma reta f(x) = ax + b, onde a é o coeficiente
   angular e b é o coeficiente linear, o código a seguir calcula o valor de f(x) para 
   os valores de x compreendidos entre x_inicial e x_final e adiciona na lista 
   lstResultados sub-listas no formato [x, f(x)].

   # ------------------------------------------------------------
   a         = int(input('Informe o valor de a (coeficiente angular): '))
   b         = int(input('Informe o valor de b (coeficiente linear): '))
   x_inicial = int(input('Informe o valor inicial de x: '))
   x_final   = int(input('Informe o valor final de x: '))
   
   # Laço para calcular f(x) para cada valor de x no intervalo
   lstResultados = list()
   for x in range(x_inicial, x_final+1):
      fx = a * x + b
      lstResultados.append([x, fx])
   
   print(lstResultados)
   # ------------------------------------------------------------
   
   Reescreva o código acima gerando a lista lstResultados utilizando List Comprehension 
   e depois escreva o resultado em um arquivo chamado 'resultados.csv' escrevendo cada 
   par (x e fx) em uma linha e separando x e fx por ;.
'''