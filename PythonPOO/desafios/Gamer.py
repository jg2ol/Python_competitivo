from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.fav = []

    def add_favoritos(self, game):
        self.fav.append(game)
        self.fav = sorted(self.fav)

    def ficha(self):
        tabela = ""
        for jogo in self.fav:
            tabela += f"\n:video_game: [blue]{jogo}[/]"
        print(Panel(f"Nome real: [black on blue]{self.nome}[/]\nJogo Favoritos:{tabela}", title=f"Jogador <{self.nick}>"))


j1 = Gamer("João Gabriel", "joso_leirbag")
j1.add_favoritos("Free Fire")
j1.add_favoritos("Among Us")
j1.add_favoritos("Rocket League")
j1.ficha()
