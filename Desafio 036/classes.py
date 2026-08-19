from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:float|int = 0):
        self._valor = valor
        self.fvalor = f"R$ {valor:.2f}"

    @property
    def valor(self):
        return self.fvalor
    @valor.setter
    def valor(self, valor):
        self._valor = valor
        self.fvalor = f"R$ {valor:.2f}"

    def pagar(self):
        print("Pagamento feito!")

class Boleto(Pagamento):
    def pagar(self):
        print(f"Pagamento confirmado no valor de {self.fvalor} via Boleto.")

class Pix(Pagamento):
    def pagar(self):
        print(f"Pagamento confirmado no valor de {self.fvalor} via Pix.")

class Credito(Pagamento):
    def pagar(self):
        print(f"Pagamento confirmado no valor de {self.fvalor} via Cartão de Crédito.")

# DUCK TYPING --------------------------------
def efetuar_pagamento(objeto, valor):
    objeto.valor = valor
    objeto.pagar()
# --------------------------------------------