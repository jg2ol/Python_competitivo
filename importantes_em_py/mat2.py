# Insira os números e descubra o período da fração

a = input("a: ")
b = input("b: ")
r = len(b)

if int(b) < int(a):
    temp = a
    a = b
    b = a

while len(b) > len(a):
    a = "0" + a

a = int(a)
b = int(b)
k = int(b/a//1)

res = 0
q = int(input("q: "))
for x in range(0, q):
    a *= k
    res = res*10**r + a

print(res)
