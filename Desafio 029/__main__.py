from Diarios import *

def main():
    meuDiario = Diario("Lucario+85")

    #meuDiario.escrever("Oi Paulinha, tudo bem com você? Hoje eu joguei TCG. Estou com saudades e te amo muito!")
    meuDiario.escrever("Um, dois, três, quatro, cinco, seis, sete...")
    meuDiario.escrever("Amor! Eu te amo :D")
    #meuDiario.escrever("Idéia TCG:")
    #meuDiario.escrever("Jogo parecido com Chaotic")
    #meuDiario.ler()
    meuDiario.ler("Lucario+85")
    #inspect(meuDiario, private=True, methods=True)

if __name__ == "__main__":
    main()