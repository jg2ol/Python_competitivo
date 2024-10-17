# Função Fatorial, fácil
# link: https://neps.academy/br/exercise/174

def fatorial(N):
    fatorial = 1
    for x in range(1, N+1):
        fatorial *= x
    return(fatorial)

n = int(input())
print(fatorial(n))