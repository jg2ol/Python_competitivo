# código que imprime os "n" primeiros termos da sequência de Fibonacci

n = int(input("Você quer quantos termos da sequência? "))

if n == 1:
    print("1")
elif n == 2:
    print("1 1")
elif n > 2:
    fn = 1
    fn1 = 1
    print("1 1", end = "")
    for x in range(0, n-2):
        fn2 = fn + fn1
        print(f" {fn2}", end = "")
        fn = fn1
        fn1 = fn2
else:
    print(0)
