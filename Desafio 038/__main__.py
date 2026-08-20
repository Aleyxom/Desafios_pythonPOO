from classes import *

def main():
    mouse = Produto("Mouse", 150)
    teclado = Produto("Teclado Mecânico", 300)
    monitor = Produto("Monitor Gamer 42'", 900)
    placaDeVideo = Produto("Placa de Vídeo Nvidea", 5000)

    c1 = Carrinho()
    c1 = c1 + mouse
    print(c1)

if __name__ == "__main__":
    main()