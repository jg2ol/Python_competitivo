# Insira um período de dízima periódica e descubra a fração geratriz

s = input("Período: ")
q = len(s)

a = int(s)
b = 10**q - 1

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

print(f"Fração geratriz: {int(aorig/mdc)}/{int(borig/mdc)}")
