from abc import ABC, abstractmethod
from rich import print
from random import randint
# mais p/ frente, fazer:
# while True p/ interações
# pergaminhos com golpes específicos de cada classe (um pergaminho pode ser uma classe)
# ilustração com tabelas de vida de cada personagem com cores
# verificar morte de personagens
# adicionar personagens e reiterar a ilustração das barras de vida

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {dano}[/]!")

    def atacar(self, alvo, forca):
        print(f"[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red]{alvo.nome}[/]([cyan]{alvo.vida}[/]) com [blue]{self.golpes[randint(0, len(self.golpes)-1)]}[/] de força [cyan]{forca}[/]")
        alvo.receber_dano(randint(1, forca))

    @abstractmethod
    def curar(self):
        pass



class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Chute Giratório", "Espadada"]

    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida.")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio Cósmico", "Vinhas Sorrateiras"]

    def curar(self):
        cura = randint(1, 200)
        self.vida += cura
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida.")
