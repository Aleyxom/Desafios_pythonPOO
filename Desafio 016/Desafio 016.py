# Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao
# funcionário se apresentar.
from rich import print
from rich.panel import Panel

class Funcionario:
    # atributos da classe
    empresa = "Curso em Vídeo"

    # atributos de instância
    def __init__(self, nome = "<desconhecido>", setor="<n/i>", cargo="<n/i>"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    # métodos da classe
    def apresentar(self):
        painel = Panel(f"Olá! Meu nome é [white]{self.nome}[/].\nTrabalho no setor: [yellow]{self.setor}[/] "
                       f"e meu cargo é: [red]{self.cargo}[/]!\nÉ um prazer te conhecer!\n{Funcionario.empresa}", title="Apresentação",
                       style="blue", width=50)
        print(painel)


func1 = Funcionario("Aleyxom Carlos", "Desenvolvimento Web", "Junior Developer")
func1.apresentar()