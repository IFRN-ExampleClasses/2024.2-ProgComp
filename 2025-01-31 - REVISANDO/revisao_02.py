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
import os

# Solicitando os coeficientes da equação da reta
intCoefAng = int(input('Informe o valor de a (coeficiente angular).: '))
intCoefLin = int(input('Informe o valor de b (coeficiente linear)..: '))

# Solicitando os valores inicial e final de x
intXInicial = int(input('Informe o valor inicial de x.: '))
intXFinal   = int(input('Informe o valor final de x...: '))

# Gerando a lista com os pares [x, f(x)]
lstFX = [[x, intCoefAng * x + intCoefLin] for x in range(intXInicial, intXFinal + 1)]

# Obtendo o diretório atual
strDirAtual = os.path.dirname(__file__)

# Escrevendo o resultado no arquivo 'resultados.csv'
arqSaida = open(f'{strDirAtual}\\resultados.csv', 'w')
for lstPar in lstFX:
    arqSaida.write(f'{lstPar[0]};{lstPar[1]}\n')
arqSaida.close()

# Exibindo a lista gerada
print(lstFX)