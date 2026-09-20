from classes import *

def main():
    a1 = Analisador()
    a1.analisar(5)
    a1.analisar("5")
    a1.analisar(["5", 4])
    a1.analisar({"nome": "Maria", "idade": 15})
    a1.analisar(-1.2)


if __name__ == "__main__":
    main()
