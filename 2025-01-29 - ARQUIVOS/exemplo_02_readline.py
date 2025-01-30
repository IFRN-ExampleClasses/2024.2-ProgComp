import os

# Obter o diretório atual
strDirAtual = os.path.dirname(__file__)

# Definir o nome do arquivo
strNomeArquivo = f'{strDirAtual}\\capitais_brasil.csv'

# Abrir o arquivo para leitura
arqEntrada = open(strNomeArquivo, 'r', encoding='utf-8')

# Ler o conteúdo do arquivo
lstConteudo = list()
while True:
   linha = arqEntrada.readline()

   # Verificar se o arquivo chegou ao final
   if not linha:break

   # Adicionando o conteúdo da linha na lista
   linha = linha.strip().split(';')
   lstConteudo.append([ linha[0].replace('\'', ''), 
                        linha[1].replace('\'', ''),
                        linha[2].replace('\'', ''),
                        int(linha[3])])

# Fechar o arquivo
arqEntrada.close()

# Imprimir o conteúdo do arquivo
print(lstConteudo)