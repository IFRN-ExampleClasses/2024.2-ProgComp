import os, json

strDir = os.path.dirname(__file__)

arqEntrada = open(strDir + '\\alunos.csv', 'r', encoding='utf-8')

dictAlunos = dict()

while True:
   strLinha = arqEntrada.readline().strip()
   if strLinha == '': break
   
   strLinha = strLinha.split(';')
   dictAlunos[strLinha[0]] = {'nota1': int(strLinha[1]), 'nota2': int(strLinha[2])} 

print('\n', dictAlunos, '\n')

for matricula, notas in dictAlunos.items():
    print(f'Matricula: {matricula} - Notas: {notas['nota1']} e {notas['nota2']}')