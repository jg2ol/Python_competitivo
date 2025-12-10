# Pesos, médio
# link: https://neps.academy/br/exercise/204

n = int(input())
pesos = []
cont_me8 = 0
cont_ma8 = 0

for x in input().split():
    pesos.append(int(x))

for x in range(0, n-1):
    if pesos[0] > 8:
        print("N")
        break
    elif pesos[x+1] - pesos[x] > 8:
        cont_ma8 += 1
    else:
        cont_me8 += 1

if cont_ma8 >= 1:
    print("N")
if cont_me8 == n-1:
    print("S")