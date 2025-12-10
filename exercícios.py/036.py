# Escada Rolante, médio
# 325

n = int(input())
tempos = []
soma = 0

for x in range(0, n):
    tempos.append(int(input()))

for x in tempos:
    if tempos.index(x) < len(tempos)-1:
        prox = tempos[tempos.index(x)+1]
        d = prox - x
        if d >= 10:
            soma += 10
        else:
            soma += d
    else:
        soma += 10

print(soma)