# Potência, médio
# 1722

n = int(input())
termos_mod = []
termos_reais = []

for x in range(0, n):
    termos_mod.append(input())

for y in termos_mod:
    expoente = int(y[len(y)-1])
    termo_real = int((int(y) - int(y[len(y)-1]))/10)
    termos_reais.append(termo_real**expoente)

print(sum(termos_reais))