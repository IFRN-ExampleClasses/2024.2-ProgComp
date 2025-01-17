'''
   EXEMPLO 02:
   A partir do código do Exemplo 01, faça as seguintes alterações:

   a) Ao sair do laço, informe quantos nomes há na lista;
   b) Caso o nome digitado após sair do laço exista na lista, 
      informe em qual posição ele está.
'''

lstNomes = list()

while True:
   strNome = input('Digite um nome ou FIM para encerrar: ').upper()
   if strNome == 'FIM': break
   lstNomes.append(strNome)

print(f'Foram digitados {len(lstNomes)} nomes.')

strNome = input('Digite um nome qualquer: ').upper()

if strNome in lstNomes:
   print(f'O nome {strNome} foi digitado anteriormente.')
   print(f'O nome {strNome} está na posição {lstNomes.index(strNome)}.')
else:
   print(f'O nome {strNome} não foi digitado anteriormente.')