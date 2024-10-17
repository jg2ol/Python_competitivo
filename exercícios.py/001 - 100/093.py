# Quadrado Mágico (OBI 2011), médio
# link: https://neps.academy/br/exercise/537

quadrado = []
n = int(input())

for x in range(0, n):
    linha = []
    for a in input().split():
        linha.append(int(a))
    quadrado.append(linha)

cont = 0
dp = []
ds = []
soma = sum(quadrado[0])
for i in range(0, n):
    coluna = []
    if sum(quadrado[i]) == soma:
        cont += 1
    
    dp.append(quadrado[i][i])
    ds.append(quadrado[n - i - 1][i])
    
    for ind in range(0, n):
        coluna.append(quadrado[ind][i])
    if sum(coluna) == soma:
        cont += 1

if sum(dp) == sum(ds) == soma:
    cont += 2

if cont == 2*(n+1):
    print(soma)
else:
    print(0)
