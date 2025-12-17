# lists[], o começo do poder

nomes = ["joao", "Gabriel", "pedro", "ana", "maria"]
print(nomes)
print(nomes[0])
print(nomes[-1])

# del --> deleta um elemento pelo seu índice
del nomes[1]
print(nomes)

# "atribuição composta" --> pega os elementos de um objeto e os coloca nas variáveis nomeadas
# precisa haver exatamente o mesmo número de variáveis e elementos do objeto
nome1, nome2, nome3, nome4 = nomes
print(nome1)
print(nome2)
print(nome3)
print(nome4)

# *var --> recebe todo o resto da lista
nome1, *resto = nomes
print(nome1)
print(resto)

# o fatiamento também funciona com listas
print(nomes[::-1])

# .append() --> insere um elemento ao final da lista
nomes.append("gabriel")

# .extend() --> insere os elementos de uma lista para outra
numeros = [1, 2, 3, 4]
nomes.extend(numeros)
print(nomes)

# .insert() --> adiciona um elemento a uma posição específica
nomes.insert(True, 1)
print(nomes)

# .remove() --> remove a primeira ocorrência de um elemento na lista
nomes.insert(2, 5.2)
nomes.insert(0, 5.2)
nomes.remove(5.2)

# .pop() --> remove um elemento da lista pelo seu índice
# remove o último elemento se não especificar índice
nomes.pop(1)
print(nomes)

# .sort() ou sorted() --> ordena os elementos da lista
nomes2 = ["joao", "Gabriel", "pedro", "ana", "maria"]
nomes = sorted(nomes2)
print(nomes2)

# .clear() --> esvazia a lista

# .reverse() --> inverte a ordem dos elementos da lista
nomes.reverse()
print(nomes)

# .index() --> retorna o índice da primeira ocorrência de um elemento na lista
# retorna erro se o procurado não pertencer à lista
print(nomes.index("ana"))

# a função enumarate() cria uma iterator que passa por pares ordenados (tuplas)
# em que o primeiro elemento é o índice e o segundo elemento é o valor
# enumerate() também aceita fatiamento
aux = enumerate(nomes)
list_aux = list(aux)
print(list_aux)
print(type(aux))
print(type(list_aux))

for a, b in aux:
    print(f"Na posição {a+1}, o elemento {b}.")

# a função zip() funciona da mesma maneira que a enumerate(), porém de forma genérica
# com quaisquer duas listas, cria pares ordenados dos elementos 1 a 1
devs = ["joao", "ana", "maria"]
ids = [34131, 11351, 976543]

zip_aux = zip(ids, devs)
print(type(zip_aux))

zip_list = list(zip_aux)
print(zip_list)

# list comprehension --> resumo de um código que cria uma lista
lista1 = [x for x in range(0, 21) if x%2 == 1]
print(lista1)

# filter() --> usa uma condição e uma lista para criar um iterável
def impar(x):
    return bool(x%2)

lista2 = list(filter(impar, range(0, 21)))
print(lista2)

# map() --> generalização da filter, ao invés de aceitar uma condição, a map()
# aplica uma função qualquer a items de um iterável
def afim(x):
    return 2*x-3

lista3 = list(map(afim, range(0, 21)))
print(lista3)

# código que recebe três strings e transforma para int
num1, num2, num3 = map(int, input("Digite três números: ").split())
print(num1, num2, num3)

# sum() --> soma dos elementos de um iterável, também aceita parâmetro que é somado à soma calculada
print(sum(lista3, start = 1)) # é o mesmo que sum(lista3) + 1
