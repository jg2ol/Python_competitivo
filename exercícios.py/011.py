# Critérios de Divisibilidade 3, médio
# 272

n = input()
soma_alg = 0
soma_alt = 0

for alg in range(0, len(n)):
    soma_alg += int(n[alg])
    if alg % 2 == 0:
        soma_alt += int(n[alg])
if (soma_alg-2*soma_alt) % 11 == 0:
    print('S')
else:
    print('N')