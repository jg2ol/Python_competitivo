# Selection sort
# O(n²)

def selection_sort(lista):
    if len(lista) <= 1:
        return lista
    result = []
    for i in range(0, len(lista)):
        menor = min(lista)
        result.append(menor)
        lista.remove(menor)
    return result
