# cálculo do mdc entre dois números, o método mais rápido (método de Euclides)

a = int(input("a = "))
b = int(input("b = "))

aorig = a
borig = b

r = a%b
if r == 0:
    mdc = min(a, b)

while r != 0:
    mdc = r
    a = b
    b = r
    r = a%b

print(f"O mdc entre {aorig} e {borig} é {mdc}.")
print(f"{aorig}/{mdc} = {aorig/mdc}")
print(f"{borig}/{mdc} = {borig/mdc}")
