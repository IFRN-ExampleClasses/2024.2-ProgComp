'''
   EXEMPLO 05:

   Adicionando um registro de pessoa em uma lista e em um dicionário.
'''

lstPessoas  = list()  
dictPessoas = dict()

strCPF      = input('Digite o CPF: ')
strNome     = input('Digite o Nome: ')
strDataNasc = input('Digite a Data de Nascimento: ')

lstPessoas.append([strCPF, strNome, strDataNasc])

dictPessoas[strCPF] = {'nome': strNome, 'data_nascimento': strDataNasc}