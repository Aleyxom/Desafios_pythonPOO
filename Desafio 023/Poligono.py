from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self):
        self.qtd_lados = 0

    #metodos
    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligono):
    def __init__(self, lados):
        super().__init__()
        self.qtd_lados = 4
        self.lados = lados

    #metodos
    def perimetro(self):
        perimetro = self.lados * self.qtd_lados
        print(f"O perímetro desse QUADRADO é {perimetro:.1f}m")

    def area(self):
        area = self.lados * self.lados
        print(f"A aréa desse QUADRADO é {area:.1f}m²")

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__()
        self.qtd_lados = 0
        self.raio = raio

    # metodos
    def perimetro(self):
        perimetro = 2 * 3.14 * self.raio
        print(f"O perímetro desse CÍRCULO é {perimetro:.1f}m")

    def area(self):
        area = 3.14 * (self.raio ** 2)
        print(f"A aréa desse CÍRCULO é {area:.1f}m²")
