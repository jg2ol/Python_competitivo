# cálculo do mdc entre dois números, o método mais rápido (método de Euclides)

a = int(input())
b = int(input())

anterior = a
atual = b
resto = anterior % atual

while resto != 0:
    anterior = atual
    atual = resto
    resto = anterior % atual

print(f"O mdc entre {a} e {b} é {atual}.")
