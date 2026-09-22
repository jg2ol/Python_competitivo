from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
    def __init__(self, valor:int|float):
        self._valor = valor

    @property
    def valor(self): return self._valor

    @valor.setter
    def valor(self, novo_valor):
        if novo_valor > 0: self._valor = novo_valor
        else: raise ValueError("O pagamento só pode ser efetuado para valores positivos.")

    @property
    def fvalor(self):
        # return f"R$ {self.valor:,.2f}"
        # Formatando a impressão de valores monetários
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        return locale.currency(self._valor, grouping=True)

    @abstractmethod
    def pagar(self, valor):
        pass



class Boleto(Pagamento):
    def __init__(self, valor=0):
        super().__init__(valor)

    def pagar(self, valor:int|float):
        try:
            self.valor = valor
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Boleto!")
        except Exception as e:
            print(f"Falha no pagamento de {self.fvalor} via Boleto!")


class Pix(Pagamento):
    def __init__(self, valor=0):
        super().__init__(valor)

    def pagar(self, valor:int|float):
        try:
            self.valor = valor
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Pix!")
        except Exception as e:
            print(f"Falha no pagamento de {self.fvalor} via Pix!")


class CartaoCredito(Pagamento):
    def __init__(self, valor=0):
        super().__init__(valor)

    def pagar(self, valor:int|float):
        try:
            self.valor = valor
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito!")
        except Exception as e:
            print(f"Falha no pagamento de {self.fvalor} via Cartão de Crédito!")


def finalizar_compra(pag:Pagamento, valor):
    try:
        pag.pagar(valor)
    except Exception as e:
        print(f"Erro: {e}")
