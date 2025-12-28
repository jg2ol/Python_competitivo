# Solucionador da Torre de Hanói

def torre_de_hanoi(n, fonte, destino, auxiliar):
    if n > 0:
        torre_de_hanoi(n - 1, fonte, auxiliar, destino)
        if fonte:
            disco = fonte.pop()
            destino.append(disco)
            result.append(f"{pino_a} {pino_c} {pino_b}")
        torre_de_hanoi(n - 1, auxiliar, destino, fonte)

def hanoi_solver(n):
    global pino_a
    global pino_b
    global pino_c
    global result
    pino_a = list(range(n, 0, -1))
    pino_b = []
    pino_c = []
    result = []
    result.append(f"{pino_a} {pino_b} {pino_c}")
    torre_de_hanoi(n, pino_a, pino_b, pino_c)
    return "\n".join(result)
