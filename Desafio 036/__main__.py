from classes import *

def main():
    efetuar_pagamento(Pix(), 5000)
    efetuar_pagamento(Boleto(), 10000)
    efetuar_pagamento(Credito(), 2000)

if __name__ == "__main__":
    main()