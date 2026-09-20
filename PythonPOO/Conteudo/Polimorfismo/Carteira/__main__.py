from classes import *

def main():
    c1 = Carteira()
    c2 = Carteira(300)
    print(c1)
    print(c2)

    c1 += 200
    c2 -= 50
    print(c1 == c2)

    if c1 > c2: print("A primeira carteira tem mais dinheiro.")
    elif c1 < c2: print("A segunda carteira tem mais dinheiro.")
    else: print("As duas carteira têm a mesma quantia.")

    print(c1)
    print(c2)

    b1 = ObjetoQualquer()
    tentar_abrir(c1)
    tentar_abrir(b1)


if __name__ == "__main__":
    main()
