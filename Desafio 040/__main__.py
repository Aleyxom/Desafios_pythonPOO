from classes040 import *

def main():
    usuarios = [
        Usuario("Aleyxom", "aleyxom@gmail.com"),
        Usuario("Ana Paula", "anapaula@outlook.com")
    ]

    alunos = [
        Aluno("Aleyxom", "TI", 3),
        Aluno("Ana", "Farmacia", 1),
        Aluno("Paula", "ADM", 2)
    ]

    exportar_dados(alunos, XML())

if __name__ == "__main__":
    main()
