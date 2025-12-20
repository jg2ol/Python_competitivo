# Algoritmo quick sort
# O(n²) no pior caso

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[-1]
    menor, maior, igual = [], [], []
    for num in lista:
        if num < pivot:
            menor.append(num)
        elif num == pivot:
            igual.append(num)
        else:
            maior.append(num)
    result = quick_sort(menor)
    result.extend(igual)
    result.extend(quick_sort(maior))
    return result
