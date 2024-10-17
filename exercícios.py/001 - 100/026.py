# Dia de Esportes, fácil
# 2015

n = int(input())
k = int(input())
s = input()
cont_R = 0
for x in s:
    if x == 'R':
        cont_R += 1
if cont_R < k:
    print('R')
else:
    print('W')