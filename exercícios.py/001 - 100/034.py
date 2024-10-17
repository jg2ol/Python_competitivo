# Média do Vetor, médio
# 328

n = int(input())
vetor = []

for x in input().split():
    vetor.append(int(x))
print(f"{sum(vetor)/n:.2f}")