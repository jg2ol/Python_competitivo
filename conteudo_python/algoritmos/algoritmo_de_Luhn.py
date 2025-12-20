# Algoritmo de Luhn
# verificador de números de cartão

def verify_card_number(seq):
    if " " in seq:
        seq = "".join(seq.split(" "))
    if "-" in seq:
        seq = ''.join(seq.split("-"))
    aux = [int(i) for i in seq[::-1]]
    soma = 0
    for i in range(0, len(aux)):
        if i%2:
            soma += 2*aux[i]
            if 2*aux[i] > 9:
                soma -= 9
        else:
            soma += aux[i]
    if not bool(soma%10):
        return "VALID!"
    return "INVALID!"
