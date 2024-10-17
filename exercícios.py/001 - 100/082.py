# Afinação da harpa, fácil
# link: https://neps.academy/br/exercise/1918


seq = input()

num = ""
cordas = ""
ant = 0
for x in range(0, len(seq)):
    if seq[x].isalpha():
        if ant != 0:
            if op == "-":
                print(cordas, "loosen", num)
            else:
                print(cordas, "tighten", num)
            num = ""
            cordas = ""
            ant = 0
        cordas += seq[x]
    elif not seq[x].isdigit() and not seq[x].isalpha():
        op = seq[x]
    else:
        num += seq[x]
        ant = x
    if x == len(seq) - 1:
        if op == "-":
            print(cordas, "loosen", num)
        else:
            print(cordas, "tighten", num)
