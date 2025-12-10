# Prêmio do Milhão, fácil
# link: https://neps.academy/br/exercise/48

n = int(input())
dias = []
dias_y = []

for x in range(0, n):
    dias.append(int(input()))
    if sum(dias) >= 1000000:
        dias_y.append(len(dias))

print(dias_y[0])