# Huaauhahhuahau, médio
# link: https://neps.academy/br/exercise/118

risada = input()
vogais = ''
contrario = ''

for x in risada:
    if x in "aeiou":
        vogais += str(x)

for x in vogais[::-1]:
    contrario += str(x)

if vogais == contrario:
    print("S")
else:
    print("N")