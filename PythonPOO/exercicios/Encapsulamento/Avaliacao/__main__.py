from classes import *

def main():
    a1 = Avaliacao("João", "Matemática", 7.5)
    # agora podemos mexer com 'nota' como se fosse público
    a1.nota = 11
    a1.nota = 10
    print(f"O(a) aluno(a) {a1.nome} tirou {a1.nota:.1f} na prova de {a1.disciplina}.")


if __name__ == "__main__":
    main()
