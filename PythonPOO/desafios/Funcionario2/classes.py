from abc import ABC, abstractmethod

def FM(valor): return f"R${valor:,.2f}"

class Funcionario(ABC):
    def __init__(self, nome:str, salario:int|float = 1621):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self): return self.__salario

    @salario.setter
    def salario(self, valor:int|float = None):
        if valor is None:
            raise ValueError("Impossível reajustar o salário desse jeito.")
        if valor < self.__salario:
            raise ValueError("Você não pode reduzir o salário de um funcionário.")
        else:
            self.__salario = valor

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self):
        return f"{self.nome} ganha {FM(self.salario)} e por ser {self.__class__.__name__} o bônus será de {FM(self.calcular_bonus())}"



class Gerente(Funcionario):
    bonus = 15/100
    def __init__(self, nome:str, salario:int|float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario*Gerente.bonus


class Designer(Funcionario):
    bonus = 8/100
    def __init__(self, nome:str, salario:int|float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario*Designer.bonus


class Desenvolvedor(Funcionario):
    bonus = 10/100
    def __init__(self, nome:str, salario:int|float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario*Desenvolvedor.bonus
