# Encapsulamento - Protejendo métodos e atributos
# + -> public -> atrib1
# # -> protected -> _atrib2
# - -> private -> __atrib3 (Name Manglin)
# em Python: Consenting Adults

def FM(valor): return f"R${valor:,.2f}"

class ContaBancaria:
    """Cria uma conta bancária que permite fazer saques e depósitos."""
    def __init__(self, id, nome, saldo=0):
        self.id = id          # público
        self._titular = nome  # protegido
        self.__saldo = saldo  # privado
        print(f"Conta criada com sucesso! Saldo atual {FM(saldo)}!")

    def __str__(self):
        return f"A conta {self.id} de {self._titular} tem {FM(self.__saldo)} de saldo."

    def deposito(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de {FM(valor)} realizado com sucesso na conta {self.id}!")

    def saque(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque negado de {FM(valor)} na conat {self.id}, saldo insuficiente!")
        else:
            self.__saldo -= valor
            print(f"Saque autorizado no valor de {FM(valor)} na conta {self.id}!")
