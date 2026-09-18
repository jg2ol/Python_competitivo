from hashlib import sha256

def FM(valor): return f"R${valor:,.2f}"

class ContaBancaria():
    def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        print(f"Conta {self._id} criada com sucesso. Saldo atual: {FM(self.__saldo)}")

    def __str__(self):
        return f"A conta {self._id} de {self._titular} tem {FM(self.__saldo)} de saldo."

    def pede_senha(self) -> str:
        from pwinput import pwinput
        senha = ""
        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
        return senha

    def validar_senha(self, chave) -> bool:
        return sha256(chave.encode("utf-8")).hexdigest() == self.__hash

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome:str = None):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            if len(nome) >= 5:
                print(f"Nome alterado de {self._titular} para {nome} com sucesso.")
                self._titular = nome
            else:
                print("O nome do titular deve ter pelo menos 5 caracteres.")
        else:
            print("Senha incorreta, não posso alterar o nome.")

    def depositar(self, valor:float):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de {FM(valor)} AUTORIZADO na conta {self._id}!")

    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)
        if chave is None: chave = self.pede_senha()
        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Saque de {FM(valor)} NEGADO na conta {self._id}: Saldo Insuficiente!")
            else:
                self.__saldo -= valor
                print(f"Saque de {FM(valor)} AUTORIZADO na conta {self._id}!")
        else:
            print("Senha incorreta, saque NÃO autorizado.")
