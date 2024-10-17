# Código com todas as possibilidades de personalização de mensagem

# estilo da fonte: sem estilo, negrito, sublinhado, inverte da letra pro fundo, do fundo pra letra
estilo = [0, 1, 4, 7]
# cores da fonte e fundo: branco, veremelho, verde, amarelo, azul, magenta, ciano e cinza
letra_cores = [30, 31, 32, 33, 34, 35, 36, 37]
fundo_cores = [40, 41, 42, 43, 44, 45, 46, 47]

texto_teste = "Meu deus, o Python tem cores!"
for x in estilo:
    for y in letra_cores:
        for z in fundo_cores:
            print(f"\033[{x};{y};{z}m{texto_teste}\033[m")
    print()
