'''
   EXEMPLO 04:

   A partir da lista lstPessoas, gere um dicionário onde a chave é o CPF da pessoa (posição 0) 
   de cada sub-lista e o valor é um dicionário onde tem a chave 'nome' e seu valor é o 
   nome da pessoa (posição 1 da sub-lista) e outra chave 'data_nascimento' e seu valor é a 
   data de nascimento (posição 2 da sub-lista).
'''

lstPessoas = [
    ['12345678901', 'João Silva'      , '15/05/1990'],
    ['98765432100', 'Maria Oliveira'  , '22/11/1985'],
    ['11223344556', 'Carlos Pereira'  , '30/01/1980'],
    ['22334455667', 'Ana Souza'       , '05/07/1995'],
    ['33445566778', 'Pedro Costa'     , '18/03/1988'],
    ['44556677889', 'Luiza Almeida'   , '13/09/1992'],
    ['55667788990', 'Fernanda Rocha'  , '25/12/1983'],
    ['66778899001', 'Lucas Lima'      , '10/06/1997'],
    ['77889900112', 'Mariana Santos'  , '02/04/1993'],
    ['88990011223', 'Felipe Rodrigues', '14/08/1980']
]

# Criando o dicionário com dicionários como valores
dictPessoas = {pessoa[0]: {'nome': pessoa[1], 'data_nascimento': pessoa[2]} 
               for pessoa in lstPessoas}

print(dictPessoas)