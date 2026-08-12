# Crie uma classe Produto, onde podemos cadastrar nome e preço. Crie também um método que mostre uma etiqueta de preço
# do produto

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome = "<None>", preco = 0.00):
        self.nome = nome
        self.preco = preco

    def mostrarEtiqueta(self):
        espaco = 50 - (len(self.nome) + 14)
        etiqueta = Panel(f"{self.nome:<}{"." * espaco} R${self.preco:^9.2f}", title=f"Etiqueta {self.nome}", width=50)
        print(etiqueta)

produto1 = Produto("Feijão", 8.99)
produto2 = Produto("Arroz", 7.50)
produto3 = Produto("Ovo de Pascoa", 75)

produto1.mostrarEtiqueta()
produto2.mostrarEtiqueta()
produto3.mostrarEtiqueta()
