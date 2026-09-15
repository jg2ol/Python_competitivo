# Abstract Base Classes
# Docs: https://docs.python.org/pt-br/3/library/abc.html

# biblioteca oficial para Abstração em Python
from abc import ABC, abstractmethod

# serão utilizadas as mesmas classes do exercício anterior (de herança)
# Classe abstrata - Abstract CLass
class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    # método concreto -> todos os filhos terão esse método genérico
    def fazer_aniversario(self):
        self.idade += 1

    # marcador que informa ao Python que este método é obrigatório para todos os filhos dessa classe
    @abstractmethod
    def estudar():
        pass


# Classe especializada
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O(a) aluno(a) {self.nome} fez sua matrícula.")

    def estudar(self):
        print(f"O(a) aluno(a) {self.nome} está estudando {self.curso} na turma {self.turma}.")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O(a) professor(a) {self.nome} começou a aula.")

    def estudar(self):
        print(f"O(a) professor(a) {self.nome} se especializa sobre {self.especialidade} no {self.nivel}.")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O(a) funcionário(a) {self.nome} acabou de bater seu ponto.")

    def estudar(self):
        print(f"O(a) funcionário(a) {self.nome} se especializa na área de {self.setor}.")
