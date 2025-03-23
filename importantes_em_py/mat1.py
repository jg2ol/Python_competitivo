# Código que verifica a equação:
# 1/n = p'n/(10^α(p'n) - k), onde α(x) é o nº de algarismos de x

k = int(input("k: "))
p0 = input("p0: ")
r = len(p0)
p0 = int(p0)
q = int(input("q: "))
res = p0

for x in range(0, q):
    p0 *= k
    res = res*10**r + p0

print(res)
