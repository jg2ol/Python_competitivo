# Tempo de Atraso, fácil
# 149

ha = int(input())
ma = int(input())
hr = int(input())
mr = int(input())

if (hr-ha)*60+(mr-ma) < 45:
    atraso = 45 - ((hr-ha)*60+(mr-ma))
    print(f"Atrasado {atraso}")
else:
    print('Sucesso')