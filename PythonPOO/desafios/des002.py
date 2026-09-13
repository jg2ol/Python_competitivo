from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return Panel(f"{self.nome.center(30, ' ')}\n{"-"*30}\n{f"R${self.preco:,.2f}".center(30, ' ')}", title="Produto", width=34)

p1 = Produto("Celular", 1500)
print(p1.etiqueta())

p2 = Produto("Notebook", 4500)
print(p2.etiqueta())
