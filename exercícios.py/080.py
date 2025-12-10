# Calculando, médio
# link: https://neps.academy/br/exercise/647

m = int(input())
cont = 1
while m != 0:
    if cont > 1:
        print()
    print(f"Teste {cont}")

    exp = input()
    numero = exp.split("+")
    numeros = []
    for x in numero:
        for y in x.split("-"):
            numeros.append(int(y))

    for x in exp:
        if x == "-":
            numeros[(exp.index(x)-1)//2 + 1] *= -1
    print(numeros)
    
    print(sum(numeros))
    cont += 1
    m = int(input())