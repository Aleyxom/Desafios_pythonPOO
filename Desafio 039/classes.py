from abc import ABC, abstractmethod

from pip._internal.commands import search
from rich import print
import re

class Validador(ABC):
    @abstractmethod
    def validar(self, dado):
        pass

    @abstractmethod
    def mensagens(self, dado, resultado):
        pass

class Usuario(Validador):
    def __init__(self):
        self.padrao = r"[a-z0-9_]{5,20}"
    def validar(self, dado):
        if re.fullmatch(self.padrao, dado):
            return True
        else:
            return False

    def mensagens(self, dado, resultado):
        if resultado:
            print("[bold green]✅  Entre 5 - 20 caracteres.[/]")
            print("[bold green]✅  Apenas letras maiúsculas, minúsculas e _.[/]")
        else:
            if not re.fullmatch(r".{5,20}", dado):
                print("[bold red]❌️ Entre 5 - 20 caracteres.[/]")
            if not re.fullmatch(r"[a-z0-9_]", dado):
                print("[bold red]❌️ Apenas letras maiúsculas, minúsculas e _.[/]")

class Email(Validador):
    def validar(self, dado):
        padrao = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if re.fullmatch(padrao, dado):
            return True
        else:
            return False

    def mensagens(self, dado, resultado):
        if resultado:
            print("[bold green]✅  Único @[/]")
            print("[bold green]✅  Apenas letras números e símbolos: . _ % + -")
            print("[bold green]✅  Domínio com ponto corretamente.")
        else:
            if not len(re.findall(r"@", dado)) == 1:
                print("[bold red]❌  Único @[/]")
            if re.search(r"[^A-Za-z0-9@_%+-.]", dado):
                print("[bold red]❌  Apenas letras números e símbolos: . _ % + -")
            if not re.fullmatch(r"\.[A-Za-z]]{2,}$", dado):
                print("[bold red]❌  Domínio com ponto corretamente.")

class Senha(Validador):
    def __init__(self):
        self.padrao = r"^(?=.{8,}$)(?=.*[A-Z])(?=.*[^A-Za-z0-9]).*$"
    def validar(self, dado):
        if re.fullmatch(self.padrao, dado):
            return True
        else:
            return False

    def mensagens(self, dado, resultado):
        if resultado:
            print("[bold green]✅  Mínimo 8 caracteres.[/]")
            print("[bold green]✅  Pelo menos uma letra maiúscula.")
            print("[bold green]✅  Pelo menos um símbolo.")
        else:
            if not re.fullmatch(r"(.{8,}$)", dado):
                print("[bold red]❌️ Mínimo 8 caracteres.[/]")
            if not re.search(r"[A-Z]", dado):
                print("[bold red]❌️ Pelo menos uma letra maiúscula.[/]")
            if not re.search(r"([^A-Za-z0-9])", dado):
                print("[bold red]❌️ Pelo menos um símbolo.")

# DUCK TYPING -----------------------------------------
def validar_dado(objeto, dado):
    try:
        resultado = objeto.validar(dado)
        print(f"O dado informado '{dado}' passou pela validação e retornou: {resultado}")
        objeto.mensagens(dado, resultado)
    except Exception as erro:
        print(f"Erro: {erro}")
# -----------------------------------------------------
