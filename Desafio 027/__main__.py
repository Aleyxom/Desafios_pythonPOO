from personagens import *
from rich import print
from time import sleep

def main():
    p1 = Guerreiro("Lucario")
    p2 = Mago("Kurie")

    while p1.vida > 0 and p2.vida > 0:
        print(f"[blue]{p1.nome}[/]: [green]{p1.vida}[/] de vida")
        print(f"[blue]{p2.nome}[/]: [green]{p2.vida}[/] de vida")
        sleep(1)

        p2.atacar(p1, 20)
        sleep(1)
        if p1.vida <= 0:
            break
        p1.curar()
        sleep(1)

        p1.atacar(p2, 15)
        sleep(1)
        if p2.vida <= 0:
            break
        p2.curar()
        sleep(1)

if __name__ == "__main__":
    main()