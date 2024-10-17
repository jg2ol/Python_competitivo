# 3n+1, fácil
# link: https://neps.academy/br/exercise/1757

n = int(input())
sequencia = []
sequencia.append(n)

while n != 1:
    if n % 2 == 0:
        n = int(n/2)
    else:
        n = 3*n + 1
    sequencia.append(n)

print(len(sequencia))