# Contagem de Algarismos, fácil
# link: https://neps.academy/br/exercise/189

n = int(input())
numeros = ''
cont_0 = 0
cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0
cont_6 = 0
cont_7 = 0
cont_8 = 0
cont_9 = 0

for x in range(0, n):
    numeros += str(int(input()))

for x in str(numeros):
    if x == '0':
        cont_0 += 1
    elif x == '1':
        cont_1 += 1
    elif x == '2':
        cont_2 += 1
    elif x == '3':
        cont_3 += 1
    elif x == '4':
        cont_4 += 1
    elif x == '5':
        cont_5 += 1
    elif x == '6':
        cont_6 += 1
    elif x == '7':
        cont_7 += 1
    elif x == '8':
        cont_8 += 1
    elif x == '9':
        cont_9 += 1

print(f'0 - {cont_0}')
print(f'1 - {cont_1}')
print(f'2 - {cont_2}')
print(f'3 - {cont_3}')
print(f'4 - {cont_4}')
print(f'5 - {cont_5}')
print(f'6 - {cont_6}')
print(f'7 - {cont_7}')
print(f'8 - {cont_8}')
print(f'9 - {cont_9}')