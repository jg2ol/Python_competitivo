# OBI 2020 - 2ª Fase, médio
# link: https://neps.academy/br/exercise/1022

c = int(input())
n = int(input())
lista = sorted([int(input()) for i in range(0, n)])

dist = [(lista[x+1] - lista[x-1])/2 for x in range(1, n-1)]
dist.insert(0, (lista[1] + lista[0])/2)
dist.append(c - lista[-1] + (lista[-1] - lista[-2])/2)

print(f"{min(dist):.2f}")
