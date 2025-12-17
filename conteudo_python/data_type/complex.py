# o python também abrange os números complexos, representados da forma a + bj

num1 = 3 + 4j
num2 = 1 - 1j

soma = num1 + num2
produto = num1*num2
divisao = num1/num2

print(soma)
print(produto)
print(divisao)
print(type(num1), type(soma), type(produto), type(divisao))

# .real, .imag --> retornam o float Re(x) e Im(x) respectivamente
re = num1.real
im = num1.imag

print(re)
print(im)
print(type(re), type(im))

# .conjugate() --> retorna o conjugado de um numero qualquer
num3 = num1.conjugate()
num_aux = 2
num4 = num_aux.conjugate()

print(num3)
print(num4)
print(type(num3), type(num4))