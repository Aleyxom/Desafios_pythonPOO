from funcionarios import *

def main():
    func1 = Horista("Aleyxom", 10, 50)
    func1.calc_salario()
    func1.analisar_salario()

    func2 = Mensalista("Ana Paula", 1900)
    func2.calc_salario()
    func2.analisar_salario()

if __name__ == "__main__":
    main()