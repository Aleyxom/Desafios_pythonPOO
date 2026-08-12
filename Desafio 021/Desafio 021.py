# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida podendo escrever frases na cor relativa.
from rich import print

class Caneta:
    def __init__(self):
        self.bocalColocado = True
        self.cor = "white"

    def destampar(self):
        self.bocalColocado = False

    def tampar(self):
        self.bocalColocado = True

    def mudarcor(self, novacor = "white"):
        self.cor = novacor
        print(f"Cor da caneta trocada para {novacor}")

    def escrever(self, texto):
        if self.bocalColocado == False:
            print(f"[{self.cor}]{texto}[/]")
        else:
            print("Você precisa destampar a caneta primeiro!")

caneta1 = Caneta()
caneta1.destampar()
caneta1.mudarcor("yellow")
caneta1.escrever("Pituba")