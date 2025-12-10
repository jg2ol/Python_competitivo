# Palavras maldosas, médio
# link: https://neps.academy/br/exercise/2307

n = int(input())
palavras = []
palavras_mod = []
maior = ''
dic = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
dic_mod = {97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z'}
letras = []
junta_letras = []
soma_letras = []

for x in range(0, n):
    palavras.append(input())

for x in palavras:
    if len(x) > len(maior):
        maior = x

for x in palavras:
    while len(x) < len(maior):
        x += "0"
    palavras_mod.append(x)

for i in range(0, len(maior)):
    for j in range(0, n):
        letras.append(palavras_mod[j][i])
    a = ''
    for x in letras:
        a += str(x)
    letras = []
    junta_letras.append(a)

for x in junta_letras:
    soma_px = 0
    cont = n
    for y in x:
        if y in dic:
            soma_px += dic[y]
        else:
            cont -= 1
    soma_letras.append(int(soma_px//cont))

for x in soma_letras:
    print(dic_mod[x], end = "")