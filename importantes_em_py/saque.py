# código que diz quantas de cada cédula são necessárias para resultar num valor total

n = int(input("Qual o valor a sacar? R$"))
totced = 0
ced = 50
total = n

while True:
    while total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0

        if total == 0:
            break
