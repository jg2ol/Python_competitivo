# Funções são relações que dão um retorno específico para cada entrada específica
# existem uma infinidade de funções próprias do python como int(), print(), ...
# porém, também podemos criar nossas próprias funções, de duas formas possíveis

# função definida --> damos um nome à uma função que criamos definidamente
def soma(a, b):
    return a+b

# funções lambda --> são relações não nomeadas e de uso instantâneo
# não há a necessidade de atribuir à uma variável pois perde o sentido de usar a função lambda

# geralmente usada em iteráveis
# estrutura: lambda [parâmetro]: [retorno]
lista1 = [1, 2, 3, 4, 5, 6]
squared_lista1 = list(map(lambda x: x*x, lista1))
# assim, map irá pegar os elementos da lista1 e elevar ao quadrado

print(lista1)
print(squared_lista1)

# também podemos pegar diretamente o return da lambda
resultado = (lambda x: x+2 if x%2 == 0 else x*x - 1)(3)
print(resultado)
