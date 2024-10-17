# Alarme Despertador, médio
# 222

n = int(input())
tempos = []

for x in range(0, n):
    h1, m1, h2, m2 = map(int, input().split())

    if h2 >= h1 and m2 >= m1:
        dh = h2 - h1
        dm = m2 - m1

    elif h2 >= h1 and m2 < m1:
        if h2 != h2:
            h1 += 1
            if h1 == 24:
                h1 = 0
            dh = h2 - h1
            dm = 60 - m1 + m2
        else:
            dh = 23
            dm = 60 - m1 + m2

    elif h2 < h1 and m2 >= m1:
        dh = h1 - h2 + 60
        dm = m2 - m1

    elif h2 < h1 and m2 < m1:
        h1 += 1
        if h1 == 24:
            h1 = 0
        dh = h2 - h1
        dm = 60 - m1 + m2
    
    tempos.append(dh*60 + dm)

for x in tempos:
    if x != 0:
        print(x)
    else:
        print()