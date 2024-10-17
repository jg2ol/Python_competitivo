# Raízes, fácil
# 170

n = int(input())
numeros = input()
numero = []
for x in numeros.split():
    numero.append(float(x))
for x in range(0, n):
    raiz = numero[x]**(1/2)
    print(f"{raiz:.4f}")