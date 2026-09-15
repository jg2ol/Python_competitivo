from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def ferver_agua(self):
        return "Fervendo água a 100 graus Celcius."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

    def preparar(self):
        print("--- Iniciando o Preparo ---")
        v = [self.ferver_agua(), self.misturar(), self.servir()]
        for x, conteudo in enumerate(v):
            print(f"{x+1}. {conteudo}")
        print("--- Bebida Pronta ---")



class Cafe(BebidaQuente):
    def misturar(self):
        return "Passando água pressurizada pelo pó de café moído."

    def servir(self):
        return "Servindo na xícara pequena."


class Cha(BebidaQuente):
    def misturar(self):
        return "Mergulhando o sachê de ervas na água."

    def servir(self):
        return "Servindo na caneca de porcelana com limão."


class Leite(BebidaQuente):
    def misturar(self):
        return "Passando o vapor pressurizado no bico do leite."

    def servir(self):
        return "Servindo na caneca grande já com café."
