from Funcoes_Contas import *

def main():
    try:
        iniciar_sistema()
    except KeyboardInterrupt:
        print("Encerrado!")
        exit()

if __name__ == "__main__":
    main()