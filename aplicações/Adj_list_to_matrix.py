# Transforma uma lista de adjacências em uma matriz de adjacências

def adjacency_list_to_matrix(dic):
    matriz = []
    for node in dic.keys():
        matriz.append([1 if no in dic[node] else 0 for no in dic.keys()])
    for linha in matriz:
        print(linha)
    return matriz
