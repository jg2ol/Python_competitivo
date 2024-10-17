# Manolo, O Minerador, médio
# 186
# link: https://neps.academy/br/exercise/186

n, q_maq = map(int, input().split())
precos = [float(x) for x in input().split()]
rendas = [float(x) for x in input().split()]

menor = precos[0]*rendas[0]
maior = precos[0]*rendas[0]
i_menor = 1
i_maior = 1
soma_rendas = 0

for x in range(0, n):
    soma_rendas += rendas[x]
    gx = precos[x]*soma_rendas
    if gx < menor:
        menor = gx
        i_menor = x + 1
    elif gx > maior:
        maior = gx
        i_maior = x + 1

menor = f"{menor*q_maq:.2f}"
maior = f"{maior*q_maq:.2f}"

print(i_maior, maior)
print(i_menor, menor)
