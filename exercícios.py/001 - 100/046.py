# Troco em Moedas
# link: https://neps.academy/br/exercise/143

n = int(input())

cont_100 = 0
cont_50 = 0
cont_25 = 0
cont_10 = 0
cont_5 = 0
cont_1 = 0

while n >= 100:
    n -= 100
    cont_100 += 1
while n >= 50:
    n -= 50
    cont_50 += 1
while n >= 25:
    n -= 25
    cont_25 += 1
while n >= 10:
    n -= 10
    cont_10 += 1
while n >= 5:
    n -= 5
    cont_5 += 1
while n >= 1:
    n -= 1
    cont_1 += 1

lista = [cont_100, cont_50, cont_25, cont_10, cont_5, cont_1]
moedas = [sum(lista)]
for x in lista:
    moedas.append(x)

for x in moedas:
    print(x)