# Volume da TV, fácil
# link: https://neps.academy/br/exercise/319

lista = []

v, q = map(int, input().split())
for x in input().split():
    lista.append(int(x))

for x in lista:
    if x + v >= 100:
        v = 100
    else:
        v += x

print(v)