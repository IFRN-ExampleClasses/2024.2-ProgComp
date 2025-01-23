pessoas_concurso = [ ['Ana', 85, 30]    , ['João', 92, 25]    , ['Maria', 88, 27]   ,
                     ['Carlos', 75, 22] , ['Fernanda', 95, 28], ['Pedro', 85, 26]   ,
                     ['Laura', 70, 24]  , ['Roberto', 92, 29] , ['Patrícia', 78, 32],
                     ['Juliana', 80, 31], ['Lucas', 85, 23]  , ['Beatriz', 95, 28] ,
                     ['Felipe', 72, 21] , ['Carla', 90, 33]  , ['Ricardo', 85, 30] ,
                     ['Sofia', 78, 29]  , ['Rafael', 88, 26] , ['Larissa', 83, 30] ,
                     ['Gabriel', 90, 25], ['Vanessa', 91, 24] ]


classificacao_concurso = sorted(pessoas_concurso, key=lambda p: (p[1], p[2]), reverse=True)

for pessoa in classificacao_concurso:
    print(f'{pessoa[0]}: {pessoa[1]} pontos, {pessoa[2]} anos')