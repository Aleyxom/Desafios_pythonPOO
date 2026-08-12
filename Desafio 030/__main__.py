from Credencial import *
from rich import print, inspect

def main():
    c = Credencial()
    c.senha = "12345678"
    # c.senha = "12345678" -> não foi possível criar outra senha

    #print(c.senha)
    inspect(c, private=True, methods=True)

    c.validar("Lucario+85")
    c.validar("12345678")

if __name__ == "__main__":
    main()