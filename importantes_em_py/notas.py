# notas de alunos e suas médias

alunos = []
aluno = []
notas = []

while True:
    nome = input("Nome: ")
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    media = float(f"{(n1 + n2)/2:.1f}")
    notas.append(n1)
    notas.append(n2)
    aluno.append(nome)
    aluno.append(notas[:])
    aluno.append(media)
    alunos.append(aluno[:])
    notas.clear()
    aluno.clear()
    
    res = input("Quer continuar? (S/N) ").strip().upper()[0]
    while res != "S" and res != "N":
        print("Resposta inválida.")
        res = input("Quer continuar? (S/N) ").strip().upper()[0]
    if res == "N":
        break

print("-="*25)
print(f"{"Nº":<4} {"NOME":<15} {"MÉDIA"}")
print("-"*30)
for x in alunos:
    print(f"{alunos.index(x) + 1:<4} {x[0]:<15} {x[2]:^5}")

while True:
    print("-"*53)
    n = int(input("Quer mostrar as notas de qual aluno? (999 cancela) "))
    if n == 999:
        print(f"{" CANCELANDO... ":^52}")
        break
    else:
        print(f"Notas de {alunos[n - 1][0]}: {alunos[n - 1][1][0]} e {alunos[n - 1][1][1]}, com média igual a {alunos[n - 1][2]}")
