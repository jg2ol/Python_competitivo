# Polimorfismo de sobrecarga de operador
# queremos fazer c1 += 100 => c1.__saldo += 100

class Carteira:
    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R${self.__saldo:,.2f} na carteira."

    def abrir(self):
        print(f"Esta carteira possui R${self.__saldo:,.2f} de saldo.")

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self):
        raise PermissionError("Você não tem autorização para alterar o saldo desse jeito.")

    # Equal to
    def __eq__(self, c):
        return self.__saldo == c.__saldo

    # Not Equal to
    def __ne__(self, other):
        return self.__saldo != other.__saldo

    # Less Than
    def __lt__(self, other): return self.__saldo < other.__saldo
    # Less Than or Equal to
    def __le__(self, other): return self.__saldo <= other.__saldo
    # Greater Than
    def __gt__(self, other): return self.__saldo > other.__saldo
    # Greater Than or Equal to
    def __ge__(self, other): return self.__saldo >= other.__saldo

    # nesses dois, sempre retornar 'self'
    # In-place Addition
    def __iadd__(self, valor:int|float):
        self.__saldo += valor
        return self
    # In-place Subtract
    def __isub__(self, valor:int|float):
        self.__saldo -= valor
        return self

# Duck Typing - Não funciona p/ métodos com return padrão (dunder methods)
class ObjetoQualquer: # não possui o método 'abrir'
    pass

def tentar_abrir(objeto):
    try: objeto.abrir()
    except: print(f"Ocorreu um problema ao tentar abrir um objeto do tipo {objeto.__class__.__name__}.")
