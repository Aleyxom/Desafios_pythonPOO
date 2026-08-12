from abc import ABC, abstractmethod
from time import sleep

class BebidaQuente(ABC):
    def preparar(self):
        print("PREPARANDO:")
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        print("fervendo água", end=" ")
        for c in range(0,3):
            print(".", end=" ")
            sleep(1)
        print("\nÁgua fervida!")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()
        self.nome = "Café"
        self.ingredientes = ["Água", "Pó de Café", "Açúcar"]

    def misturar(self):
        print("Misturando ingredientes!")
        for c in range(0,len(self.ingredientes)):
            sleep(1)
            print(f"Colocando: {self.ingredientes[c]}")
        sleep(1)
        print("\nTudo Pronto!")

    def servir(self):
        print(f"\nServindo {self.nome}! Bom apetite!")
        sleep(1)
        print(":)")

class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()
        self.nome = "Leite"
        self.ingredientes = ["Água quente", "Leite em pó"]

    def misturar(self):
        print("Misturando ingredientes!")
        for c in range(0, len(self.ingredientes)):
            sleep(1)
            print(f"Colocando: {self.ingredientes[c]}")
        sleep(1)
        print("\nTudo Pronto!")

    def servir(self):
        print(f"\nServindo {self.nome}! Bom apetite!")
        sleep(1)
        print(":)")

class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()
        self.nome = "Chá"
        self.ingredientes = ["Água Quente", "Ervas do chá", "Adoçante"]

    def misturar(self):
        print("Misturando ingredientes!")
        for c in range(0, len(self.ingredientes)):
            sleep(1)
            print(f"Colocando: {self.ingredientes[c]}")
        sleep(1)
        print("\nTudo Pronto!")

    def servir(self):
        print(f"\nServindo {self.nome}! Bom apetite!")
        sleep(1)
        print(":)")
