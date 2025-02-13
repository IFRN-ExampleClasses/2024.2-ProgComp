import os, json

strDir = os.path.dirname(__file__)

arqEntrada = open(strDir + '\\alunos.json', 'r', encoding='utf-8')

dictAlunos = json.load(arqEntrada)

print(dictAlunos)