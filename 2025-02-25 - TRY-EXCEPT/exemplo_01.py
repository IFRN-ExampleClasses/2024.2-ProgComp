import sys, math

try:
   valor = int(input('Digite um valor: '))
except:
   print('Valor inválido')
   print(f'Erro: {sys.exc_info()}')
else:
   print(f'O fatotial de {valor} é {math.factorial(valor)}')

