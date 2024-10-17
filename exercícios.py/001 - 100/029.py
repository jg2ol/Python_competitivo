# Postes, fácil
# 41

n = int(input())
num_postes = input()
cont_c = 0
cont_s = 0

for x in num_postes.split():
    altura = int(x)
    if 85 > altura >= 50:
        cont_c += 1
    elif altura < 50:
        cont_s += 1
print(cont_s, cont_c)