# Tempo de Viagem em Segundos
# link: https://neps.academy/br/exercise/178

d1 = int(input())
h1 = int(input())
m1 = int(input())
d2 = int(input())
h2 = int(input())
m2 = int(input())

Dd = d2 - d1 - 1
Dh = 24 - h1 + h2 - 1
Dm = 60 - m1 + m2

print((Dd*24*60+Dh*60+Dm)*60)