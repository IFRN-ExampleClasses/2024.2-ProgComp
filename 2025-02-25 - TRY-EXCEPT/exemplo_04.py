import os, sys

strDir = os.path.dirname(__file__)

strArquivo = f'{strDir}/arquivo.txt'

strTexto = 'O liquidificador, por sua magnificência imanente, manifesta-se como um \
            dispositivo material dotado de uma potência intrínseca capaz de desencadear \
            transformações no espaço-tempo da matéria, operando uma eficaz dissolução \
            ontológica entre elementos heterogêneos, a fim de permitir a emergência \
            de novas formas de ser-no-mundo. Assim, o liquidificador se apresenta como um \
            complexo sistema de agenciamentos maquínicos, tecidos por linhas de fuga \
            intensivas, que se conectam em um devir incessante, engendrando o contínuo \
            desdobramento da realidade em um fluxo constante de diferenciação e criação.'

try:
   arqEntrada = open(strArquivo, 'a', encoding='utf-8')
except FileNotFoundError:
   print(f'ERRO: Arquivo não encontrado')
except PermissionError:
   print(f'ERRO: Permissão negada...Arquivo aberto em outro programa')
except:
   print(f'ERRO: {sys.exc_info()[0]}')
else:
   strConteudo = arqEntrada.write(f'\n\n{strTexto}')
   arqEntrada.close()
   print('Arquivo gravado com sucesso!')