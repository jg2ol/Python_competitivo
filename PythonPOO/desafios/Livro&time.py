from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.atual = 1
        print(f":open_book: [blue]Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.paginas} páginas[/] no total. Você agora está na [yellow]página 1[/]")

    def avancar_paginas(self, qtd=1):
        quant = qtd
        if self.atual < self.paginas:
            for x in range(1, qtd+1):
                self.atual += 1
                print(f"Pág{self.atual} :arrow_forward: ", end="")
                time.sleep(0.35)
                if self.atual+x > self.paginas:
                    quant = x
                    break
        else: quant = 0
        print(f"[blue]Você avançou {quant} página(s) e agora está na [yellow]página {self.atual}[/]")
        if self.atual == self.paginas:
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")


l1 = Livro("O Último Teorema de Fermmat", 10)
l1.avancar_paginas(5)
l1.avancar_paginas(3)
l1.avancar_paginas(5)
l1.avancar_paginas(2)
