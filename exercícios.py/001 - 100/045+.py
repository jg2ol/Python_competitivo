# Soma de Frações, médio
# 268
# imprimir uma fração irredutível originada pela soma de outras duas

a, b, c, d = map(int, input().split())

n1 = a*d + c*b
n2 = b*d

anterior = n1
atual = n2
resto = anterior % atual
while resto != 0:
    anterior = atual
    atual = resto
    resto = anterior % atual

n1 = int(n1/atual)
n2 = int(n2/atual)

print(n1, n2)