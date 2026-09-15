from abc import ABC, abstractmethod

def FM(x): return f"R${x:.2f}"

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = Moto.fator*self.distancia
        return FM(self.frete)

class Caminhao(Transporte):
    fator = 1.2
    distancia_min = 50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < Caminhao.distancia_min:
            self.frete = 0
            return f"Raio mínimo de {Caminhao.distancia_min}km"
        else:
            self.frete = Caminhao.fator*self.distancia
            return FM(self.frete)


class Drone(Transporte):
    fator = 9.5
    distancia_max = 10
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > Drone.distancia_max:
            self.frete = 0
            return f"Raio máximo de {Drone.distancia_max}km"
        else:
            self.frete = Drone.fator*self.distancia
            return FM(self.frete)
