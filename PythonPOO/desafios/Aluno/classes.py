from datetime import date
from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if date.today().year - 100 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido.")

    @property
    def idade(self):
        return 2026 - self._nascimento

    @idade.setter
    def idade(self):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento.")


class Aluno(Pessoa):
    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]
    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso

    def __str__(self):
        return f"O aluno {self._nome} de {self.idade} anos de idade cursa {self.curso}."

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, c:str):
        c = c.upper()
        if c not in self.cursos_oficiais:
            self._curso = None
            raise ValueError(f"O curso {c} não está na lista de cursos oficiais.")
        else:
            self._curso = c

    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        if curso in Aluno.cursos_oficiais:
            print(f"O curso {curso} já está na lista dos cursos oficiais.")
        else:
            if 3 <= len(curso) <= 5:
                Aluno.cursos_oficiais.append(curso)
            else:
                raise ValueError(f"O nome {curso} está fora do padrão de cursos oficiais.")
