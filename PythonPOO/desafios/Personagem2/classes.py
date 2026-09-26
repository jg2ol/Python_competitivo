from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from random import randint

"""
mais p/ frente, fazer:
while True p/ interações (op -> atacar, curar, criar_personagem*)
pergaminhos com golpes específicos de cada classe (um pergaminho pode ser uma classe)
ilustração com tabelas de vida de cada personagem com cores
adicionar personagens e reiterar a ilustração das barras de vida
"""

def onColor(color, qtd, max_qtd, back_color="#ffffff"):
    return f"[black on {color}]{qtd}{" "*(int(40*qtd/max_qtd)-len(str(qtd)))}[/][black on {back_color}]{" "*(40-int(40*qtd/max_qtd)-len(str(max_qtd)))}{max_qtd}[/]"

ataques_basicos = ["Soco", "Chute"]

class Personagem(ABC):
    def __init__(self, nome:str="player"):
        self._nome = nome
        self.__maxVida = 100
        self._vida = 100
        self._forca = 25
        self.__level = 0
        self.__maxXp = 20
        self._xp = 0
        self.__vivo = True
        self._ataques = ataques_basicos

    @property # a := ativo (realiza uma ação)
    def anome(self): return f"[cyan]{self._nome}[/]([green]{self._vida}[/])"
    @property # p := passivo (recebe uma ação)
    def pnome(self): return f"[red]{self._nome}[/]([purple]{self._vida}[/])"
    @property
    def rataque(self): return f"{self._ataques[randint(0, min(len(self._ataques), self.__level + len(ataques_basicos)) - 1)]}"

    @property
    def maxVida(self): return self.__maxVida
    @property
    def level(self): return self.__level
    @property
    def maxXp(self): return self.__maxXp
    @property
    def vivo(self): return self.__vivo

    def __str__(self):
        conteudo = f"HEALTH: {onColor("green", self._vida, self.__maxVida)}\n"
        conteudo += f"    XP: {onColor("yellow", self._xp, self.__maxXp)}\n"
        conteudo += f"STRENGTH: {self._forca}"
        print(Panel(conteudo, title=f"{self.__class__.__name__}: {self._nome}", width=40+20))
        return ""

    def subir_level(self):
        self.__level += 1
        self.__maxVida += 50
        self._vida = self.__maxVida
        self._forca += 25
        self._xp = 0
        self.__maxXp += 10
        print(f"{self.anome} [yellow]subiu de nível[/]!")

    def receber_xp(self, xp):
        if self._xp + xp >= self.__maxXp:
            xp -= self.__maxXp - self._xp
            self.subir_level()
            self.receber_xp(xp)
        else: self._xp += xp

    def receber_dano(self, dano:int):
        print(f"{self.pnome} recebeu [red]dano de {dano}[/]!")
        if dano < self._vida: self._vida -= dano
        else:
            self._vida = 0
            print(f"Isso é demais para [red]{self._nome}[/]...")
            self.morte()

    def atacar(self, alvo:Personagem):
        if self.__vivo and alvo.__vivo:
            print(f"{self.anome} atacou {alvo.pnome} com [blue]{self.rataque}[/] de [cyan]força {self._forca}[/]")
            alvo.receber_dano(5*randint(1, self._forca//5))
            self.receber_xp(5)

    @abstractmethod
    def curar(self):
        pass

    def morte(self):
        self.__vivo = False
        print(f"Menos um Personagem na história, [blue]{self._nome}[/] foi um grande [red]{self.__class__.__name__}[/]...")



class Guerreiro(Personagem):
    def __init__(self, nome:str):
        super().__init__(nome)
        self._ataques = ataques_basicos + ["Espadada", "Pulo Giratório", "Tombo Atordoante", "Ataque de Escudo"]

    def curar(self):
        if self.vivo:
            cura = min(self.maxVida - self._vida, 5*randint(1, 10))
            self._vida += cura
            print(f"{self.anome} enrolou uma atadura nos ferimentos e recuperou [green]{cura} pontos[/] de vida.")


class Mago(Personagem):
    def __init__(self, nome:str):
        super().__init__(nome)
        self._ataques = ataques_basicos + ["Bola de Fogo", "Vento Congelante", "Vinhas Sorrateiras", "Raio Cósmico"]

    def curar(self):
        if self.vivo:
            cura = min(self.maxVida - self._vida, 5*randint(1, 10))
            self._vida += cura
            print(f"{self.anome} fez uma magia de cura e recuperou [green]{cura} pontos[/] de vida.")



# def criar_guerreiro(nome, vida, level):
#     pass

# def criar_mago(nome, vida, level):
#     pass

def play():
    while True:
        op = input()
        if op == "x": break
