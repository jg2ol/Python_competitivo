# Convenções p/ docstring:
# https://peps.python.org/pep-0257/

class Pessoa:
    # Documentação da classe -> docstring
    """Esta classe cria uma pessoa com nome e idade
    Declaração: var = Pessoa(nome, idade)"""
    # Método Construtor
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    # Método de Instância
    def aniversario(self):
        self.idade += 1
    # Dunder Method
    def __str__(self):
        return f"{self.nome} é uma Pessoa e possui {self.idade} anos de idade."
    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade = {self.idade}"


p1 = Pessoa("João", 17)
p1.aniversario()
print(p1)
print(p1.__doc__) # Dunder Attribrute
print(p1.__dict__) # dicionário com os atributos da instância
print(p1.__getstate__()) # mesmo que dict, porém, pode ser personalizado
print(p1.__class__)
