from classes import *

def main():
    c = Credencial()
    c.senha = "joao1234"
    print(c.senha)
    print(c.validar("1234"))
    print(c.validar("joao1234"))


if __name__ == "__main__":
    main()
