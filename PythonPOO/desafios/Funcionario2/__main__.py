from classes import *

def main():
    g = Gerente("Ana", 3500)
    dev = Desenvolvedor("João", 1800)
    dgn = Designer("Pedro", 1500)

    dev.salario = 2000
    dgn.salario = 1800

    print(g)
    print(dev)
    print(dgn)


if __name__ == "__main__":
    main()
