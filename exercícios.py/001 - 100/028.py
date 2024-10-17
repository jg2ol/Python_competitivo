# Consecutivos, médio
# link: https://neps.academy/br/exercise/110

numeros = []
valores = []
contadores = []

n = int(input())
for x in input().split():
    numeros.append(int(x))

cont = 1
for x in range(0, n - 1):
    if numeros[x] == numeros[x + 1] and x != n - 2:
        cont += 1
    elif x == n - 2 and numeros[n - 2] == numeros[n - 1]:
        cont += 1
        valores.append(numeros[x])
        contadores.append(cont)
        cont = 1
    else:
        valores.append(numeros[x])
        contadores.append(cont)
        cont = 1

maior = -1
for x in contadores:
    if x >= maior:
        maior = x

print(maior)