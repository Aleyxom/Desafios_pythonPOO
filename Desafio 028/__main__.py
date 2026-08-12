from mecanicas import *
from Termostato import *
from rich import inspect

def main():
    t = Termostato()
    while True:
        #inspect(t, private=True, methods=True)
        desenhar_termostato(t)
        mudar_termostato(t)
        atualizar_tela()

if __name__ == "__main__":
    main()