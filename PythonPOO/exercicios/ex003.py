def FM(valor):
    return f"R${valor:,.2f}"

class ContaBancaria:
    """Cria uma conta bancária que permite fazer saques e depósitos."""
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta criada com sucesso! Saldo atual {FM(saldo)}!")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso na conta {self.id}!")

    def saque(self, valor):
        if valor > self.saldo:
            print(f"Saque negado de {valor} na conat {self.id}, saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque autorizado no valor de {valor} na conta {self.id}!")


conta = ContaBancaria(314, "João", 2500)
conta.saque(500)
conta.deposito(1000)
print(conta)
