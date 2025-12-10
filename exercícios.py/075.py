# Fraseando
# link: https://neps.academy/br/exercise/1470

n = input()
a = n
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

st = []
for x in a:
    if x not in st:
        st.append(x)

code = {}
for i, x in enumerate(st):
    code[x] = alfabeto[i]

texto = []
for x in a:
    texto.append(code[x])

s = ""
for x in texto:
    s += x

print(s)
