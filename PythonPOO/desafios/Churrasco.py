from rich import print
from rich.panel import Panel


class Churrasco:
    # Consumo padrão: 400g por pessoa
    cp = 0.4
    # Preço: R$82.40/kg
    preco = 82.4
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    def analisar(self):
        print(Panel(f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\nCada participante comerá 0.4kg e cada kg custa R$82.40\nRecomendo [blue]comprar {self.quant*Churrasco.cp:.3f}kg[/] de carne\nO custo total será de [green]R${self.quant*Churrasco.cp*Churrasco.preco:.2f}[/]\nCada pessoa pagará [yellow]R${Churrasco.cp*Churrasco.preco:.2f}[/] para participar.", title=f"{self.titulo}"))


churras = Churrasco("Churras dos amigos", 15)
churras.analisar()
