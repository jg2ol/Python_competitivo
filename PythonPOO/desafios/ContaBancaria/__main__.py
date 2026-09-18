from classes import ContaBancaria

def main():
    c1 = ContaBancaria(123, "João", 1000)
    print("Tentando sacar 500")
    c1.sacar(500)
    c1.depositar(300)
    print("Tentando mudar o nome")
    c1.nome = "Maria"
    print(c1)


if __name__ == "__main__":
    main()
