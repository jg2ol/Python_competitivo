# Estacionamento Ocupado, fácil
# link: https://neps.academy/br/exercise/2025

n = int(input())
ontem = input()
hoje = input()
cont = 0

for i in range(0, n):
    if hoje[i] == ontem[i] == "C":
        cont += 1

print(cont)