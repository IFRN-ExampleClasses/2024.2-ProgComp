import os

# Obter o diretório atual
strDirAtual = os.path.dirname(__file__)

# Definir o nome do arquivo
strNomeArquivo = f'{strDirAtual}\\capitais_brasil.csv'

# Abrir o arquivo para leitura
arqEntrada = open(strNomeArquivo, 'r', encoding='utf-8')

# Ler o conteúdo do arquivo
lstConteudo = arqEntrada.readlines()

# Fechar o arquivo
arqEntrada.close()

# Tratando o conteúdo do arquivo
lstConteudo = [linha.strip().split(';') for linha in lstConteudo]

lstConteudo = list(map(lambda c: [c[0].replace('\'', ''), 
                             c[1].replace('\'', ''),
                             c[2].replace('\'', ''),
                             int(c[3])], lstConteudo))


# Imprimir o conteúdo do arquivo
print(lstConteudo)