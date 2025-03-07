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

   if not fltDelta:
      sys.exit('ERRO: Delta não pode ser calculado')

   raizes = funcoes.raizesEq2Grau(a, b, fltDelta)
   print(raizes)