import os

# Obter o diretório atual
strDirAtual = os.path.dirname(__file__)

# Definir o nome do arquivo
strNomeArquivo = f'{strDirAtual}\\capitais_brasil.csv'

# Abrir o arquivo para leitura
arqEntrada = open(strNomeArquivo, 'r', encoding='utf-8')

# Ler o conteúdo do arquivo
strConteudo = arqEntrada.read()

# Fechar o arquivo
arqEntrada.close()

# Imprimir o conteúdo do arquivo
print(strConteudo)