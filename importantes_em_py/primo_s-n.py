# algoritmo mais curto p/ saber se um número é primo ou não

n = int(input())
q_div = 0

for x in range(1, int(n**(1/2)//1+2)):
    if n % x == 0:
        q_div += 1

if q_div == 1:
    print('S')
else:
    print('N')
