from rich import print
from rich.table import Table


# Imprimindo tabelas
tabela = Table(title="Tabela de preços")
tabela.add_column("Nome", justify="right", style="red")
tabela.add_column("Preço", justify="center", style="blue")
tabela.add_row("Lápis", "R$1,50")
tabela.add_row("Borracha", "R$2,00")
print(tabela)
