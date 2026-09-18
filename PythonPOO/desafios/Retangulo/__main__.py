from classes import Retangulo

def main():
    r = Retangulo()
    try:
        r.medidas = (4, 5)
        r.base = 3
        r.altura = -2
    except Exception as e:
        print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")

    print(r.medidas)


if __name__ == "__main__":
    main()
