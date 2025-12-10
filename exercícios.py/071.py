# Flipper, fácil
# link: https://neps.academy/br/exercise/1736

seq = input()
conth = 0
contv = 0

for x in seq:
    if x == 'H':
        conth += 1
    elif x == 'V':
        contv += 1

if contv % 2 == 0 and conth % 2 == 0:
    print('1 2')
    print('3 4')
elif contv % 2 == 0 and conth % 2 == 1:
    print('3 4')
    print('1 2')
elif contv % 2 == 1 and conth % 2 == 0:
    print('2 1')
    print('4 3')
elif contv % 2 == 1 and conth % 2 == 1:
    print('4 3')
    print('2 1')