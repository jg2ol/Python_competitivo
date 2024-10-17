# Instruções Secretas, médio
# link: https://neps.academy/br/exercise/1473

codigo = input()
while codigo != "99999":
    direcao = ''
    passos = ''

    soma = 0
    for x in codigo[0:2]:
        soma += int(x)
    
    if soma % 2 == 1:
        direcao = 'left'
        direcao_anterior = direcao
    elif soma % 2 == 0 and soma != 0:
        direcao = 'right'
        direcao_anterior = direcao
    else:
        direcao = direcao_anterior
    
    passos = codigo[2:5]

    print(direcao, passos)
    
    codigo = input()