# menor e maior valor digitado com suas respectivas posições em uma lista

lista = []

n = int(input("Digite a quantidade de termos da sua lista: "))
for x in range(0, n):
    lista.append(int(input(f"Digite um número para a posição {x + 1}: ")))

menor = maior = lista[0]
for x in lista:
    if x < menor:
        menor = x
    if x > maior:
        maior = x

print(f"O menor valor digitado foi {menor} e apareceu nas posições", end = " ")
for pos, x in enumerate(lista):
    if x == menor:
        print(f"{pos + 1}... ", end = "")
print()

print(f"O maior valor digitado foi {maior} e apareceu nas posições", end = " ")
for pos, x in enumerate(lista):
    if x == maior:
        print(f"{pos + 1}... ", end = "")
