# Funções úteis p/ strings

def linha(tam = 30):
    '''
    --> Função que imprime uma linha contínua
    :tam: (opcional) quantidade de caracteres que terá a linha, caso não seja informado terá 30 caracteres
    :return - print: Uma linha com {tam} caracteres
    '''
    print("-"*tam)


def linhaC(caract, tam = 30):
    '''
    --> Função que imprime uma linha contínua com o caractere que desejar
    :tam: (opcional) quantidade de caracteres que terá a linha, caso não seja informado terá 30 caracteres
    :caract: caractere em que será composto a linha (lembre-se de colocar somente um caractere, senão, terá que ajustar seu comprimento)
    :return - print: Uma linha com {tam} caracteres
    '''
    print(f"{caract}"*tam)


def escreva(texto):
    '''
    --> Função que imprime um texto formatado por linhas
    :texto: mensagem que você quer formatar
    :retunr - print: Mensagem formatada
    '''
    tam = len(texto) + 4
    print("-"*tam)
    print(f"  {texto}")
    print("-"*tam)

