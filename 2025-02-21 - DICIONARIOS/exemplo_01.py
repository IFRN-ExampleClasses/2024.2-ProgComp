import sys, requests

strURL = 'https://dados.ifrn.edu.br/dataset/7b48f9d0-205d-46b1-8225-a3cc7d3973ff/resource/fe0e9d2c-1c02-4625-b692-13edcc3380ae/download/dados_extraidos_recursos_cursos-ofertados.json'

response = requests.get(strURL)

if response.status_code != 200:
   sys.exit(f'\nErro ao acessar a URL...\nCódigo de erro: {response.status_code}\n')

print(response.json())
