# Robô de Fazenda, médio
# 128

bornes, num_comandos, desvastada = map(int, input().split())
ordem = input().split()
comandos = []
for x in ordem:
    comandos.append(int(x))

cont_devastada = 0
posicao = 1

if posicao == desvastada:
    cont_devastada += 1

for x in range(0, num_comandos):
    if comandos[x] == 1:
        posicao += 1
        if posicao == bornes + 1:
            posicao = 1
    else:
        posicao -= 1
    
    if posicao == 0:
        posicao = bornes

    if posicao == desvastada:
        cont_devastada += 1

print(cont_devastada)