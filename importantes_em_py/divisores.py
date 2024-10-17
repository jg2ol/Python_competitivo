# código que imprime os divisores de um número, melhor forma

n = int(input("Digite um número para saber seus divisores: "))
div1 = []
div2 = []

for a in range(1, int(n**(1/2)//1+1)):
    if n % a == 0:
        div1.append(a)

for a in range(len(div1)-1, 0, -1):
    div2.append(int(n/div1[a]))

for x in div1:
    if x in div2:
        raiz = int(x)
        div2.remove(raiz)

div1.extend(div2)
div1.append(n)

if len(div1) % 2 == 1:
    print(f"O valor digitado é o quadrado de {raiz}. Seus divisores são:")
elif len(div1) == 2:
    print("O valor digitado é um número primo. Portanto, seus divisores são:")
else:
    print(f"O valor digitado não é quadrado perfeito. Seus divisores são:")

for x in div1:
    print(x, end = " ")