# Lâmpadas, médio
# link: https://neps.academy/br/exercise/52

n = int(input())
cont_l1 = 0
cont_l2 = 0

seq_int = []
for x in input().split():
    seq_int.append(int(x))

for x in seq_int:
    if x == 1:
        cont_l1 += 1
    elif x == 2:
        cont_l1 += 1
        cont_l2 += 1

print(cont_l1 % 2)
print(cont_l2 % 2)