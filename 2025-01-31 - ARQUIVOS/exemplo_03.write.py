import os

# Obter o diretório atual
strDirAtual = os.path.dirname(__file__)

# Definir o nome do arquivo de entrada
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

# Criando um set contendo as regiões
setRegioes = set(map(lambda x: x[2], lstConteudo))

# Criar o arquivo de saída
strNomeArquivo = f'{strDirAtual}\\populacao_capitais_regiao.csv'
arqSaida = open(strNomeArquivo, 'w', encoding='utf-8')
arqSaida.write('Região;População\n')
for strRegiao in setRegioes:
   lstFiltro     = filter(lambda x: x[2] == strRegiao, lstConteudo)
   intPolulacao  = sum(map(lambda x: x[3], lstFiltro))
   arqSaida.write(f'{strRegiao};{intPolulacao}\n')
arqSaida.close()
