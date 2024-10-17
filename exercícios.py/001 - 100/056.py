# Zerinho ou Um, fácil
# link: https://neps.academy/br/exercise/88

a, b, c = map(int, input().split())

if a == b == c:
    print("*")
elif a != b == c and a != c:
    print("A")
elif a != b != c and a == c:
    print("B")
elif a == b != c and a != c:
    print("C")