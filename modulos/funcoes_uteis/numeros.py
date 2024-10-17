# Funções úteis p/ números

def dobro(n, form = False):
    '''
    --> Método simples p/ dobrar um valor numérico
    :n: valor a ser dobrado
    :form: formatar ou não o valor p/ moeda (R$)
    :return: Retorna o dobro do número dito
    '''
    valor = n * 2
    if form:
        return moeda(valor)
    else:
        return valor


def metade(n, form = False):
    '''
    --> Método simples p/ dividir um valor numérico por 2
    :n: valor a ser dividido
    :form: formatar ou não o valor p/ moeda (R$)
    :return: Retorna um float, a metade do número dito
    '''
    valor = n / 2
    if form:
        return moeda(valor)
    else:
        return valor


def aumenta(valor, taxa, form = False):
    '''
    --> Função que aumenta um certo valor em uma certa porcentagem
    :valor: o valor a ser modificado
    :taxa: a porcentagem a ser aumentada
    :form: formatar ou não o valor p/ moeda (R$)
    :return: Retorna o valor modificado
    '''
    res = valor + valor * taxa/100
    if form:
        return moeda(res)
    else:
        return res


def diminui(valor, taxa, form = False):
    '''
    --> Função que diminue um certo valor em uma certa porcentagem
    :valor: o valor a ser modificado
    :taxa: a porcentagem a ser diminuída
    :form: formatar ou não o valor p/ moeda (R$)
    :return: Retorna o valor modificado
    '''
    res = valor - valor * taxa/100
    if form:
        return moeda(res)
    else:
        return res


def moeda(valor, moeda = "R$"):
    '''
    --> Função que formata um valor para uma dada moeda
    :valor: o valor a ser formatado
    :moeda: sigla com o cifrão indicando a moeda para ser transformado o valor
    :return: Retorna uma string com o valor formatado
    '''
    return f"{moeda}{valor:.2f}".replace(".", ",")


def resumo(preco, aum, dim):
    '''--> Função do problema 110 curso em vídeo, Python - Mundo 03'''
    print("-"*34)
    print(f"{"resumo do valor":^34}".upper())
    print("-"*34)
    print(f"Valor Analisado: {moeda(preco):>17}") 
    print(f"Dobro do preço: {dobro(preco, True):>18}")
    print(f"Metade do preço: {metade(preco, True):>17}")
    print(f"{aum}% de aumento: {aumenta(preco, aum, True):>18}")
    print(f"{dim}% de redução: {diminui(preco, dim, True):>18}")
    print("-"*34)


def modulo(n):
    '''
    --> Função que calcula o módulo de um número
    :n: o valor que queremos calcular o módulo
    :return: Retorna o módulo do número
    '''
    if n < 0:
        return -n
    else:
        return n


def parteInteira(n):
    '''
    --> Função que calcula a parte inteira de um número
    :n: número no qual queremos calcular a parte inteira
    :return: Retorna um inteiro, a parte inteira (cálculo matemático) do número dado
    '''
    return int(n // 1)


def leiaInt(texto):
    while True:
        try:
            n = int(input(texto))
        except (ValueError, TypeError):
            print(f"\033[31mErro: por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
        except EOFError:
            print("O usuário tentou escapar da entrada de dados.")
        else:
            return n


def leiaFloat(texto):
    while True:
        try:
            n = float(input(texto))
        except (ValueError, TypeError):
            print(f"\033[31mErro: por favor, digite um número real válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[31mO usuário preferiu não digitar esse número.\033[m")
            return 0
        except EOFError:
            print("Não tente escapar da entrada de dados.")
        else:
            return n


def fatorial(n):
    if n <= 1:
        return 1
    fat = 1
    for x in range(1, n + 1):
        fat *= x
    return fat

