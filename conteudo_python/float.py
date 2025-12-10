# o tipo float suporta todo número que contém ponto flutuante
# operações com float's sempre resulta diretamente num float (ou complexo em caso de exponenciação)
num1 = 2.1
num2 = -10.0
soma = num1 + num2
exp = num2**num1
print(soma)
print(exp)
print(type(num1), type(num2), type(soma), type(exp))

# a chamada da função int() em um float é equivalente a função piso(x)
num3 = int(num1)
print(num3)

# o python costuma aproximar números racionais resultantes de operações com 15 casas decimais
# mesmo que "desnecessariamente"
divisao = num2/num1
print(divisao)

# também podemos nós mesmos aproximar números com quantas casas decimais quisermos
num4 = 3.141591
num5 = round(num4, 2) # 2 casas decimais de precisão
print(num5) # 3.14
num6 = round(num4, 4) # 4 casas decimais de precisão
print(num6) # 3.1416
