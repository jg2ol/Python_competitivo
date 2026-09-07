from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return Panel(f"{self.nome:^30}\n{"-"*30}\n{f"R${self.preco:,.2f}":^30}", title="Produto", width=50)

p = Produto("Celular", 1500)
print(p.etiqueta())
