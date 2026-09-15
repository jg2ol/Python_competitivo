from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max:int = 3
    def __init__(self, canal=1, volume=1):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligada:bool = False

    def on(self): return self.ligada
    def liga_desliga(self):
        self.ligada = not self.ligada
    def tela(self):
        conteudo = ''
        if not self.ligada:
            conteudo = f":prohibited: [red]A TV está desligada[/]"
        else:
            conteudo = f"CANAL  = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max+1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "
            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max+1):
                if volume <= self.volume_atual:
                    conteudo += f"[on cyan]  [/]"
                else:
                    conteudo += f"[on white]  [/]"
        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)

    def avancar_canal(self):
        if self.ligada:
            self.canal_atual = self.canal_atual%ControleRemoto.canal_max + 1
    def voltar_canal(self):
        if self.ligada:
            self.canal_atual -= 1
            if self.canal_atual == 0:
                self.canal_atual = ControleRemoto.canal_max

    def aumentar_volume(self):
        if self.ligada:
            if self.volume_atual < ControleRemoto.volume_max:
                self.volume_atual += 1
    def diminuir_volume(self):
        if self.ligada:
            if self.volume_atual > ControleRemoto.volume_min:
                self.volume_atual -= 1


c1 = ControleRemoto()
while True:
    c1.tela()
    op = input("< CH >   - VOL +   0\n")
    if op == "@":
        c1.liga_desliga()
    elif op == ">":
        c1.avancar_canal()
    elif op == "<":
        c1.voltar_canal()
    elif op == "+":
        c1.aumentar_volume()
    elif op == "-":
        c1.diminuir_volume()
    elif op == "0":
        break
    print("\n"*10)
