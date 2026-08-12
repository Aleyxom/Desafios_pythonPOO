# Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um
# método que permite mostrar a ficha desse gamer.
from rich import print
from rich.table import Table
from rich.panel import Panel

class Gamer:
    def __init__(self, nome="<desconhecido>", nick="<none>"):
        self.nome = nome
        self.nick = nick
        self.listaDeFavoritos = list()

    def adicionarFavorito(self, jogo):
        self.listaDeFavoritos.append(jogo)

    def mostrarPerfil(self):
        painelGamer = Panel(f"Nome: {self.nome}\nApelido: <{self.nick}>",
                            title=f"<Perfil de {self.nick}>", width=len(self.nick)+20, style="blue")
        self.listaDeFavoritos.sort()
        tabelaJogo = Table(title=f"Jogos Favoritos de <{self.nick}>")
        tabelaJogo.add_column("Jogos", justify="center", width=len(self.nick)+20)
        for jogo in self.listaDeFavoritos:
            tabelaJogo.add_row(jogo)
        print(painelGamer)
        print(tabelaJogo)


player1 = Gamer("Aleyxom", "MaskCode")
player1.adicionarFavorito("Super Mario")
player1.adicionarFavorito("Zelda: Majoras Mask")
player1.adicionarFavorito("Pokemon Violet")

player1.mostrarPerfil()