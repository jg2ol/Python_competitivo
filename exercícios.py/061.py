# Vestibular, fácil
# link: https://neps.academy/br/exercise/160

n = int(input())
gabarito = input()
aluno = input()
acertos = 0

i = 0
while i < n:
    if gabarito[i] == aluno[i]:
        acertos += 1
    i += 1

print(acertos)