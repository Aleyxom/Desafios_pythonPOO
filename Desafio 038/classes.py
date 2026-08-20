from rich import print
from rich.panel import Panel

# CLASSE CARRINHO DE COMPRAS --------------------------------------------------------------------------------
class Carrinho:
    def __init__(self):
        self.produtos = []
        self._total = 0

    @property
    def total(self):
        for produto in self.produtos:
            self._total += produto.preco
        return f"R${self._total}"

    @total.setter
    def total(self, valor):
        print("Erro! Você não pode mexer nisso assim!")

    def __iadd__(self, objeto):
        self.produtos.append(objeto)

    def __str__(self):
        txt = ""
        for produto in self.produtos:
            txt += f"{produto.nome:<30}{produto.preco:.2f:<7}"
            txt += "\n"
        txt += "_" * 37
        txt += "\n"
        txt += f"{self.total:>37}"
        painel = Panel(txt, title="Recibo")
        print(painel)

# -----------------------------------------------------------------------------------------------------------

# PRODUTOS --------------------------------------------------------------------------------------------------
class Produto:
    def __init__(self,nome:str, preco:float|int):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:.2f})"
# -----------------------------------------------------------------------------------------------------------