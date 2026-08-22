from rich import print
from rich.panel import Panel

# CLASSE CARRINHO DE COMPRAS --------------------------------------------------------------------------------
class Carrinho:
    def __init__(self):
        self.produtos = []
        self._total = 0

    @property
    def total(self):
        self._total = 0
        for produto in self.produtos:
            self._total += produto.preco
        return f"R${self._total:.2f}"
    @total.setter
    def total(self, valor):
        print("Erro! Você não pode mexer nisso assim!")

    def __add__(self, objeto):
        if objeto.__class__.__name__ == "Carrinho":
            for obj in objeto.produtos:
                self.produtos.append(obj)
        elif objeto.__class__.__name__ == "Produto":
            self.produtos.append(objeto)

    def __str__(self):
        txt = ""
        for produto in self.produtos:
            txt += f"{produto.nome:<30}R${produto.preco:>7.2f}"
            txt += "\n"
        txt += "_" * 39
        txt += "\n"
        txt += f"{self.total:>39}"
        return txt
# -----------------------------------------------------------------------------------------------------------

# PRODUTOS --------------------------------------------------------------------------------------------------
class Produto:
    def __init__(self,nome:str, preco:float|int):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:.2f})"
# -----------------------------------------------------------------------------------------------------------