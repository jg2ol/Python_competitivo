# Conversão de Inteiro para Binário, fácil
# link: https://neps.academy/br/exercise/195

n = int(input())
seq_bin = ''
bin = ''

while n != 1 and n != 0:
    bin += str(n % 2)
    n = n//2

seq_bin += str(n % 2)
for x in bin:
    seq_bin += str(x)

print(seq_bin)