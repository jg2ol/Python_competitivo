# Sequência Lógica 02, médio
# link: https://neps.academy/br/exercise/180

list_a = []
list_b = []

for x in range(0, 31):
    list_a.append(x)
    list_a.append(x+1)
for y in range(1, 63):
    if y % 2 == 1:
        list_b.append(y)
    else:
        list_b.append(y-3)
for z in range(0, 62):
    print(f"a = {list_a[z]} <-> b = {list_b[z]}")