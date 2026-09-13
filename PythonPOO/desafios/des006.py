from rich import print

class Caneta:
    def __init__(self, cor):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tamp = True

    def destampar(self): self.tamp = False
    def tampar(self): self.tamp = True

    def quebrar_linha(self, qtd=1): print("\n"*qtd, end="")
    def escrever(self, text):
        if self.tamp:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!", end="")
        else:
            print(f"{self.cor}{text}[/]", end="")

c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c1.escrever("Olá ")
c2.escrever("Mundo!")
c3.escrever("Bom dia!")
c3.destampar()
c3.escrever("Bom dia!")
c1.quebrar_linha(2)
c1.escrever("Eu sou a Caneta azul.")
c1.tampar()
c2.tampar()
c3.tampar()
c3.escrever("Eu sou a caneta verde.")
