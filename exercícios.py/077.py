# String Complexa
# link: https://neps.academy/br/exercise/2007

n = int(input())
a = input()
conta = 0
contb = 0
contc = 0
contd = 0
conte = 0

for x in a:
    if x == 'A':
        conta = 1
    elif x == 'B':
        contb = 1
    elif x == 'C':
        contc = 1
    elif x == 'D':
        contd = 1
    else:
        conte = 1

if conta + contb + contc + contd + conte >= 3:
    print("Yes")
else:
    print("No")