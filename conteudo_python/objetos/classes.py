# CLasses --> codificação de objetos
# Objetos --> objetos são tudo o que quisermos! (listas, dicionários, etc)

def format_zero(num):
    num = str(num)
    if len(num) == 1:
        num = "0" + num
    return num

# sintaxe: class [nome]:
class Data:
    # __init__ --> função de "inicialização" onde os elementos inerentes serão atribuído
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    # agora, podemos criar o que for necessário para este objeto
    # sempre passar como parâmetro desses atributos o 'self', que é o próprio objeto
    def printData(self):
        print(f"Data: {format_zero(self.dia)}/{format_zero(self.mes)}/{self.ano}.")

try:
    dia = int(input("Digite o dia: "))
    if dia > 31 or dia < 1:
        raise TypeError("O dia deve ser um inteiro de 1 a 31.")
    mes = int(input("Digite o mês: "))
    if mes < 1 or mes > 12:
        raise TypeError("O mês deve ser um inteiro de 1 a 12.")
    ano = int(input("Digite o ano: "))
    if ano < 0:
        raise TypeError("O ano deve ser um inteiro maior que zero.")
except ValueError as e:
    print(f"Erro: O dia, o mês e o ano devem ser números inteiros.")
except TypeError as e:
    print(f"Erro: {e}")
else:
    obj = Data(dia, mes, ano)
    obj.printData()

class Dog:
    # atributo de classe --> valor que pode ser acessado por todos os objetos dessa classe
    especie = "Dalmata"
    def __init__(self, name):
        # atributo de instância --> valores próprios de cada objeto dessa classe
        self.name = name

print(Dog.especie)

dog1 = Dog("Bethoveen")
print(dog1.name)
print(dog1.especie)

dog2 = Dog("Luke")
print(dog2.name)
print(dog2.especie)

# funções especiais --> é a forma com que o python vê todas as funções (aprofundamento de visão)
# a exemplo: len() -> __len__(), 3 + 4 -> 3__add__(4), ...
class book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
    # caso quisermos utilizar funções já definidas em objetos criados, devemos utilizar a notação especial (__)
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"O livro '{self.name}' tem {self.pages} páginas."
    
    # devemos conhecer como funcionam essas funções são lidas para poder utilizá-las nas classes
    # igualdade (==) -> __eq__(p1, p2)
    # precisamos definir esta pois sem ela o python retorna a comparação entre as posições de memória
    def __eq__(self, other):
        return self.name == other.name and self.pages == other.pages

book1 = book("Metamorfose", 120)
book2 = book("Dom Quixote", 1597)
print(len(book1))
print(str(book2))
print(book1 == book2)

# getattr() --> função que retorna um atributo de um objeto
# caso o objeto não possua o atributo, retorna o valor padrão e se não tiver valor padrão retorna AttributeError

# setattr() --> adiciona um novo atributo ou atualiza o valor do mesmo caso já exista no objeto
setattr(dog1, "name", "Lilica")
setattr(dog1, "age", "15")
print(dog1.name, dog1.age)

# hasattr() --> retorna True se o objeto tiver o atributo e False caso contrário
if hasattr(dog2, "age"):
    print(dog2.age)
else:
    print("dog2 não tem 'age'.")

# delattr() --> deleta um atributo do objeto
delattr(dog1, "age")

# dir() --> lista com os todos parâmetros de um objeto, incluindo os padrões como __init__()
print(dir(dog1))
for attr in dir(dog1):
    if not attr.startswith("__"):
        print(attr, end = " ")
print()

for attr in dir(book1):
    if not attr.startswith("__"):
        print(attr, end = " ")
print()

# um outro exemplo que utiliza várias funções embutidas
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

    # função que retorna o valor de um iterável num index
    def __getitem__(self, index):
        return self.items[index]

    # função que retorna o operador 'in'
    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

cart = Cart()
cart.add('Laptop')
print(len(cart))
print('Laptop' in cart)
