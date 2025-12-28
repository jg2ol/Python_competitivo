# Solucionador do problema das n rainhas

def dfs_n_queens(n):
    tabuleiro = [[0 for _ in range(0, n)] for _ in range(0, n)]
    solutions = []
    solve(tabuleiro, 0, n, solutions)
    return solutions

def safe(tabuleiro, linha, coluna, n):
    for i in range(0, linha):
        if tabuleiro[i][coluna] == 1:
            return False
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False
    for i, j in zip(range(linha, -1, -1), range(coluna, n)):
        if tabuleiro[i][j] == 1:
            return False
    return True

def solve(tabuleiro, linha, n, solutions):
    if linha == n:
        lista = []
        for l in tabuleiro:
            for i in range(0, n):
                if l[i] == 1:
                    lista.append(i)
        solutions.append(lista)

    for coluna in range(0, n):
        if safe(tabuleiro, linha, coluna, n):
            tabuleiro[linha][coluna] = 1
            solve(tabuleiro, linha+1, n, solutions)
            tabuleiro[linha][coluna] = 0

print(dfs_n_queens(4))
print(dfs_n_queens(5))
