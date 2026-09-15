from classes import *

def main():
    p1 = Guerreiro("Kratos", 3000)
    p2 = Mago("Merlin", 2000)

    p1.atacar(p2, 1000)
    p2.curar()
    p2.atacar(p1, 750)
    p1.curar()


if __name__ == "__main__":
    main()
