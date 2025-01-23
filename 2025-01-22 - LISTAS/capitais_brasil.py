capitais_br = [['Rio Branco', 'AC', 'N', 413418]      , ['Maceió', 'AL', 'NE', 1038382], 
               ['Manaus', 'AM', 'N', 2192407]         , ['Salvador', 'BA', 'NE', 2886698], 
               ['Fortaleza', 'CE', 'NE', 2670757]     , ['Vitória', 'ES', 'SE', 3658553], 
               ['Goiânia', 'GO', 'CO', 1559473]       , ['São Luís', 'MA', 'NE', 1182025], 
               ['Cuiabá', 'MT', 'CO', 618124]         , ['Campo Grande', 'MS', 'CO', 877028], 
               ['Belo Horizonte', 'MG', 'SE', 2521564], ['Belém', 'PA', 'N', 1700000],
               ['João Pessoa', 'PB', 'NE', 817511]    , ['Curitiba', 'PR', 'S', 1963726], 
               ['Recife', 'PE', 'NE', 1645727]        , ['Teresina', 'PI', 'NE', 892661], 
               ['Rio de Janeiro', 'RJ', 'SE', 6747815], ['Natal', 'RN', 'NE', 892211],
               ['Porto Alegre', 'RS', 'S', 1484980]   , ['Porto Velho', 'RO', 'N', 539354], 
               ['Boa Vista', 'RR', 'N', 436000]       , ['Florianópolis', 'SC', 'S', 508826], 
               ['São Paulo', 'SP', 'SE', 12325232]    , ['Aracaju', 'SE', 'NE', 664906], 
               ['Palmas', 'TO', 'N', 306296]          , ['Brasília', 'DF', 'CO', 3015268] ]

# Ordena a lista de capitais por população de forma decrescente
capitais_br.sort(key=lambda x: x[3], reverse=True)

# Filtra as capitais de uma determinada região
regiao = 'SE'

'''
# Usando FOR
capitais_filtro = list()
for capital in capitais_br:
   if capital[2] == regiao:
      capitais_filtro.append(capital)
'''

'''
# Usando LIST COMPREHENSION
capitais_filtro = [capital for capital in capitais_br if capital[2] == regiao]
'''

# Usando FILTER
capitais_filtro = list(filter(lambda x: x[2] == regiao, capitais_br))

# Imprime a lista de capitais
for capital in capitais_filtro:
   print(capital)