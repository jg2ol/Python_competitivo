# Primo, fácil
# 247

n = int(input())
q_div = 0

for x in range(0, n):
    if n % (x+1) == 0:
        q_div += 1
if q_div == 2:
    print('S')
else:
    print('N')