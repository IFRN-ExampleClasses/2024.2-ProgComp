import os, sys

strDir = os.path.dirname(__file__)

strArquivo = f'{strDir}/arquivo.txt'

try:
   arqEntrada = open(strArquivo, 'r', encoding='utf-8')
except FileNotFoundError:
   print(f'ERRO: Arquivo não encontrado')
except:
   print(f'ERRO:`{sys.exc_info()[0]}`')
else:
   strConteudo = arqEntrada.read()
   arqEntrada.close()
   print(strConteudo)