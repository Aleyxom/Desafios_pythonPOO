from Retangulos import *

def main():
    forma = Retangulo()
    forma.altura = 10
    forma.base = 10
    print(forma.medidas)

    forma.altura = 8
    forma.base = 5
    print(forma.medidas)

    forma.medidas = (5, 6)
    inspect(forma, private=True, methods=True)

if __name__ == "__main__":
    main()