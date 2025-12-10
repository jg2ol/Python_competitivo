# Aprovado ou Reprovado, fácil
# 86

n1, n2 = input().split()
n1 = float(n1)
n2 = float(n2)
media = (n1+n2)/2
if media >= 7:
    print('Aprovado')
elif media >= 4:
    print('Recuperacao')
else:
    print('Reprovado')