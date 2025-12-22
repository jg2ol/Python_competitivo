# Heap --> lista de prioridades do módulo heapq do tipo min-heap (menor valor -> maior prioridade)
# cria uma árvore binária (binary tree) nos bastidores em que cada nó que possui filho
# tem valor menor que o dos filhos

import heapq

heap1 = []

# heappush() --> adiciona um valor ao heap e reorganiza a lista com o novo valor
heapq.heappush(heap1, 1)
heapq.heappush(heap1, 3)
heapq.heappush(heap1, 2)
heapq.heappush(heap1, 5)
heapq.heappush(heap1, 10)
heapq.heappush(heap1, -1)
print(heap1)
# heappop() -- > remove e retorna o elemento com menor prioridade (o de menor valor)
heapq.heappop(heap1)
print(heap1)
print(heapq.heappop(heap1))
print(heap1)

# heappushpop() --> faz os dois simultaneamente p/ maior eficiência
# já que os métodos push e pop fazem uma ordenação binária a cada chamada
# os três métodos possuem complexidade O(log n)
heapq.heappushpop(heap1, 15)
print(heap1, end="\n\n")

# heapify() --> transfomra uma lista em um heap
# O(n)
lista = [-1, 5, 3, 3, 7, 4]
heapq.heapify(lista)
print(lista, end="\n\n")

# estratégia: se inserirmos pares priority-value, podemos mudar de min-heap para max-heap
heap2 = []

heapq.heappush(heap2, (3, 4))
heapq.heappush(heap2, (2, 5))
heapq.heappush(heap2, (1, -2))
print(heap2)
