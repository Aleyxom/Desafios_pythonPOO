from abc import ABC, abstractmethod
from functools import total_ordering

from rich import print
from rich.panel import Panel
from rich.table import Table

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    def consultar(self):
        tabela = Table()
        tabela.add_column("DESCRIÇÃO")
        tabela.add_column("VALORES")

        tabela.add_row("MOTO", f"R$ {(self.distancia * 0.5):.2f}")
        if self.distancia >= 50:
            tabela.add_row("CAMINHÃO", f"R$ {(self.distancia * 1.20):.2f}")
        else:
            tabela.add_row("CAMINHÃO", "VIAGEM MUITO CURTA (MÍN. 50Km)")

        if self.distancia <= 10:
            tabela.add_row("DRONE", f"R$ {(self.distancia * 9.50)}")
        else:
            tabela.add_row("DRONE", "DISTÂNCIA MUITO LONGA (MÁX 10Km)")

        print(tabela)


    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        mensagem = "O total do seu frete foi:\n"
        mensagem += f"R$ {self.frete:.2f}\n"
        mensagem += f"Para a distância de {self.distancia}km"
        painel = Panel(mensagem, title="MOTO", width=40)
        print(painel)

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20

    def calc_frete(self):
        #min 50km
        if self.distancia >= 50:
            self.frete = self.distancia * self.fator
            mensagem = "O total do seu frete foi:\n"
            mensagem += f"R$ {self.frete:.2f}\n"
            mensagem += f"Para a distância de {self.distancia}km"
            painel = Panel(mensagem, title="CAMINHÃO", width=40)
            print(painel)
        else:
            print("A distância informada é muito curta e não pode ser fretada por caminhão!\n Mínimo 50Km")

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.5

    def calc_frete(self):
        #max 10km
        if self.distancia <= 10:
            self.frete = self.distancia * self.fator
            mensagem = "O total do seu frete foi:\n"
            mensagem += f"R$ {self.frete:.2f}\n"
            mensagem += f"Para a distância de {self.distancia}km"
            painel = Panel(mensagem, title="DRONE", width=40)
            print(painel)
        else:
            print("A distância informada é muito longa para ser entregue por Drone!\nMáximo 10Km")