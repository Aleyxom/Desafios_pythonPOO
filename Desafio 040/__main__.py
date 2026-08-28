from classes040 import *

def main():
    usuarios = [
        Usuario("Aleyxom", "aleyxom@gmail.com"),
        Usuario("Ana Paula", "anapaula@outlook.com"),
        Usuario("Luan", "luan@gmail.com")
    ]

    alunos = [
        Aluno("Aleyxom", "TI", 3),
        Aluno("Ana", "Farmacia", 1),
        Aluno("Paula", "ADM", 2),
        Aluno("Lucas", "TI", 6)
    ]

    exportar_dados(usuarios, XML())

if __name__ == "__main__":
    main()
