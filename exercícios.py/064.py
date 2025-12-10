# Soma do Vetor, fácil
# link: https://neps.academy/br/exercise/326

n = int(input())
vetor = []

for x in input().split():
    vetor.append(int(x))

print(sum(vetor))