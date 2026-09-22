from classes import *

def main():
    finalizar_compra(Boleto(), 2500)
    finalizar_compra(Pix(), 375)
    finalizar_compra(CartaoCredito(), 4000)


if __name__ == "__main__":
    main()
