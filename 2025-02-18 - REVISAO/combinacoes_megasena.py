import os, random, sys

# Diretório do aplicativo
strDirApp = os.path.dirname(__file__)

# Solicitando a quantidade de dezenas a serem sorteadas
n = int(input('Quantas dezenas deseja sortear? '))

# Verificando se o número de dezenas está entre 7 e 60
if n < 7 or n > 60:
   sys.exit('ERRO: O número de dezenas deve ser entre 7 e 60')

# Lista com todas as dezenas entre 1 e 60 (inclusive)
lstDezenas     = [x for x in range(1, 61)]

# Lista com as dezenas escolhidas aleatoriamente sem repetição e ordenadas
lstEscolhidos = random.sample(lstDezenas, n)
lstEscolhidos.sort()

# Escrevendo as dezenas escolhidas em um arquivo
arqSaida = open(f'{strDirApp}\\numeros_escolhidas.txt', 'w', encoding='utf-8')
strLinha = ' '.join([str(dezena) for dezena in lstEscolhidos]) + '\n'
arqSaida.close()

# Lista para armazenar as combinações
lstCombinacoes = list()

# Arquivo de saída
arqSaida = open(f'{strDirApp}\\combinacoes.csv', 'w', encoding='utf-8')

# Gerando as combinações
for d1 in range(len(lstEscolhidos)):
   for d2 in range(d1 + 1, len(lstEscolhidos)):
      for d3 in range(d2 + 1, len(lstEscolhidos)):
         for d4 in range(d3 + 1, len(lstEscolhidos)):
            for d5 in range(d4 + 1, len(lstEscolhidos)):
               for d6 in range(d5 + 1, len(lstEscolhidos)):
                  # Montando a linha
                  lstAuxiliar = [lstEscolhidos[d1], lstEscolhidos[d2], lstEscolhidos[d3], 
                                 lstEscolhidos[d4], lstEscolhidos[d5], lstEscolhidos[d6]]
                  strLinha = ';'.join([str(dezena) for dezena in lstAuxiliar]) + '\n'
                  # Escrevendo a linha no arquivo                  
                  arqSaida.write(strLinha)

# Fechando o arquivo
arqSaida.close()