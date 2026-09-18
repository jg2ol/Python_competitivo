class Diario:
    def __init__(self, senha="1234"):
        self.__senha = senha
        self.__segredos = []

    def escrever(self, text):
        if isinstance(text) and len(text) > 0:
            self.__segredos.append(text.strip())

    def ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler este diário!")
        else:
            for i, x in enumerate(self.__segredos):
                print(f"{i+1}. {x}")

    @property
    def senha(self):
        raise PermissionError("Ninguém pode acessar a senha")
