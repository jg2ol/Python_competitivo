# Tesouro, fácil
# link: https://neps.academy/br/exercise/2161

n, x, y = map(int, input().split())
seq = input()

for a in seq:
    if a == "C":
        x -= 1
    elif a == "B":
        x += 1
    elif a == "D":
        y += 1
    elif a == "E":
        y -= 1

print(x, y)