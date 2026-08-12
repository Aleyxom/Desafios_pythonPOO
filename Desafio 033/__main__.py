from sistema_funcoes import *

def main():
    try:
        iniciar_sistema()
    except KeyboardInterrupt:
        print("Encerrando...")
        exit()

if __name__ == "__main__":
    main()