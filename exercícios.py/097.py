# Torres de Hanói
# link: https://neps.academy/br/exercise/337

c = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    c += 1
    print(f"Teste {c}")
    print(2**n - 1)
    print()
