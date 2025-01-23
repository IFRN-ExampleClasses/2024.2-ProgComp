capitais_ne = [   ['Aracaju', 664906],
                  ['Salvador', 2886698],
                  ['Fortaleza', 2670757],
                  ['São Luís', 1182025],
                  ['Natal', 892211],
                  ['Recife', 1645727],
                  ['João Pessoa', 817511],
                  ['Maceió', 1038382],
                  ['Teresina', 892661] ]

# Ordenando a lista de capitais do Nordeste pela população
capitais_ne.sort(key=lambda x: x[1], reverse=True)

for capital in capitais_ne:
    print(capital)


