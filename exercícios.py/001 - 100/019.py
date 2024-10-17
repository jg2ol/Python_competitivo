# Pontuação por Atividades, difícil
# 2695

e = int(input())
a = int(input())
c = int(input())
pontos = e*2 + a*3 + c*5
if pontos >= 200:
    print('O')
elif pontos >= 150:
    print('S')
elif pontos >= 100:
    print('B')
else:
    print('N')