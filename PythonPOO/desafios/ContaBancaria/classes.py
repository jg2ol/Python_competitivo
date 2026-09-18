from hashlib import sha256

def FM(valor): return f"R${valor:,.2f}"

class ContaBancaria():
    def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:None = "1234"):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        print(f"Conta {self._id} criada com sucesso. Saldo atual: {FM(self.__saldo)}")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome, chave=input()):
        if sha256(chave.encode("utf-8")).hexdigest() != self.__hash:
            raise PermissionError("Senha inválida!")
        else:
            self._titular = str(nome)

    def validar_senha(self, chave):
        pass

    def pede_senha(self):
        while True:
            senha = input("Senha: ")
            if len(senha) >= 6:
                break
        return senha

    def sacar(self, valor, chave):
        pass

    def depositar(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise ValueError("Valor inválido.")
        else:
            self._saldo += valor
