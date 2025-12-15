# Tratamento de erros --> como ildar com inputs errados e falhas lógicas

# alguns erros comuns: 
# SyntaxError --> quando o código não está de acordo com a linguagem
# print("Olá)

# NameError --> quando tentamos acessar uma variável que não existe naquele escopo
# print(a)

# TypeError --> quando fazemos operações com o tipo errado de dado
# soma = 2 + "2"

# IndexError --> quando tentamos acessar um índice fora do alcance de um iterable
# lista = [1, 2, 3]
# print(lista[4])

# AttributeError --> quando passamos um atributo que não existe para aquele tipo de estrutura
# a = 2
# b = a.split() -> o tipo int não possui o método split()

# try, except, else, finally --> tratamento de erros
# estrutura: try -> código que queremos fazer
# except -> possíveis erros que podem acontecer com os dados de try
# else -> executa se nenhuma exceção for tratada pelos except's
# finally -> sempre é executado independentemente dos erros tratados
# semanticamente, finally é mais usado p/ fechar arquivos, apagar variáveis, etc (limpeza).

# raise --> utilizado para tratar os erros do python de forma personalizada
# com ele, podemos substituir as mensagens de erro
def non_zero(a):
    if a == 0:
        raise ZeroDivisionError("Não é possível dividir por zero")
    return a

try:
    a = non_zero(int(input("Digite um número inteiro: ")))
    x = 2/a
except ZeroDivisionError as dbz:
    print(f"Erro: {dbz}")
else:
    print(f"2/{a} = {x}")
finally:
    print("Boa noite.")
