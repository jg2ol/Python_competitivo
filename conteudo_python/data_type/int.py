# os limites são dinamicos, se adaptam à memória disponível
# ou seja, não há limite para números em python
# o tipo int suporta qualquer inteiro sem ponto flutuante

num1 = 2
num2 = 5

divisao = num1/num2
soma = num1 + num2
exp = num1**num2
# a função power(base, expoente, módulo) faz a exponenciação com ou sem módulo

print(soma)
print(divisao)
print(exp)

# bin(num) --> representação binária de um número
# oct(num) --> representação octal de um número
# hex(num) --> representação hexadecimal de um número
# também funcionam para float's
print(bin(1005))
print(oct(1005))
print(hex(1005))
