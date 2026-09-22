from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, msg:str = "", tipo:str = "aviso", icone:str = ":speech_balloon:"):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        print(Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", width=44, style="#ffffff on #000000"))



class Alerta(Mensagem):
    def __init__(self, msg):
        super().__init__(msg, "alerta", ":warning:")

    def mostrar(self):
        print(Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", width=44, style="#000000 on #fffc1b"))


class Erro(Mensagem):
    def __init__(self, msg):
        super().__init__(msg, "erro", ":prohibited:")

    def mostrar(self):
        print(Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", width=44, style="#ffff00 on #880000"))
