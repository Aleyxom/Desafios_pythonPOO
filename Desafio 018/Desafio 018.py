# Crie uma classe chamada Churrasco, onde sejá possível informar quantas pessoas vão participar e mostre quanto de
# carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, nome="<não informado>", qtdPessoas = 0):
        self.nome = nome
        self.qtdPessoas = qtdPessoas
        self.precoCarne = 50.00
        self.gramasPorPessoa = 0.4

    def ResumoChurrasco(self):
        precoTotal = self.gramasPorPessoa * self.qtdPessoas * self.precoCarne
        valorDividido = precoTotal / self.qtdPessoas
        painel = Panel(f"Irão {self.qtdPessoas} pessoas. Cada uma comendo cerca de "
                       f"{self.gramasPorPessoa:.3f} Kg de carne. \n"
                       f"Sendo a carne R${self.precoCarne:.2f} o Kilo. "
                       f"Será necessário gastar R${precoTotal:.2f}\n"
                       f"Cada pessoas pagará: R${valorDividido:.2f}",
                       title=f"Preparação para Churrasco {self.nome}", width=65)
        print(painel)


churrasco1 = Churrasco("Fim de semana", 35)
churrasco1.ResumoChurrasco()