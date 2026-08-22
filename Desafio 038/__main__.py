from classes import *

def main():
    mouse = Produto("Mouse", 150)
    teclado = Produto("Teclado Mecânico", 300)
    monitor = Produto("Monitor Gamer 42'", 900)
    placaDeVideo = Produto("Placa de Vídeo Nvidea", 5000)

    c1 = Carrinho()
    c1 + mouse
    c1 + teclado

    print(c1)
    print()

    c2 = Carrinho()
    c2 + monitor
    c2 + placaDeVideo

    print(c2)
    print()

    c1 + c2
    print(c1)
    print()

    print(c1)
    for prod in c1.produtos:
        print(prod.nome)

if __name__ == "__main__":
    main()