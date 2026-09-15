from abc import ABC, abstractmethod

def FM(x): return f"R${x:,.2f}"

class Transporte(ABC):
    def __init__(self, distancia, frete):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)

    def calc_frete(self):
        print(f"O frete será de {FM(Moto.fator*self.distancia)}")

class Caminhao(Transporte):
    fator = 1.2
    distancia_min = 50
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)

    def calc_frete(self):
        if self.distancia >= Caminhao.distancia_min:
            print(f"O frete será de {FM(Caminhao.fator*self.distancia)}")
        else:
            print("Distância muito pequena para entregar de caminhão.")


class Drone(Transporte):
    fator = 9.5
    distancia_max = 10
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)

    def calc_frete(self):
        if self.distancia <= Drone.distancia_max:
            print(f"O frete será de {FM(Drone.fator*self.distancia)}")
        else:
            print("Muito longe para entregar de drone.")
