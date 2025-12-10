# Quadrado Mágico (OBI 2007), médio
# link: https://neps.academy/br/exercise/236

n = int(input())
quadrado = []
somas = []

for x in range(0, n):
    linha = []
    soma = 0
    for num in input().split():
        soma += int(num)
        linha.append(int(num))
    somas.append(soma)
    quadrado.append(linha)

somadp = 0
somads = 0
for x in range(0, n):
    soma = 0
    for y in range(0, n):
        soma += quadrado[y][x]
    somas.append(soma)
    somadp += quadrado[x][x]
    somads += quadrado[n-1-x][x]
somas.append(somadp)
somas.append(somads)

cont = somas.count(somas[0])
if cont == 2*(n+1):
    print(somas[0])
else:
    print(-1)
