# Divisores de um Número, fácil
# 182

n = int(input())
divisores = []
div = ''
soma = 0

for x in range(1, n+1):
    if n % x == 0:
        divisores.append(x)

for y in divisores:
    div += f" {str(y)}"
    soma += y

print(f"{len(divisores)} divisor(es):{div}")
print(f"Soma de divisores = {soma}")
if len(divisores) == 2:
    print('Primo')
else:
    print('Nao primo')