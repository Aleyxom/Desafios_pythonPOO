import os
from metodos_opcoes import *

def indicador_conta_atual(conta_atual):
    print(f"Olá sr(a) {conta_atual.nome}, bem vindo!\nSeu ID é: {conta_atual.id_conta}")
    print("=-" * 30)

def sacar_dinheiro(conta):
    while True:
        try:
            valor = float(input("Informe valor do saque: R$ ").strip())
            if valor > 0:
                break
            else:
                print("[red]Valor inválido! Tente novamente![/]")
        except Exception as erro:
            print(f"Erro: {erro}. Informe valor novamente!")

    conta.sacar(valor)
    input("Aperte ENTER para continuar...")

def saldo(conta):
    os.system("cls")
    indicador_conta_atual(conta)
    print(f"Saldo atual: {conta.saldo}")
    input("Aperte ENTER para continuar...")

def deposito(conta):
    while True:
        os.system("cls")
        indicador_conta_atual(conta)
        try:
            valor = float(input("Quanto deseja depositar? R$").strip())
            if valor > 0:
                conta.depositar(valor)
                break
            else:
                print("Valor inválido! Tente novamente!")
        except Exception as erro:
            print(f"Erro {erro}. Tente novamente!")
    input("Aperte ENTER para continuar...")

def transferir(conta, correntistas):
    valor = 0
    escolha = ""

    while True:
        os.system("cls")
        indicador_conta_atual(conta)
        contas_para_transferir = []
        contas_para_transferir.clear()

        for cc in correntistas:
            if cc.id_conta != conta.id_conta:
                contas_para_transferir.append(cc)

        for i, c in enumerate(contas_para_transferir):
            print(f"{i} - {c.nome}")
        while True:
            try:
                escolha = int(input("Para qual conta deseja transferir? ").strip())
                if escolha >= len(contas_para_transferir):
                    print("Escolha inválida! Tente de novo!")
                else:
                    destinatario = contas_para_transferir[escolha]
                    break
            except Exception as erro:
                print(f"Erro: {erro}! Tente novamente!")

        try:
            while True:
                valor = float(input("Qual o valor? ").strip())
                if valor > 0:
                    break
                else:
                    print("Valor inválido! Tente de novo!")
        except Exception as erro:
            print(f"Erro: {erro}. Tente novamente!")

        # Transferindo agora------------------------------------------------------------
        conta.transferir(valor, destinatario)
        input("Aperte ENTER para continuar...")
        break