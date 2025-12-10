# O retorno do King, médio
# link: https://neps.academy/br/exercise/2108

s = input()

notas = []
for x in range(0, len(s)-1):
    if s[x] == "1":
        if s[x+1] == "0":
            notas.append(10)
        else:
            notas.append(1)
    else:
        if s[x] != "0":
            notas.append(int(s[x]))
if s[-1] != "0":
    notas.append(int(s[-1]))

media = f"{sum(notas)/len(notas):.2f}"
print(media)
