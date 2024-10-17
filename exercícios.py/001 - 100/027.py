# Critérios de Divisibilidade 2, médio
# 263

n = input()
alg_n = []

for x in n:
    alg_n.append(int(x))

if len(n) == 1:
    if int(n) % 4 == 0:
        print('S')
    else:
        print('N')
    if int(n) % 9 == 0:
        print('S')
    else:
        print('N')
    if int(n) % 25 == 0:
        print('S')
    else:
        print('N')
else:
    num_2ud = alg_n[len(n)-2]*10 + alg_n[len(n)-1]
    if num_2ud % 4 == 0:
        print('S')
    else:
        print('N')
    if sum(alg_n) % 9 == 0:
        print('S')
    else:
        print('N')
    if num_2ud % 25 == 0:
        print('S')
    else:
        print('N')