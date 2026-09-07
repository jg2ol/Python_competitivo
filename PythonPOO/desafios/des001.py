from rich import print

class Funcionario:
    empresa = "Curso em Vídeo"
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":+1: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} na empresa {self.empresa}"


c1 = Funcionario("Maria", "Admnistração", "Diretora")
print(c1.apresentacao())

c2 = Funcionario("Pedro", "TI", "Programação")
print(c2.apresentacao())
