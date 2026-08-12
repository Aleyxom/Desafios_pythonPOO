from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome = "<não-informado>", sal_bruto = 0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario_minimo_atual = 1612
        self.inss = 7.5

    def analisar_salario(self):
        print("Salário analisado!")
        mensagem = f"Olá, {self.nome}"
        analise = (self.sal_bruto - (self.sal_bruto * self.inss) /100) / self.salario_minimo_atual
        mensagem += f"\nVocê recebe {analise:.1f} salários mínimos"
        painel = Panel(mensagem, title=f"Funcionário {self.nome}", width=50)
        print(painel)

    @abstractmethod
    def calc_salario(self):
        pass

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas
        self.sal_bruto = self.valor_hora * self.horas_trabalhadas

    def calc_salario(self):
        salario_liquido = self.sal_bruto - ((self.sal_bruto * self.inss)/100)
        print(f"Seu salário líquido foi de: R${salario_liquido:.2f}")

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)

    def calc_salario(self):
        salario_liquido = self.sal_bruto - (self.sal_bruto * self.inss) / 100
        print(f"Seu salário líquido foi de: R${salario_liquido:.2f}")
