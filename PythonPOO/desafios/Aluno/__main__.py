from classes import Aluno

def main():
    a1 = Aluno("João", 2008, "CONT")
    a1.add_curso("MAT")
    a1.curso = "MAT"
    print(a1.curso)
    print(a1.cursos_oficiais)
    print(a1)


if __name__ == "__main__":
    main()
