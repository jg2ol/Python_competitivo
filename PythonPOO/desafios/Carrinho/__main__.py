from classes import *

def main():
    p1 = Produto("Mouse", 300)
    p2 = Produto("Teclado", 450)
    p3 = Produto("Placa de Vídeo", 26000)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p3
    print(c1)
    c2 = c2 + c1 + p2
    print(c2)

if __name__ == "__main__":
    main()
