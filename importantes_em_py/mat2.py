# Insira os números e descubra o período da fração

a = input("Valor inicial: ")
r = int(input("Razão da P.G.: "))
q = int(input("Nº de alg. a serem considerados: ")) # Distância entre as somas

while r > len(a):
    a += "0"

op = int(input("Nº de operações (nº bem grande): "))
res = int(a)

temp = int(a)
for x in range(0, op):
    temp *= r
    res = res*10**q + temp

print(res)
