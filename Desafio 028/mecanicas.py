import numpy as np
import os
from time import sleep
from rich import print
from rich.panel import Panel

def desenhar_termostato(t):
    conteudo = ""
    conteudo += "MIN. "
    for c in np.arange(16.0,30.5, 0.5):
        if c <= t.temperatura:
            if t.temperatura <= 23:
                conteudo += "[blue on blue] [/]"
            else:
                conteudo += "[red on red] [/]"
        else:
            conteudo += "[white on white] [/]"
    conteudo += " .MAX"
    termo = Panel(conteudo, title="TERMOSTATO", width=50)
    print(termo)
    print(f"A temperatura é {t.temperatura} ou {t.ftemperatura}")

def mudar_termostato(termostato):
    try:
        valor = str(input("Insira ( - ) ou ( + ) para alterar o termostato: ")).strip()
        if valor not in ('+', '-'):
            print("[bold red]Insira apenas + ou -[/]")
            sleep(1)
        else:
            if valor == "+":
                termostato.temperatura += 0.5
            elif valor == "-":
                termostato.temperatura -= 0.5
    except ValueError:
        raise ValueError("Insira apenas + ou -")
    except KeyboardInterrupt:
        print("Finalizando programa!")
        exit()

def atualizar_tela():
    # Limpa o terminal no Windows (cls) ou Linux/Mac (clear)
    os.system('cls' if os.name == 'nt' else 'clear')