# Escolha Difícil, fácil
# 103

a, b, c = input().split()
m, n, p = input().split()
a = int(a)
b = int(b)
c = int(c)
m = int(m)
n = int(n)
p = int(p)
if a <= m:
    d1 = m - a
else:
    d1 = 0
if b <= n:
    d2 = n - b
else:
    d2 = 0
if c <= p:
    d3 = p - c
else:
    d3 = 0
print(d1+d2+d3)