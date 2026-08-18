from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str = "", salario:float|int = 1600):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario:float|int = 0):
        if novo_salario > self.__salario:
            print(f"Salário atualizado: de R$ {self.__salario:.2f} para R${novo_salario:.2f}")
            self.__salario = novo_salario
        elif novo_salario == self.__salario:
            print(f"Você está tentando mudar o salário para {novo_salario:.2f} "
                  f"um valor igual ao anterior: R${self.__salario:.2f}")
        else:
            print("O salário é irredutível!")

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self):
        return (f"{self.nome} é um {self.__class__.__name__}, recebe R${self.__salario:.2f} "
                f"e sua bonificação é de R${self.calcular_bonus()}.")

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        bonif = self.salario * 15 / 100
        return f"{bonif:.2f}"

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        bonif = self.salario * 10 / 100
        return f"{bonif:.2f}"

class Designer(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        bonif = self.salario * 8 / 100
        return f"{bonif:.2f}"