# string's são qualquer sequência de caracteres bem definidos

str1 = "Olá MUNDO!"
print(str1)

# em python, tanto faz declarar strings com aspas simples ou duplas
# se uma string tiver aspas dentro de si podemos usar a barra invertida
# para que não haja confusão entre as aspas do texto e as de atribuição
str2 = "Então ele me disse: \"Eu achava que este era seu.\""
print(str2)

# .input() --> inserção de dados (tipo string)
nome = input('Seu nome: ')
print(f"Olá, {nome}.")

# podemos fatiar uma string chamando apenas o intervalo de caracteres que queremos
print(str1[1:5])
print(str1[1:7:2]) # dando "saltos" de 2 em 2
print(str1[::-1]) # invertendo a string

# .upper() --> retorna a string com todos as suas letras em maiúsculas
# .isupper() --> verifica se a string está em maiúsculas
up = str1.upper()
print(up)

# .lower() --> retorna a string com todos as suas letras em minúsculas
# .islower() --> verifica se a string está em minúsculas
low = str1.lower()
print(low)

# .strip() --> retorna a string sem os espaços à esquerda e à direita
# .lstrip() e .rstrip() assim como todas as variações L e R executam apenas à esquerda e à direita, respectivamente
str_aux = "     texto     "
print(str_aux.strip())
print(str_aux.lstrip())
print(str_aux.rstrip())

# .capitalize() --> retorna a string com apenas a primeira letra maiúscula
cap = str1.capitalize()
print(cap)

# .title() --> retorna a string com apenas as iniciais das palavras em maiúsculas
tit = str1.title()
print(tit)

# .split([separador]) --> retorna uma tupla com as fatias da string em toda ocorrência do separador
# obs: o separador não aparece em nenhuma parte da tupla
str3 = "Como é bom ter aulas com o Caio."
print(str3.split()[2]) # por padrão o separador será um espaço: " "
print(str3.split('a')[2])

# .replace() --> subsitui em todas as ocorrências uma substring por outra string
print(str1.replace("Olá", "Alô"))
print(str1.replace("O", "b"))

# .join() --> une string's de uma lista colocando uma string entre todas as pertencentes à lista
lista = ["bom", "dia", "à", "todos"]
str4 = " ".join(lista)
print(str4)

# .startswith() e .endswith() --> booleano que retorna True se começa ou termina com uma substring
print(str1)
print(str1.startswith("Olá"))
print(str1.endswith("MUNDO"))

# .find() --> retorna a primeira posição em que uma substring é encontrada em uma string, -1 se não há ocorrência
pos = str1.find("U")
print(pos)

# .count() --> retorna quantas vezes uma substring aparece em uma string
numero_de_b = str1.count("b")
print(numero_de_b)

# str.maketrans() --> cria um dicionário que serve como tradutor próprio a partir de duas strings de mesmo tamanho
alfabeto = "abcdefghijklmnopqrstuvwxyz"
corresp = "pmoniubyvtcrq wasdeefghjkl"
tradutor = str.maketrans(alfabeto, corresp)
print(tradutor)
print(type(tradutor))

# .translate() --> traduz/criptografa uma string de acordo com um tradutor criado ateriormente
# obs: sensível à minúsculas e maiúsculas
str5 = str2.translate(tradutor)
print(str5)
