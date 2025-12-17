# tuplas são como listas porém imutáveis

tupla = ("bom", 1, "dia", 1, 1, "3")
print(tupla)
print(type(tupla))
print(tupla[0])
print(tupla[-1])

# a variável que receber atribuição composta com asterísco será uma lista
aux1, *aux2 = tupla
print(aux1)
print(aux2)

# fatiamento
print(tupla[::-1])

# .count() --> retorna o número de vezes que um elemento aparece na tupla
print(tupla.count(1))
print(tupla.count(2))

# .index() --> retorna o índice da primeira ocorrência de um elemento da tupla ou erro caso não pertença
# aceita parâmetros de início e fim (fatiamento de busca)
print(tupla.index(1))
print(tupla.index(1, 3)) # procura a partir do índice 3
print(tupla.index(1, 2, 5))

# uso de sorted()
tupla2 = ("bom", "dia", "oi", "joao", "gabriel", "maria")
print(sorted(tupla2, key = len, reverse = True))
