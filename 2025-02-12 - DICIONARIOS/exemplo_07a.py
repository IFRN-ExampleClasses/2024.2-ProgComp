'''
   EXEMPLO 07:

   Usando o dicionário dictAlunos faça um programa que solicite ao usuário a matrícula de um 
   aluno:
   
    - Caso a matrícula não exista no dicionário, o programa deverá solicitar as duas notas 
    da disciplina e adicione os valores digitados no dicionário;

    - Caso a matrícula já exista no dicionário, o programa deverá exibir a mensagem "Matrícula já  existe!" 
    mostrar as notas cadastradas e solicitar as novas notas.  

   O programa deve continuar solicitando a matrícula e as notas até que o usuário digite a
   matrícula 0.

   Ao final, o programa deve exibir o dicionário dictAlunos.

   ADD: Salvar os dados em um arquivo (CSV) e em um arquivo JSON.
'''
import os, json

# Cria o dicionário
dictAlunos = dict()

# Obter o diretório atual
strDir = os.path.dirname(__file__)

while True:
   # Solicita a matrícula do aluno
   strMatricula = input('\nDigite a matrícula do aluno: ')

   # Se a matrícula for igual a '0', encerra o programa
   if strMatricula == '0': break
   
   # Se a matrícula já existir no dicionário, exibe as notas cadastradas
   if strMatricula in dictAlunos.keys():
      print('Matrícula já existe!')
      print('Notas cadastradas: ', dictAlunos[strMatricula])

   # Solicita as notas do aluno
   while True:
      intNota1 = int(input('Digite a primeira nota.: '))
      if intNota1 >= 0 and intNota1 <= 100: break

   while True:
      intNota2 = int(input('Digite a segunda nota..: '))
      if intNota2 >= 0 and intNota2 <= 100: break

   # Adiciona a matrícula e as notas no dicionário ou atualiza as notas
   dictAlunos[strMatricula] = [intNota1, intNota2]


# Exibe o dicionário
for matricula, notas in dictAlunos.items():
   #print(f'Aluno: {matricula} - Notas: {notas}')
   print(f'Aluno: {matricula} - Nota 1: {notas[0]} - Nota 2: {notas[1]}')

# Salvar os dados em um arquivo (CSV)
arqSaidaCSV = open(f'{strDir}\\alunos.csv', 'w', encoding='utf-8')
for matricula, notas in dictAlunos.items():
   arqSaidaCSV.write(f'{matricula};{notas[0]};{notas[1]}\n')
arqSaidaCSV.close()

# Salvar os dados em um arquivo (JSON)
arqSaidaJSON = open(f'{strDir}\\alunos.json', 'w', encoding='utf-8')
json.dump(dictAlunos, arqSaidaJSON, indent=3)
arqSaidaJSON.close()