# Código (OBI 2015), fácil
# link: https://neps.academy/br/exercise/47

n = int(input())
seq = input().split()
seq_num = []
cont_100 = 0

for x in seq:
    seq_num.append(int(x))

i = 0
while i <= len(seq_num)-3:
    if seq_num[i] == 1:
        if seq_num[i+1] == 0:
            if seq_num[i+2] == 0:
                cont_100 += 1
    i += 1

print(cont_100)