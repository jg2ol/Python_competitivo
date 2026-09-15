from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    salario_min = 1621
    inss = 7.5 # desconto do INSS em porcentagem
    def __init__(self, nome):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        print(Panel(f"O salário de [blue]{self.nome}[/] ([cyan]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] e correponde a [yellow]{self.salario/Funcionario.salario_min:.1f} salários mínimos[/].", title="Análise de Salários", width=50))



class Horista(Funcionario):
    def __init__(self, nome, valor_hora=7.37, horas_trab=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.salario_bruto = self.valor_hora*self.horas_trab

    def calcular_salario(self):
        self.salario = self.salario_bruto*(100 - Funcionario.inss)/100


class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto=Funcionario.salario_min):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calcular_salario(self):
        self.salario = self.salario_bruto*(100 - Funcionario.inss)/100
