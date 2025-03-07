import sys, funcoes

try:
   a = float(input('Digite o valor de A: '))
   b = float(input('Digite o valor de B: '))
   c = float(input('Digite o valor de C: '))
except ValueError:
   sys.exit('Digite apenas números!')
except:
   sys.exit(sys.exc_info()[0])
else:
   fltDelta = funcoes.delta(a, b, c)
   
   if not fltDelta[0]:
      sys.exit(f'ERRO: {fltDelta[1]}')

   raizes = funcoes.raizesEq2Grau(a, b, fltDelta[1])

   if not raizes[0]:
      sys.exit(f'ERRO: {raizes[1]}')

   print(f'Raiz 1: {raizes[1]}')
   print(f'Raiz 2: {raizes[2]}')