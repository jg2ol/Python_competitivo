# Telefone (PJ), fácil
# link: https://neps.academy/br/exercise/592

seq = input()
letras = []
telefone = ''
dic = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}

for x in seq.split("-"):
    letras.append(x)

for x in letras:
    for y in x:
        for z in dic.keys():
            if y in z:
                telefone += str(dic[z])
    if letras.index(x) != len(letras) - 1:
        telefone += "-"

print(telefone)