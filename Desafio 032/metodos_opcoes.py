from ContaBancaria import *
from funcoes_conta import *
from Funcoes_Contas import *
from random import randint

opcoes_conta = ["SACAR", "SALDO", "DEPÓSITO", "TRANSFERIR", "VOLTAR"]
conta1 = ContaBancaria("00000", "Teste teste", "12345")
conta2 = ContaBancaria("11111", "Aleyxom Carlos", "12345")
correntistas = [conta1, conta2]

def indicador_conta_atual(conta_atual):
    print(f"Olá sr(a) {conta_atual.nome}, bem vindo!\nSeu ID é: {conta_atual.id_conta}")
    print("=-" * 30)

def criar_conta():
    # CRIANDO ID E NOME ----------------------------------------------------------------------
    novo_id = ""
    repetido = False
    while True:
        for c in range(0,5):
            novo_id += str(randint(0,9))
        for cc in correntistas:
            if novo_id == cc.id_conta:
                repetido = True
        if not repetido:
            break

    novo_nome = str(input("Informe seu nome: ").strip().capitalize())
    #-----------------------------------------------------------------------------------------

    conta = ContaBancaria(novo_id, novo_nome)
    correntistas.append(conta)
    print(f"[green]Conta {novo_id}, Sr(a) {novo_nome} criada com sucesso![/]")
    input("Aperte ENTER para continuar...")

def acessar_conta():
    while True:
        # LISTA DE CONTAS PARA ACESSAR -----------------------------------------------------------------
        os.system("cls")
        print("Qual conta deseja acessar? ou [9999] para retornar a tela anterior...")
        for i in range(0, len(correntistas)):
            print(f"( {i} ) / {correntistas[i].id_conta} / {correntistas[i].nome}")
        # ----------------------------------------------------------------------------------------------

        # ESCOLHENDO CONTA -----------------------------------------------------------------------------
        while True:
            try:
                conta_op = int(input("Informe opção: ").strip())
                if conta_op >= len(correntistas) and conta_op != 9999:
                    print("Opção inválida! Escolha novamente!")
                else:
                    break
            except Exception as erro:
                print(f"Erro: {erro}. Tente novamente!")
        if conta_op == 9999: # OPÇÃO DE VOLTAR
            break
        #--------------------------------------------------------------------------------------------------

        # OPÇÕES DA CONTA ---------------------------------------------------------------------------------
        while True:
            os.system("cls")
            indicador_conta_atual(correntistas[conta_op])
            # ESCREVENDO OPÇÕES -----------------------------------------
            for opcao in range(0, len(opcoes_conta)):
                print(f"{opcao} - {opcoes_conta[opcao]}")
            # -----------------------------------------------------------

            # ESCOLHENDO OPÇÕES ----------------------------------------------------------------------------
            while True:
                try:
                    escolha = input("Escolha o que deseja fazer: ").strip()
                    if escolha in ("0", "1", "2", "3", "4"):
                        break
                    else:
                        print("Opção inválida! Escolha novamente!")
                except Exception as erro:
                    print(f"Erro: {erro}. Tente novamente!")

            match escolha:
                case "0":
                    sacar_dinheiro(correntistas[conta_op])
                case "1":
                    saldo(correntistas[conta_op])
                case "2":
                    deposito(correntistas[conta_op])
                case "3":
                    transferir(correntistas[conta_op], correntistas)
                case "4":
                    break
            # -----------------------------------------------------------------------------------------------