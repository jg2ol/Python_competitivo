# Função Primo, fácil
# link: https://neps.academy/br/exercise/175

def eh_primo(x):
    q_div = 0

    for a in range(1, int(x**(1/2)//1+2)):
        if x % a == 0:
            q_div += 1

    if q_div == 1:
        return(True)
    else:
        return(False)

x = int(input())
if eh_primo(x):
	print('S')
else:
	print('N')