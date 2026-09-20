from classes import *

def main():
    c1 = ContaBancaria(101, "Maria", 5000)
    c1.deposito(500)
    c1.saque(-200)
    c1.id = 110 # atributo público pode ser alterado no código principal
    c1._titular = "Jorge" # é permitido mas não se deve alterar atributo protegido
    c1._ContaBancaria__saldo = 0 # não sobrou nada pro beta...
    print(c1)
    print(c1.__dict__)


if __name__ == "__main__":
    main()
