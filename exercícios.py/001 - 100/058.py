# Álbum da Copa, fácil
# link: https://neps.academy/br/exercise/163

n = int(input())
m = int(input())
figurinhas = []
cont_num = 0
cont = []

for x in range(0, m):
    figurinhas.append(int(input()))

print(n - len(set(figurinhas)))