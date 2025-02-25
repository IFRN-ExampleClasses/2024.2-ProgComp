import sys

try:
   dividendo = int(input('Digite o Dividendo: '))
   divisor   = int(input('Digite o Divisor..: '))
   quociente = dividendo / divisor
except ValueError:
   print('ERRO: Digite apenas números inteiros')
except ZeroDivisionError:
   print('ERRO: Divisão por zero')
except KeyboardInterrupt:
   print('\nAVISO: Operação interrompida pelo usuário')
except:
   print(f'ERRO: {sys.exc_info()[0]}\nEntre em contato com o suporte')
else:
   print(f'{dividendo} / {divisor} = {quociente}')