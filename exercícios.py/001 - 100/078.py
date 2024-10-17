# Próximo Caractere, fácil
# link: https://neps.academy/br/exercise/2011

n = int(input())
seq = input()
vazia = ''

for i in range(0, n-1):
    if seq[i + 1] == "J":
        print(seq[i])