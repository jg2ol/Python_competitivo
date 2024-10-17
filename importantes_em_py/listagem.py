# Imprimindo uma lista de compras utilizando formatação de string

produtos = ("Arroz", 5.50, "Feijão", 7.50, "Lápis", 1.00, "Borracha", 0.50, "Caneta", 1.00, "Computador", 850.00)

print("-"*40)
print(f"{"Tabela de preços":^40}")
print("-"*40)

for x in produtos:
    if produtos.index(x) % 2 == 0:
        valor = produtos[produtos.index(x) + 1]
        print(f"{x:.<30} R${valor:>7.2f}")
#       alinhado 7 casas p/ a esquerda com 2 pontos flutuantes
