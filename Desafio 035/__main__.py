from classes import *

def main():
    a1 = PDF("contrato", 1550000)
    a2 = DOC("prova_portugues", 500500)

    a1.abrir()
    a2.abrir()

    abrir_arquivo(a1)
    abrir_arquivo(a2)

if __name__ == "__main__":
    main()