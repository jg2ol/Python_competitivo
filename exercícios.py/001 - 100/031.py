# Substituição no Vetor, fácil
# 401

numeros = []
indices = []
menor = 10**100
ocorrencia = ''
mod = ''

for a in range(0, 10):
    numeros.append(int(input()))

for b in numeros:
    if b < menor:
        menor = b

for c in numeros:
    if c == menor and numeros.index(c) != numeros.index(menor):
        indices.append(numeros.index(c))

for x in indices:
    ocorrencia += f" {str(x)}"
#falta pegar os índices dos números que são numericamente iguais ao menor valor

numeros_mod = numeros
for y in numeros:
    if y == menor:
        numeros_mod[numeros.index(y)] = -1

for y in numeros_mod:
    mod += f"{str(y)} "

print(f"Menor: {menor}")
print(f"Ocorrências:{ocorrencia}")
print(mod)