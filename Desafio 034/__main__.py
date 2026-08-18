from classes import *

def main():
    f = Gerente("Lucas", 3000)
    print(f.calcular_bonus())
    f.salario = 4000
    f.salario = 3000
    f.salario = 4000
    print(f)

if __name__ == "__main__":
    main()