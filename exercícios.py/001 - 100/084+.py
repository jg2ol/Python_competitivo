# Como fica o nome?, fácil
# link: https://neps.academy/br/exercise/1947

n = int(input())
for x in range(0, n):
    seq = input().split()
    t = int(seq[0])
    nome = ""
    letras = []

    for x in seq[1:]:
        nome += f" {x}"
    nome = nome.strip()

    for x in nome:
        letras.append(x)
    
    t = t % len(nome)

    for x in range(0, t):
        a = letras[0]
        del letras[0]
        letras.append(a)
    
    vazia = ""
    for x in letras:
        vazia += str(x)
    print(vazia)

# site paia