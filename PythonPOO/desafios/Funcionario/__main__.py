from classes import *

def main():
    f1 = Horista("Paulo", 12, 200)
    f2 = Mensalista("Maria", 4500)

    f1.calcular_salario()
    f2.calcular_salario()
    f1.analisar_salario()
    f2.analisar_salario()


if __name__ == "__main__":
    main()
