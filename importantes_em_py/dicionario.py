# dicionário em ordem crescente

from random import randint
from time import sleep
from operator import itemgetter

jogo = {}
for x in range(0, 4):
    jogo[f"Jogador{x+1}"] = randint(1, 6)

for x, y in jogo.items():
    print(f"{x} tirou {y} no dado.")
    sleep(1)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
for x, y in enumerate(ranking):
    print(f"{x+1}º Lugar: {y[0]} com {y[1]}.")
