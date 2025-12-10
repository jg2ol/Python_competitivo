# Sedex Marciano, médio
# 234
# link: https://neps.academy/br/exercise/234
# condição para que um paralelepípedo de medidas l, a e c caiba dentro de uma esfera de raio r

l, a, c, r = map(int, input().split())
if l**2 + a**2 + c**2 <= 4*r**2:
    print('S')
else:
    print('N')