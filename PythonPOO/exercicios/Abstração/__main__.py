from classes import Aluno, Professor, Funcionario
# não preciso importar a classe Pessoa pois não irei gerar objeto da classe abstrata


# estrutura de código útil para projetos grandes
def main():
    a1 = Aluno("João", 17, "Matemática", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()

    p1 = Professor("Antônio", 43, "História", "Mestrado")
    p1.dar_aula()
    p1.estudar()

    f1 = Funcionario("Maria", 37, "Secretária", "Secretaria")
    f1.bater_ponto()
    f1.estudar()


if __name__ == "__main__":
    main()
