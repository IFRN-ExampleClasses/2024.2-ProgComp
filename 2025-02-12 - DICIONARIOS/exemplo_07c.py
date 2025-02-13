import os, json

strDir = os.path.dirname(__file__)

arqEntrada = open(strDir + '\\alunos.csv', 'r', encoding='utf-8')

dictAlunos = dict()

while True:
   strLinha = arqEntrada.readline().strip()
   if strLinha == '': break
   
   strLinha = strLinha.split(';')
   dictAlunos[strLinha[0]] = [int(strLinha[1]), int(strLinha[2])]

print('\n', dictAlunos, '\n')

for matricula, notas in dictAlunos.items():
    print(f'Matricula: {matricula} - Notas: {notas[0]} e {notas[1]}')