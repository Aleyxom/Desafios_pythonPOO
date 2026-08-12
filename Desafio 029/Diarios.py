from rich import print, inspect
from metodos import *
import math

class Diario:
    def __init__(self, senha = "12345"):
        self.__senha = senha
        self.__segredos = []

    def ler(self,senha = None):
        if self.__senha == senha:
            print("[bold green]Acesso autorizado![/]")
            mensagens = self.segredo
            mostrar_diario(mensagens)
        else:
            print("[bold red] Acesso negado! Senha incorreta![/]")

    def escrever(self, texto):
        self.segredo = texto

    @property #GETTER
    def senha(self):
        raise PermissionError("Ninguém poder ver a senha!")

    @property
    def segredo(self):
        return self.__segredos

    @segredo.setter
    def segredo(self, texto):
        if len(self.__segredos) < 20:
            if len(texto) > 30:
                for parte in range(0, len(texto), 30):
                    self.__segredos.append(texto[parte:parte+30])
                    if len(self.__segredos) >= 20:
                        print("Diário cheio! Não há mais linhas para escrever!")
            else:
                self.__segredos.append(texto)
        else:
            print("Diário cheio! Não há mais linhas para escrever!")