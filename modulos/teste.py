# PROGRAMA PRINCIPAL

from funcoes_uteis import numeros as num

preco = float(input("Digite o preço: R$"))
aumento = float(input("Aumento: "))
reducao = float(input("Redução: "))
num.resumo(preco, aumento, reducao)
