'''
   EXEMPLO 02:

   Faça um programa que solicite um CPF e retorne o nome e a data de nascimento da pessoa.

   Caso o CPF não seja encontrado, exiba a mensagem 'CPF não encontrado'.
'''

dictPessoas = {
    '12345678901': ['João Silva', '15/05/1990'],
    '98765432100': ['Maria Oliveira', '22/11/1985'],
    '11223344556': ['Carlos Pereira', '30/01/1980'],
    '22334455667': ['Ana Souza', '05/07/1995'],
    '33445566778': ['Pedro Costa', '18/03/1988'],
    '44556677889': ['Luiza Almeida', '13/09/1992'],
    '55667788990': ['Fernanda Rocha', '25/12/1983'],
    '66778899001': ['Lucas Lima', '10/06/1997'],
    '77889900112': ['Mariana Santos', '02/04/1993'],
    '88990011223': ['Felipe Rodrigues', '14/08/1980']
}

strCPF = input('Digite o CPF: ')

if strCPF in dictPessoas.keys():
    print(f'Nome: {dictPessoas[strCPF][0]}')
    print(f'Data de Nascimento: {dictPessoas[strCPF][1]}')
else:
    print('CPF não encontrado')
