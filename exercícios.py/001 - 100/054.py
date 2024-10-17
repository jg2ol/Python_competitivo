# Garçom, fácil
# link: https://neps.academy/br/exercise/324

n = int(input())

copos_quebrados = 0
for x in range(0, n):
    l, c = map(int, input().split())
    if l > c:
        copos_quebrados += c

print(copos_quebrados)