# Manolo e as Criptomoedas, médio
# 184

n = int(input())
valores = input()
a = []
for x in valores.split():
    a.append(float(x))
print(f"{100*(a[len(a)-1] - a[0]):.2f}")