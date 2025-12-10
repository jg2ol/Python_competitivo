# Maior valor, fácil
# link: https://neps.academy/br/exercise/2071

n = int(input())
m = int(input())
s = int(input())
I = []
cont = 0

for x in range(n, m+1):
    soma_alg = 0
    for alg in str(x):
        soma_alg += int(alg)
    if soma_alg == s:
        I.append(x)
    else:
        cont += 1

if cont == m - n + 1:
    print(-1)
else:
    print(I[len(I) - 1])