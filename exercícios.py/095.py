# Iguais, médio
# link: https://neps.academy/br/exercise/1469

n = int(input())

soma = 0
maior = 0
for x in input().split():
    soma += int(x)
    if int(x) > maior:
        maior = int(x)

x = int(input())

if (soma + x)%n == 0 and (soma + x)/n >= maior:
    print("Boa Sorte")
else:
    print("Sem Sorte")
