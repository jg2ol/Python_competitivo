# Costa, médio
# 329
# link: https://neps.academy/br/exercise/329

m, n = map(int, input().split())
# m: número de colunas
# n: número de linhas

mapa = []
for x in range(0, m):
    linhax = []
    for y in input():
        linhax.append(y)
    mapa.append(linhax)

cont_costeira = 0
for x in mapa:
    if mapa.index(x) == 0:
        for y in x:
            if y == '#':
                cont_costeira += 1
    elif mapa.index(x) == n-1:
        for y in x:
            if y == '#':
                cont_costeira += 1
    else:
        for y in x:
            if x.index(y) == 0:
                if y == '#':
                    cont_costeira += 1
            elif x.index(y) == m-1:
                if y == '#':
                    cont_costeira += 1
            else:
                if y == '#':
                    sup = mapa[mapa.index(x)-1][x.index(y)]
                    inf = mapa[mapa.index(x)+1][x.index(y)]
                    esq = mapa[mapa.index(x)][x.index(y)-1]
                    dir = mapa[mapa.index(x)][x.index(y)+1]
                    if sup == '.' or inf == '.' or esq == '.' or dir == '.':
                        cont_costeira += 1

for x in mapa:
    print(x)

print()
print(cont_costeira)