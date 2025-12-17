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

# raise --> amplia as condições de erros padrões do python
# com ele, podemos substituir as mensagens de erro
def check_age(age):
    if age < 0:
        raise ValueError("A idade não pode ser negativa.")
    return age

try:
    age = check_age(-2)
except ValueError as erro:
    print(f"Erro: {erro}")
else:
    print(f"Idade: {age}")
finally:
    print("Tenha um bom dia!")

# assert --> condicional para erros
def sqrt_positive(x):
    assert x >= 0, "Não pode calcular raiz quadrada de números negativos."
    return x**0.5

try:
    sqrt_positive(-5)
except AssertionError as erro:
    print(f"Erro: {erro}")

# outro uso de raise (sem argumento)
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')
