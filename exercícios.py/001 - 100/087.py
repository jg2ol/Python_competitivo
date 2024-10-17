# Revisão de Contrato, médio
# link: https://neps.academy/br/exercise/238

while True:
    d, n = map(str, input().split())
    if d == n == "0":
        break
    else:
        valor = n.replace(d, "")
        if len(valor) == 0:
            print(0)
        else:
            print(int(valor))