from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, mensagem):
        self.mensagem = mensagem
        self.tipo = "black on white"
        self.icone = "💬"

    def mostrar(self):
        painel = Panel(self.mensagem,
                       title=f"{self.icone}{self.__class__.__name__}{self.icone}",
                       style=self.tipo)
        print(painel)

class Alerta(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.icone = "⚠️"
        self.tipo = "black on yellow"

class Erro(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.icone = "🚫"
        self.tipo = "white on red"


