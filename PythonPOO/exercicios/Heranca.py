from rich import print, inspect
# Herança em Python

# Classe mãe - Super Class
class Pessoa:
    def __init__(self, nome="", idade=0):
        # todos os filhos dessa classe irão ter atributos 'nome' e 'idade'
        self.nome = nome
        self.idade = idade

    # e também terão o método 'fazer_aniversario()'
    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        # os filhos sempre devem iniciar primeiramente como filho da classe mãe
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazer_matricula(self):
        print(f"O(a) aluno(a) {self.nome} fez sua matrícula.")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O(a) professor(a) {self.nome} começou a dar aula.")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O(a) funcionário(a) {self.nome} bateu o ponto.")


a1 = Aluno("João", 17, "Matemática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor("Antônio", 37, "Física", "Mestre")
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario("Maria", 20, "Secretária", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods=True)
