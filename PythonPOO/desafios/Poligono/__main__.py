from rich import print
from classes import Quadrado, Circulo

def main():
    q1 = Quadrado(5)
    print(f"Perímetro = [blue]{q1.perimetro():.1f}[/]")
    print(f"Área = [blue]{q1.area():.1f}[/]")

    c1 = Circulo(3)
    print(f"Perímetro = [blue]{c1.perimetro():.1f}[/]")
    print(f"Área = [blue]{c1.area():.1f}[/]")


if __name__ == "__main__":
    main()
