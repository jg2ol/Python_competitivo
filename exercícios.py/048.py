# Cofrinhos da Vó Vitória, fácil
# link: https://neps.academy/br/exercise/635

n = int(input())
cont = 1
while n > 0:
    if n == 0:
        break
    else:
        print()

    joao = []
    ze = []
    diferencas = []
    
    print(f"Teste {cont}")
    for x in range(0, n):
        j, z = map(int, input().split())
        joao.append(j)
        ze.append(z)
        diferencas.append(j-z)
        print(sum(diferencas))
    
    cont += 1
    n = int(input())