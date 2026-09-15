from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado=1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return 4*self.lado

    def area(self):
        return self.lado*self.lado


class Circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(float("INF"))
        self.raio = raio

    def perimetro(self):
        return 2*3.14*self.raio

    def area(self):
        return 3.14*self.raio*self.raio
