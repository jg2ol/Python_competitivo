# Inversão de uma String
# link: https://neps.academy/br/exercise/1782

n, a, b = map(int, input().split())
seq = input()

letras = []
inverso = ''

for x in seq:
    letras.append(str(x))

for x in range(b-1, a-2, -1):
    inverso += letras[x]

for x in range(0, a-1):
    print(letras[x], end = "")
print(inverso, end = "")
for x in range(b, n):
    print(letras[x], end = "")