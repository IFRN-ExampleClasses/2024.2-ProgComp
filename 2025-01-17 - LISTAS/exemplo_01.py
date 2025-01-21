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
import os, keyboard

lstAlunos = list()

strAviso  = '\nPressione qualquer tecla para continuar...'

# ----------------------------------------------------------------------
# Laço para digitar os dados dos alunos
while True:
   # Limpando a tela
   os.system('cls' if os.name == 'nt' else 'clear')

   # Digitando o nome do aluno
   strNome = input('Digite o nome do aluno: ').upper().strip()

   # Verificando se o nome é FIM para sair do laço   
   if strNome == 'FIM': break

   # Verificando se o nome é vazio
   if strNome == '':
      print(f'Nome do aluno não pode ser vazio!{strAviso}')
      keyboard.read_event()
      continue

   # Digitando a primeira nota do aluno e Verificando se a nota está entre 0 e 100
   while True:
      intNota1 = int(input('Digite nota da Etapa 1: '))
      if intNota1 < 0 or intNota1 > 100:
         print(f'Nota inválida! A nota deve estar entre 0 e 100!{strAviso}')
         keyboard.read_event()
      else:
         break

   # Digitando a segunda nota do aluno e Verificando se a nota está entre 0 e 100
   while True:
      intNota2 = int(input('Digite nota da Etapa 2: '))
      if intNota2 < 0 or intNota2 > 100:
         print(f'Nota inválida! A nota deve estar entre 0 e 100!{strAviso}')
         keyboard.read_event()
      else:
         break   

   # Adicionando os dados do aluno na lista
   lstAlunos.append([strNome, intNota1, intNota2])


# ----------------------------------------------------------------------
# Laço para exibir os dados dos alunos e calcular a média e a situação de cada aluno
for aluno in lstAlunos:
   # Calculando a média do aluno
   fltMedia = (aluno[1]*2 + aluno[2]*3) / 5

   # Verificando a situação do aluno
   strSituacao = 'REPROVADO'
   if fltMedia >= 59.5: strSituacao = 'APROVADO'

   # Exibindo os dados do aluno
   print(f'Aluno: {aluno[0]} | E1: {aluno[1]} | E2: {aluno[2]} | MF: {fltMedia:.0f} ({strSituacao})')