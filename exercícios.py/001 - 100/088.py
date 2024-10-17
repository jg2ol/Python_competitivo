# Pew Pew Estático
# link: https://neps.academy/br/exercise/734

inim = []
tiros = []
mortos = 0

n = int(input())
for c in range(0, n):
    x, y = map(int, input().split())
    inim.append((x, y))

m = int(input())
for c in range(0, m):
    x, y = map(int, input().split())
    tiros.append((x, y))

for tiro in tiros:
    if tiro in inim:
        mortos += 1
        inim.remove(tiro)
vivos = n - mortos

print(f"vivos: {vivos}")
print(f"mortos: {mortos}")