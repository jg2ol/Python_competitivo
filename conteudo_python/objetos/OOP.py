# Programação Orientada a Objetos (OOP) --> metodos de programação que trabalham com objetos

class Wallet:
   def __init__(self, balance):
       self.__balance = balance # dessa forma não se há acesso direto à 'balance' (é usado somente internamente)
       # se fosse prefixado com um underscore, acessar o valor fora da classe deve gerar bugs

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount

   def withdraw(self, amount):
       if 0 < amount <= self._balance:
           self.__balance -= amount

# obs: quando prefixamos com dunder, o python muda de '__[atributo]' para '_[nome_classe]__[atributo]'
# para evitar confusão de funções/atributos em casos de polimorfismo
wallet_obj = Wallet(14)
print(wallet_obj._Wallet__balance)

# getters --> propriedades para pegar os dados de objetos
# setters --> propriedades para modificar os atributos de um objeto mesmo quando seus dados estão "ocultos"
# deleter --> retira um atributo de um objeto

# obs1: chamar self.radius dentro dos setters gera um recursão infinita e retorna RecursionError
# por isso, dentro dos setters, sempre se deve chamar self._radius quando quisermos relacionar ao raio
# obs2: @property e @[property_name].getter é a mesma coisa
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property # serve apenas para indicar que a função abaixo é uma propriedade que pode er acessada como um atributo
    def radius(self):
        return self._radius
    
    # setter que modifica o valor do atributo de instância '_radius'
    @radius.setter # apenas para deixar claro qual o objetivo dessa função
    def radius(self, value):
        if value <= 0:
            raise ValueError("O raio deve ser positivo.")
        self._radius = value
    
    # deleter que apaga o dado '_radius'
    @radius.deleter
    def radius(self):
        print("Deletando o raio...")
        del self._radius

    @property
    def area(self):
        return 3.14 * (self._radius**2)

circle_obj = Circle(3)
print(circle_obj.radius) # chama o getter radius(self) como um atributo
print(circle_obj.area)

circle_obj.radius = 8 # chama o setter radius(self, value) como um atributo
print(circle_obj.radius)

del circle_obj.radius # chama o deleter radius(self)
print("Raio deletado!")
try:
    print(circle_obj.radius)
except AttributeError as e:
    print(f"Erro: {e}")

# Polimorfismo --> quando geramos uma classe (pai) como 'parâmetro' de outra (filha)
# "classe pai"
class Animal:
    def sound(self):
        return "Algum som de animal."

# "classe filha"
class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Meau"
    
    # super() --> referencia o valor para funções/atributos da classe pai
    def superior_sound(self):
        return super().sound() # este 'sound()' vem de 'Animal'

animal_obj = Animal()
cat_obj = Cat("Mary")

print(animal_obj.sound())
print(cat_obj.sound())
print(cat_obj.superior_sound())

# Abstração --> Abstract Base Class (ABC), apenas uma organização do código 
# utilizando a abstração, as classes filhas devem ter todos os métodos e atributos da classe pai
from abc import ABC, abstractmethod

class abs_Animal(ABC):
    @abstractmethod # decorador de abc
    def make_sound(self):
        # nenhum retorno é necessário
        # estamos apenas dizendo que todas as classes filhas devem ter o método 'make_sound()'
        pass

class dog(abs_Animal):
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return f"Eu sou {self.name}, woof woof!"

class cat(abs_Animal):
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return f"Eu sou {self.name}, meau!"

"""
class bird(abs_Animal):
    pass

bird1 = bird()
"""
# TypeError: Can't instantiate abstract class Bird 
# without an implementation for abstract method 'make_sound'
