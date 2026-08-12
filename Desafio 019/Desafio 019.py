# Crie uma classe Livro que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao
# fim da leitura.

from rich import print
from rich.panel import Panel
from time import sleep

class Livro:
    def __init__(self, nome = "<desconhecido>", paginas = 0):
        self.nome = nome
        self.paginas = paginas
        self.paginaAtual = 0

    def mostrarLivro(self):
        livro = Panel(f"Página Atual: {self.paginaAtual} / {self.paginas}",
                      title=f"Nome do Livro: {self.nome}", width=40)
        print(livro)

    def passarPaginas(self, num=1):
        self.mostrarLivro()
        contador = 0
        while contador < num:
            if self.paginaAtual < self.paginas:
                self.paginaAtual += 1
                contador +=1
                print(f" pág{self.paginaAtual}> ", end='')
                sleep(0.3)
            else:
                print("\nO livro chegou ao fim!")
                break
        print()
        self.mostrarLivro()

livro1 = Livro("O homem invisível", 20)

livro1.passarPaginas(11)
livro1.passarPaginas(15)


