class Pessoa:
    def __init__(self, nome, nasc):
        self._nome = nome
        self._nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if ano > 2026 or ano < 1926:
            return ValueError(f"Ano {ano} é inválido.")
        else:
            self._nascimento = ano

    @property
    def idade(self):
        return 2026 - self._nascimento

    @idade.setter
    def idade(self):
        return PermissionError("Você não pode alterar a idade. Mude o ano de nascimento.")


class Aluno(Pessoa):
    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__(nome, nasc)
        self._curso = curso
        self.cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, c):
        if c not in self.cursos_oficiais:
            return ValueError(f"O curso {c} não está na lista de cursos oficiais.")
        else:
            self._curso = c

    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        if curso not in self.cursos_oficiais and 3 <= len(curso) <= 5:
            self.cursos_oficiais.append(curso)
