# Carnaval, fácil
# 321

n1, n2, n3, n4, n5 = map(float, input().split())
notas = [n1, n2, n3, n4, n5]

menor = 11
maior = 0
for x in notas:
    if x < menor:
        menor = x
    if x > maior:
        maior = x
del notas[notas.index(menor)]
del notas[notas.index(maior)]
soma = 0
for x in notas:
    soma += x
print(f"{soma:.1f}")