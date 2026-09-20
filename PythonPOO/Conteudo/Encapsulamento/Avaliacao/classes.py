class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Atributos Validáveis - Como o Python altera atributos privados
    @property
    def nota(self): # getter
        return self._nota

    @nota.setter
    def nota(self, valor): # setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida!")

    @nota.deleter
    def nota(self):
        pass

    # Como é tradicionalmente feito
    # # métodos acessores
    # def get_nota(self): # método getter
    #     return self._nota

    # def set_nota(self, valor): # método setter
    #     if 0 <= valor <= 10:
    #         self._nota = valor
    #     else:
    #         print("Nota inválida!")
