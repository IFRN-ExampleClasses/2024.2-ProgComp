'''
   Efetua uma requisição GET a uma URL e exibe o conteúdo JSON retornado.


   Utiliza a biblioteca requests para efetuar a requisição GET e exibir o 
   conteúdo JSON retornado.

   pip install requests --user   
'''

import sys, requests

# URL da API de Dados Abertos do IFRN
strURL = 'https://dados.ifrn.edu.br/dataset/7b48f9d0-205d-46b1-8225-a3cc7d3973ff/resource/fe0e9d2c-1c02-4625-b692-13edcc3380ae/download/dados_extraidos_recursos_cursos-ofertados.json'

# Efetua a requisição GET
response = requests.get(strURL)

# Verifica se a requisição foi bem sucedida
if response.status_code != 200:
   sys.exit(f'\nErro ao acessar a URL...\nCódigo de erro: {response.status_code}\n')

# Exibe o conteúdo JSON retornado
lstDadosGeral = response.json()

# Chaves que deseja extrair do dicionário de dados
dictChaves = {'codigo', 'descricao', 'carga_horaria', 'diretoria', 'eixo', 'modalidade', 'natureza_participacao'}

# Lista que armazenará os dados dos cursos
lstDadosCursos = [
    {chave: dicionario[chave] for chave in dictChaves if chave in dicionario} 
    for dicionario in lstDadosGeral
]

# Transforma a lista em um dicionário, usando 'codigo' como chave
dictDadosCursos = {dicionario['codigo']: dicionario for dicionario in lstDadosCursos}

# Exibe os dados dos cursos
for k, v in dictDadosCursos.items():   
   print(f'\n{k}: {v}')

print(f'\n{len(dictDadosCursos)} Cursos listados...\n')