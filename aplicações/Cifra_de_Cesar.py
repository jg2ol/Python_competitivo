# Código que codifica e decodifica string's pela Cifra de Cesar

# dado a mensagem a ser criptografada e o espaçamento entre as letras com suas correpondentes
# retorna a mensagem criptorafada
def cesar(text, shift, encrypt = True):
    # se quisermos decodificar uma mensagem, basta fazer o fatiamento de string's
    # com shift negativo (e de mesmo módulo)
    if not encrypt:
        shift *= -1
    
    # algoritmo q obtém o "alfabeto" de Cesar
    alf = "abcdefghijklmnopqrstuvwxyz"
    cript = alf[shift:] + alf[:shift]
    
    # para codificar letras maiúsculas também
    alf += alf.upper()
    cript += cript.upper()
    
    # fazendo o "tradutor"
    trad = str.maketrans(alf, cript)
    return text.translate(trad)

# Função que codifica uma mensagem dado o espaçamento
def code(text, shift):
    return cesar(text, shift)

# Função que decodifica uma mensagem dado o espaçamento
def decode(text, shift):
    return cesar(text, shift, False)
