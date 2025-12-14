# sets (conjuntos) são "listas" não ordenadas em que um elemento só aparece uma vez

set1 = {5, 3, 2, 1, 4}
# obs: para criar um set vazio é necessário chamar a função set(), pois {} é um dicionário vazio
print(set1)
print(type(set1))

# .add() --> adiciona um elemento ao final do set, caso ele não já esteja presente
set1.add(6)
print(set1)
set1.add(1)
print(set1)

# .remove() ou .discard --> remove um elemento do set
# a diferença consiste no fato de discard não retornar erro caso o elemento não pertencer ao set
set1.remove(2)
set1.discard(5)
set1.discard(0)
print(set1)

# .clear() --> esvazia o set

# .issubset() --> retorna True se o set parametrado contém o set chamado
# .issuperset() --> retorna True se o set chamado contém o set parametrado
set2 = {1, 4, 3}
print(set2)

if set1.issubset(set2):
    print("set1 é um subconjunto de set2.")
else:
    print("set1 não é um subconjunto de set2.")

if set1.issuperset(set2):
    print("set1 contém set2.")
else:
    print("set1 não contém set2.")

# .isdisjoint() --> retorna True se os conjuntos não tiverem intersecções
if set1.isdisjoint(set2):
    print("set1 e set2 não têm elementos em comum.")
else:
    print("set1 e set2 têm elementos em comum.")

# Operações com conjuntos
# união (|) --> cria um novo conjunto com todos os elementos dos conjuntos unidos
print(set1 | set2)

# intersecção (&) --> elementos pertencentes ao dois conjuntos
print(set1 & set2)

# diferença (-) --> elementos em set1 que não pertencem a set2
print(set1 - set2)

# diferença simétrica (^) --> elementos em set1 ou em set2 mas não nos nois
# ou seja, set1|set2 - set1&set2
print(set1 ^ set2)
