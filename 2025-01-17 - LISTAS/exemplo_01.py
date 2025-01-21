'''
   EXEMPLO 01:

   Fazer um programa que solicite ao usuário o nome e duas notas de um aluno. 

   O programa deverá parar de solicitar os dados dos alunos (nome e notas) quando o
   usuário digitar FIM no nome do aluno. 

   Após a digitação dos dados, o programa deverá exibir o nome do aluno, suas respectivas 
   notas e a média das notas (usar o cálculo da média do IFRN) e a situação do aluno 
   (Aprovado ou Reprovado) de acordo com os critérios de média do IFRN.   

   Lembre que o programa não deverá aceitar nome de aluno vazio e só deverá aceitar notas 
   entre 0 e 100. Lembre também que as notas são do tipo INTEIRO.
'''

lstAlunos = list()

while True:
   # Digitando o nome do aluno
   strNome = input('Digite o nome do aluno: ').upper().strip()

   # Verificando se o nome é FIM para sair do laço   
   if strNome == 'FIM': break

   # Verificando se o nome é vazio
   if strNome == '':
      print('Nome do aluno não pode ser vazio!')
      continue

   # Digitando a primeira nota do aluno
   intNota1 = int(input('Digite a primeira nota do aluno: '))

   # Verificando se a nota está entre 0 e 100
   if intNota1 < 0 or intNota1 > 100:
      print('Nota inválida! A nota deve estar entre 0 e 100.')
      continue

   # Digitando a segunda nota do aluno
   intNota2 = int(input('Digite a segunda nota do aluno: '))

   # Verificando se a nota está entre 0 e 100
   if intNota2 < 0 or intNota2 > 100:
      print('Nota inválida! A nota deve estar entre 0 e 100.')
      continue   

   # Adicionando os dados do aluno na lista
   lstAlunos.append([strNome, intNota1, intNota2])


# Exbindo os dados dos alunos
for aluno in lstAlunos:
   print(aluno)