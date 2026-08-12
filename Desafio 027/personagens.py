from abc import ABC, abstractmethod
from rich import print
import random

class Personagem(ABC):
    def __init__(self, nome = "<não-informado>"):
        self. nome = nome
        self.vida = 0
        self.golpes = list()

    def atacar(self, alvo, poder):
        golpe = random.choice(self.golpes)
        poder = random.randint(1, poder)
        alvo.receber_dano(poder, golpe)

    def receber_dano(self, poder, golpe):
        self.vida -= poder
        if self.vida <= 0:
            print(f"{self.nome} recebeu um [yellow]{golpe}[/] de {poder} de dano!")
            print(f"[red]{self.nome} morreu![/]")
        else:
            print(f"{self.nome} recebeu um [yellow]{golpe}[/] de {poder} de dano!")

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.vida = 30
        self.golpes = ["Soco", "Ataque com lâmina", "Pancada com escudo"]

    def curar(self):
        cura = random.randint(1, 10)
        self.vida += cura
        print(f"{self.nome} curou [green]{cura}[/] e ficou com {self.vida}")

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.vida = 20
        self.golpes = ["Bola de fogo", "Raio", "Estaca de gelo"]

    def curar(self):
        cura = random.randint(1, 6)
        self.vida += cura
        print(f"{self.nome} curou [green]{cura}[/] e ficou com {self.vida}")
