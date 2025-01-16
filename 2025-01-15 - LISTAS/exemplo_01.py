'''
   EXEMPLO 01:
   Fazer um programa que nomes de pessoas ao usuário. O programa deverá parar de
   solicitar quando o usuário digitar FIM.
   
   Em seguida o programa deverá solicitar um nome de uma pessoa qualquer e 
   informar se esse nome consta nos nomes digitados anterioremente ou não.
'''

lstNomes = list()

while True:
   strNome = input('Digite um nome ou FIM para encerrar: ').upper()
   if strNome == 'FIM': break
   lstNomes.append(strNome)

strNome = input('Digite um nome qualquer: ').upper()

if strNome in lstNomes:
   print(f'O nome {strNome} foi digitado anteriormente.')
else:
   print(f'O nome {strNome} não foi digitado anteriormente.')