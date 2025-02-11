'''
   EXEMPLO 03:

   Faça um programa que solicite um CPF e retorne o nome e a data de nascimento da pessoa.

   Caso o CPF não seja encontrado, exiba a mensagem 'CPF não encontrado'.
'''

dictPessoas = {
    '12345678901': {'nome': 'João Silva', 'data_nascimento': '15/05/1990'},
    '98765432100': {'nome': 'Maria Oliveira', 'data_nascimento': '22/11/1985'},
    '11223344556': {'nome': 'Carlos Pereira', 'data_nascimento': '30/01/1980'},
    '22334455667': {'nome': 'Ana Souza', 'data_nascimento': '05/07/1995'},
    '33445566778': {'nome': 'Pedro Costa', 'data_nascimento': '18/03/1988'},
    '44556677889': {'nome': 'Luiza Almeida', 'data_nascimento': '13/09/1992'},
    '55667788990': {'nome': 'Fernanda Rocha', 'data_nascimento': '25/12/1983'},
    '66778899001': {'nome': 'Lucas Lima', 'data_nascimento': '10/06/1997'},
    '77889900112': {'nome': 'Mariana Santos', 'data_nascimento': '02/04/1993'},
    '88990011223': {'nome': 'Felipe Rodrigues', 'data_nascimento': '14/08/1980'}
}


strCPF = input('Digite o CPF: ')

if strCPF in dictPessoas.keys():
    print(f'Nome: {dictPessoas[strCPF]['nome']}')
    print(f'Data de Nascimento: {dictPessoas[strCPF]['data_nascimento']}')
else:
    print('CPF não encontrado')
