# Fiboonacci, fácil
# link: https://neps.academy/br/exercise/257

n = int(input())
seq = ''

if n == 1:
    print("0")
elif n == 2:
    print("0 1")
elif n == 3:
    print("0 1 1")
elif n > 3:
    fn = 1
    fn1 = 1
    print("0 1 1", end = "")
    for x in range(0, n-3):
        fn2 = fn + fn1
        seq += f" {fn2}"
        fn = fn1
        fn1 = fn2
    print(seq)