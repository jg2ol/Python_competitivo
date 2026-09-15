from classes import *
from rich import print
from rich.table import Table

def main():
    dist = 50
    entregas = [Moto(dist), Caminhao(dist), Drone(dist)]
    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")
    for e in entregas:
        tabela.add_row(f"{dist}km", f"{type(e).__name__}", f"{e.calc_frete()}")
    print(tabela)


if __name__ == "__main__":
    main()
