# Polimorfismo de sobrecarga (overload) [de método]
from functools import singledispatchmethod

class Analisador:
    # caso não haja método para o tipo de 'valor'
    @singledispatchmethod # valida o primeiro valor passado para o método
    def analisar(self, valor):
        print("Não foi possível analisar o valor.")

    @analisar.register
    def _(self, valor:int):
        print("Inteiro")

    # esse não dá certo porque falta o decorador
    def _(self, valor:str):
        print("String")

    # caso 'valor' seja do tipo tuple, list ou dict
    @analisar.register
    def _(self, valor:tuple|list|dict):
        print("Variável composta.")

    @analisar.register
    def _(self, valor:float):
        print("Valor real.")
