from metodos_opcoes import *
from rich import print

opcoes_inicio = ["CRIAR CONTA", "ACESSAR CONTA", "SAIR"]

def iniciar_sistema():
    while True:
        os.system("cls")
        for contador in range(0, len(opcoes_inicio)):
            print(f"{contador + 1} - {opcoes_inicio[contador]}")
        opcao = input("Informe a opção: ").strip()
        if opcao in ("1", "2", "3"):
            match opcao:
                case "1":
                    criar_conta()
                case "2":
                    acessar_conta()
                case "3":
                    print("Encerrado")
                    exit()
        else:
            print("[red]Opção inválida! Escolha novamente![/]")
            input("Aperte ENTER para continuar!")