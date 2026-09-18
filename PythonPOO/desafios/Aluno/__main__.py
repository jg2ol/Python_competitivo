from rich import inspect
from classes import Aluno

def main():
    a1 = Aluno("João", 2008, "CONT")
    a1.add_curso("MAT")
    a1.curso = "MAT"
    inspect(a1, methods=True, private=True)


if __name__ == "__main__":
    main()
