import random, sys

lstNumeros = [random.randint(1, 100) for i in range(20)]

print(lstNumeros)

try:
   posicao = int(input('Digite a posição do número que deseja visualizar: '))
   print(lstNumeros[posicao])
except ValueError:
   print('Digite um número inteiro.')
except IndexError:
   print(f'ERRO: Posição inválida... Informe um valor entre 0 e {len(lstNumeros)-1}.')
except:
   print(f'ERRO: Ocorreu um erro inesperado...{sys.exc_info()[0]}')
else:
   print('Tudo certo!')