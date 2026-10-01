from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from random import randint


def onColor(color, qtd, max_qtd, back_color="#ffffff"):
    """Retorna uma barra de atributo (atual/máximo) com cores recebidas."""
    return f"[black on {color}]{qtd}{" "*(int(40*qtd/max_qtd)-len(str(qtd)))}[/][black on {back_color}]{" "*(40-int(40*qtd/max_qtd)-len(str(max_qtd)))}{max_qtd}[/]"


class Personagem(ABC):
    ataques_basicos = ["Soco", "Chute"]
    def __init__(self, nome:str="player"):
        self._nome = nome
        self.__maxVida = 100
        self._vida = 100
        self._forca = 25
        self.__level = 0
        self.__maxXp = 20
        self._xp = 0
        self.__vivo = True
        self._ataques = Personagem.ataques_basicos

    @property
    def classe(self): return self.__class__.__name__
    @property
    def nome(self): return self._nome
    @property
    def title(self): return f"[magenta]{self.classe}[/]: [cyan]{self.nome}[/]"
    @property # a := ativo (realiza uma ação)
    def anome(self): return f"[cyan]{self._nome}[/]([green]{self._vida}[/])"
    @property # p := passivo (recebe uma ação)
    def pnome(self): return f"[red]{self._nome}[/]([purple]{self._vida}[/])"
    @property
    def rataque(self): return f"{self._ataques[randint(0, min(len(self._ataques), self.__level + len(Personagem.ataques_basicos)) - 1)]}"

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
        print(Panel(conteudo, title=self.title, width=40+20))
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
        '''No caso de ambos estarem vivos, faz um Personagem atacar o outro.'''
        if self.__vivo and alvo.__vivo:
            print(f"{self.anome} atacou {alvo.pnome} com [blue]{self.rataque}[/] de [cyan]força {self._forca}[/]")
            alvo.receber_dano(5*randint(1, self._forca//5))
            self.receber_xp(5)

    @abstractmethod
    def curar(self):
        '''Cura de 5 a 50 pontos de vida.'''
        pass

    def reviver(self):
        '''Revive um Personagem'''
        self.__init__(self._nome)
        print(f"{self.anome} [green]reviveu[/]!")

    def morte(self):
        self.__vivo = False
        print(f"Menos um Personagem na história, [blue]{self._nome}[/] foi um grande [magenta]{self.classe}[/]...")



class Guerreiro(Personagem):
    def __init__(self, nome:str):
        super().__init__(nome)
        self._ataques = Personagem.ataques_basicos + ["Espadada", "Pulo Giratório", "Tombo Atordoante", "Ataque de Escudo"]

    def curar(self):
        if self.vivo:
            if self._vida == self.maxVida: print(f"A vida de [green]{self._nome}[/] já está cheia!")
            else:
                cura = min(self.maxVida - self._vida, 5*randint(1, 10))
                self._vida += cura
                print(f"{self.anome} enrolou uma atadura nos ferimentos e recuperou [green]{cura} pontos[/] de vida.")


class Mago(Personagem):
    def __init__(self, nome:str):
        super().__init__(nome)
        self._ataques = Personagem.ataques_basicos + ["Bola de Fogo", "Vento Congelante", "Vinhas Sorrateiras", "Raio Cósmico"]

    def curar(self):
        if self.vivo:
            if self._vida == self.maxVida: print(f"A vida de [green]{self._nome}[/] já está cheia!")
            else:
                cura = min(self.maxVida - self._vida, 5*randint(1, 10))
                self._vida += cura
                print(f"{self.anome} fez uma magia de cura e recuperou [green]{cura} pontos[/] de vida.")
        else: print(f"[red]{self._nome}[/] não está mais entre nós...")


""" mais p/ frente, fazer:
melhorar o printPersonagens
pergaminhos com golpes específicos de cada classe (um pergaminho pode ser uma classe)
"""

def play():
    classes = ["Guerreiro", "Mago"]
    personagens = []
    died = []
    def valid_num(s:str):
        """Retorna True se na string só tiver dígitos.
        Caso contrário, retorna False."""
        if len(s) == 0: return False
        for c in s:
            if c.isalpha(): return False
        return True
    def printPersonagens():
        print("\n"*10)
        for p in personagens: print(p, end="")
    def criarPersonagem(tipo:str, nome:str):
        """Retorna um Personagem dado a classe e o nome."""
        if tipo == "Guerreiro": p = Guerreiro(nome)
        elif tipo == "Mago": p = Mago(nome)
        return p
    def fazerPersonagem():
        """Faz o processo de receber os dados para que o player crie um Personagem.
        Retorna None caso o player queira Voltar."""
        while True:
            print(f"Selecione uma [magenta]Classe[/]", end=" ")
            for x in range(0, len(classes)):
                print(f"-> ({x+1})[magenta]{classes[x]}[/]", end=" ")
            print(f"-> ([yellow]R[/])Voltar")
            classe = input().strip().upper()
            if classe == "R": return None
            elif valid_num(classe):
                classe = int(classe)
                if classe < 1 or classe > len(classes):
                    print(f"Digite um número de 1 a {len(classes)} ou [yellow]R[/] para voltar.")
                    continue
                classe = classes[classe-1]
                print(f"Nome do [yellow]Personagem[/]:", end=" ")
                nome = input()
                if len(nome) == 0:
                    print("O nome não pode ser vazio.")
                    continue
                p = criarPersonagem(classe, nome)
                return p
            else: print(f"Digite um número de 1 a {len(classes)} ou [yellow]R[/] para voltar.")
    def reviverPersonagem():
        """Retorna o índice na lista 'died' do Personagem que o player quer reviver.
        Retorna None caso seja necessário Voltar."""
        if len(died) == 0:
            print(f"Não há [yellow]Personagem[/] para [green]reviver[/]!")
            return None
        while True:
            for d in range(0, len(died)): print(f"-> ([yellow]{x+1}[/]){died[d].title}", end=" ")
            print(f"-> ([yellow]R[/])Voltar")
            r = input().strip().upper()
            if r == "R": return None
            elif valid_num(r):
                r = int(r)-1
                if r < 0 or r > len(died)-1:
                    print(f"Digite um número de 1 a {len(died)} ou [yellow]R[/] para Voltar.")
                    continue
                return r
            else: print(f"Digite um número de 1 a {len(died)} ou [yellow]R[/] para Voltar.")
    def eliminarPersonagem():
        """Faz o processo de receber o índice do personagem que o player deseja eliminar e o retorna.
        Retorna None caso seja necessário Voltar."""
        a = len(personagens)
        b = len(died)
        if a+b == 0:
            print(f"Não há [yellow]Personagem[/] para [red]eliminar[/].")
            return None
        while True:
            if a != 0:
                print(f"[yellow]Personagens[/] atuais:", end=" ")
                for x in range(0, a): print(f"-> ([yellow]{x+1}[/]){personagens[x].title}", end=" ")
                print()
            if len(died) != 0:
                print(f"[yellow]Personagens[/] esperando para serem [green]revividos[/]:", end=" ")
                for x in range(0, b): print(f"-> ([yellow]{x+a+1}[/]){died[x].title}", end=" ")
                print()
            print(f"-> ([yellow]R[/])Voltar")
            elim = input().strip().upper()
            if elim == "R": return None
            elif valid_num(elim):
                elim = int(elim)
                if elim < 1 or elim > a+b:
                    print(f"Digite um número de 1 a {a+b} ou [yellow]R[/] para Voltar.")
                    continue
                if elim > a:
                    elim -= a
                    print(f"O {died[elim-1].title} foi [red]eliminado[/] e não pode mais ser [green]revivido[/].")
                    del died[elim-1]
                else:
                    print(f"O {personagens[elim-1].title} foi [red]eliminado[/] e não pode mais ser [green]revivido[/].")
                    del personagens[elim-1]
                return elim
            else: print(f"Digite um número de 1 a {a+b} ou [yellow]R[/] para Voltar.")
    def atacarPersonagem():
        pass


    try:
        while True:
            if len(personagens) == 0:
                print("Não há [yellow]Personagens[/] no jogo. [yellow]Crie[/] um ou [green]reviva[/] os que se foram!")
                while True:
                    print(f"([yellow]C[/])Criar Personagem   ([green]R[/])Reviver   ([red]X[/])Sair")
                    op = input().strip().upper()
                    if len(op) != 0: op = op[0]
                    if op == "X": return
                    elif op == "R":
                        r = reviverPersonagem()
                        if r is not None:
                            died[r].reviver()
                            personagens.append(died[r])
                            del died[r]
                            break
                    elif op == "C":
                        p = fazerPersonagem()
                        if p is not None:
                            personagens.append(p)
                            printPersonagens()
                            print(f"O [magenta]{p.classe}[/] {p.anome} está em jogo!")
                            break
            else:
                print("Selecione uma opção:")
                for x in range(0, len(personagens)):
                    print(f"-> ([yellow]{x+1}[/]){personagens[x].title}", end=" ")
                print("\n-> ([green]R[/])Reviver Personagem -> ([yellow]C[/])Criar Personagem -> ([purple]E[/])Eliminar Personagem -> ([red]X[/])Sair")
                op = input().strip().upper()
                if len(op) != 0: op = op[0]
                if op == "X": break
                elif op == "R":
                    r = reviverPersonagem()
                    if r is not None:
                        died[r].reviver()
                        personagens.append(died[r])
                        del died[r]
                elif op == "C":
                    p = fazerPersonagem()
                    if p is not None:
                        personagens.append(p)
                        printPersonagens()
                        print(f"O {p.title} entrou para o jogo!")
                elif op == "E":
                    eliminarPersonagem()
                    printPersonagens()
                elif valid_num(op):
                    while True:
                        p = int(op)-1
                        if p > len(personagens)-1 or p < 0:
                            print(f"Digite um número de 1 a {len(personagens)} ou uma opção válida.")
                            break
                        print(f"([green]C[/])Curar   ([red]A[/])Atacar   ([yellow]R[/])Voltar")
                        acao = input().strip().upper()
                        if len(acao) != 0: acao = acao[0]
                        if acao == "R": break
                        elif acao == "C":
                            personagens[p].curar()
                            printPersonagens()
                        elif acao == "A":
                            if len(personagens) > 1:
                                while True:
                                    for x in range(0, len(personagens)):
                                        if x != p: print(f"-> ([yellow]{x+1}[/]){personagens[x].title}", end=" ")
                                    print(f"-> ([yellow]R[/])Voltar")
                                    print(f"Selecione um [yellow]Personagem[/]:", end=" ")
                                    op_atack = input().strip().upper()
                                    if len(op_atack) != 0: op_atack = op_atack[0]
                                    if op_atack == "R": break
                                    elif valid_num(op_atack):
                                        p_atacado = int(op_atack)-1
                                        if p_atacado == p or p_atacado > len(personagens)-1 or p_atacado < 0:
                                            print(f"Você só pode atacar um outro [yellow]Personagem[/] existente.")
                                            continue
                                        personagens[p].atacar(personagens[p_atacado])
                                        if not personagens[p_atacado].vivo:
                                            died.append(personagens[p_atacado])
                                            del personagens[p_atacado]
                                        printPersonagens()
                                        break
                            else: print("Não há ninguém para ser atacado. Adicione mais [yellow]Personagens[/] à história!")
                        break
                else: print(f"Selecione uma operação válida ou ([red]X[/]) para Cancelar.")
    except Exception as e:
        print(f"[red]Erro[/]: {e}")
