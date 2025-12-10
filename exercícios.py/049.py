# Bolas, fácil
# link: https://neps.academy/br/exercise/373

b1, b2, b3, b4, b5, b6, b7, b8 = map(int, input().split())
bolas = [b1, b2, b3, b4, b5, b6, b7, b8]

cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0
cont_6 = 0
cont_7 = 0
cont_8 = 0
cont_9 = 0
cont_0 = 0
for x in bolas:
    if x == 1:
        cont_1 += 1
    elif x == 2:
        cont_2 += 1
    elif x == 3:
        cont_3 += 1
    elif x == 4:
        cont_4 += 1
    elif x == 5:
        cont_5 += 1
    elif x == 6:
        cont_6 += 1
    elif x == 7:
        cont_7 += 1
    elif x == 8:
        cont_8 += 1
    elif x == 9:
        cont_9 += 1
    else:
        cont_0 += 1

contadores = [cont_0, cont_1, cont_2, cont_3, cont_4, cont_5, cont_6, cont_7, cont_8, cont_9]
cont_m5 = 0
for x in contadores:
    if x > 4:
        cont_m5 += 1

if cont_m5 == 1:
    print("N")
else:
    print("S")