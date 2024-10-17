# Xor Space
# link: https://neps.academy/br/exercise/1352

n = input()

for x in n:
    if x == x.upper():
        n = n.replace(x, x.lower())
    elif x == x.lower():
        n = n.replace(x, x.upper())

print(n)