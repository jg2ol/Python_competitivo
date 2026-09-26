from classes import *

def main():
    p1 = Guerreiro("Kratos")
    p2 = Mago("Merlin")
    # play()

    while(p1.vivo and p2.vivo):
        p1.atacar(p2)
        p2.atacar(p1)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
