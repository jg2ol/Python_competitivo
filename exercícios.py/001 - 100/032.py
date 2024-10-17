# Critérios de Divisibilidade 1, médio
# 266

n = input()
soma = 0

if int(n[len(n)-1]) % 2 == 0:
    print('S')
else:
    print('N')

for x in n:
    soma += int(x)
if soma % 3 == 0:
    print('S')
else:
    print('N')

if int(n[len(n)-1]) % 5 == 0:
    print('S')
else:
    print('N')