def FM(valor):
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return locale.currency(valor, grouping=True)

class Produto:
    def __init__(self, nome:str, preco:int|float):
        self.nome = nome
        self.preco = preco

    def __str__(self): return f"{self.nome} ({FM(self.preco)})"


class Carrinho:
    def __init__(self, produtos:list = None):
        self.produtos = produtos if produtos else []

    @property
    def total(self): return sum(p.preco for p in self.produtos)

    def __str__(self):
        width = max(len(str(p)) for p in self.produtos)
        return "\n".join(str(p) for p in self.produtos) + "\n" + "-"*width + f"\nTotal: {FM(self.total)}\n"

    def __add__(self, other):
        if isinstance(other, Produto): return Carrinho(self.produtos + [other])
        elif isinstance(other, Carrinho): return Carrinho(self.produtos + other.produtos)
        else: raise TypeError("Você tentou adicionar algo inválido ao carrinho.")
