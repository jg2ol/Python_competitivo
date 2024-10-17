# cálculos, fácil
# 1602

a, b = input().split()
a = int(a)
b = int(b)
if (a+b) > (a-b):
    print(a+b)
    print(a-b)
else:
    print(a-b)
    print(a+b)