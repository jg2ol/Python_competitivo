# Caminhando com um personagem num jogo 2D

from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    
    def make_move(self):
        move = random.choice(self.moves)
        self.position = (self.position[0]+move[0], self.position[1]+move[1])
        self.path.append(self.position)
    
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def make_move(self):
        super().make_move()
        return self.position
    
    def level_up(self):
        diagonal_moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.moves.extend(diagonal_moves)
    
    def __str__(self):
        return f"Posição: {self.position}\nMovimentos possíveis: {self.moves}\nCaminho: {self.path}\n"

pawn = Pawn()
pawn.make_move()
pawn.make_move()
print(pawn)
pawn.level_up()
pawn.make_move()
pawn.make_move()
pawn.make_move()
print(pawn)
