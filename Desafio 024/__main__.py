from bebidas import *
from rich import inspect, print

def main():
    bebida1 = Cafe()
    bebida1.preparar()

    bebida2 = Leite()
    bebida2.preparar()

    bebida3 = Cha()
    bebida3.preparar()


if __name__ == "__main__":
    main()