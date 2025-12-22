# Lista todos os nós alcançáveis a partir de um nó inicial

def dfs(matriz, start_node):
    n = len(matriz)
    visitado = [False]*n
    pilha = [start_node]
    result = []
    while pilha:
        no = pilha.pop()
        if not visitado[no]:
            visitado[no] = True
            result.append(no)
            for viz in range(0, n):
                if not visitado[viz] and matriz[no][viz] == 1:
                    pilha.append(viz)
    return result
