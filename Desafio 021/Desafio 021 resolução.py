from rich import print

class Caneta:
    def __init__(self, cor="azul"):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha

        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!")
        else:
            print(f"{self.cor}{msg}[/]")

    def quebrarlinha(self, num = 1):
        for c in range(0, num):
            print()

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False



c1 = Caneta("vermelha")
c2 = Caneta("verde")
c3 = Caneta("Wh")

c1.destampar()
c2.destampar()

c1.escrever("Olá mundo!")
c1.quebrarlinha(2)

c2.escrever("Olá mundo de novo!")
c2.quebrarlinha()

c3.escrever("Um, dois, três!")