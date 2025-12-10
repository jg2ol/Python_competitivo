# Par ou Ímpar (OBI 2004), "fácil"
# 629

n = int(input())
i = 1
while n > 0:
    print(f"Teste {i}")
    jog1 = input()
    jog2 = input()
    for x in range(0, n):
        djog1, djog2 = map(int, input().split())
        if (djog1+djog2) % 2 == 0:
            print(jog1)
        else:
            print(jog2)
    i += 1

    n = int(input())
    if n == 0:
        break