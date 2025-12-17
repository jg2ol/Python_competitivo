# dicionários: estrutura ideal para dados estruturados
# são úteis para criar um paralelo entre listas e outros iteráveis

dic = {"nome" : "joao", "idade": 17, "estudos": ["matemática"]}
print(dic)
print(type(dic))
print(dic["nome"])
print(dic["estudos"])

# .get() --> usado para acessar o valor de uma chave do dicionário mas sem retornar erro
# quando a chave não existir no dicionário
print(dic.get("idade")) # retorna dic["idade"], pois "idade" é uma chave de dic
print(dic.get("altura")) # retorna None
print(dic.get("altura", 1.7)) # retorna 1.7, como definimos

# .keys() --> iterável com todas as chaves presente no dicionário
# .values() --> iterável com todos os valores presente no dicionário
# .items() --> iterável com os pares chave-valor presentes no dicionário
print(dic.keys())
print(type(dic.keys()))
print(dic.values())
print(type(dic.values()))
print(dic.items())
print(type(dic.items()))

# .clear() --> esvazia o dicionário (remove todos os pares chave-valor)

# .pop() --> remove um par chave-valor pela chave e retorna o valor da chave
# assim como get(), pop() não retorna erro quando a chave não está presente e passamos um valor padrão
dic.pop("idade") # apaga o par ("idade", 17) de dic.items()
dic.pop("altura", 8) # não retorna erro apesar de "idade" não pertencer à dic.keys()
print(dic)

# .popitem() --> apaga o último par chave-valor inserido no dicionário
dic[2.7] = ("bom", "dia")
print(dic)
dic.popitem()
print(dic)

# .update() --> atualiza os valores do dicionário a partir de outro dicionário
# se uma chave está presente, seu valor é substituído, senão, o par chave-valor é adicionado ao dicionário
dic.update({"idade": 17, "estudos": ["matemática", "programação"]})
# adiciono "idade" (de volta) e atualizo "estudos"
print(dic)

# percorrendo os valores do dicionário com um contador começando em 1
for index, valor in enumerate(dic.items(), 1):
    print(index, valor)
