from Pessoas_Alunos import *
from rich import print, inspect

lista_alunos = []

def iniciar_sistema():
    while True:
        nome = str(input("Informe seu nome: ").strip())
        if len(nome) > 2:
            break
        else:
            print("Nome inválido. Campo deve ter pelo menos 2 caracteres.")
            input("Aperte ENTER para continuar...")

    while True:
        try:
            ano_nasc = int(input("Informe seu ano de nascimento(YYYY): ").strip())
            if len(str(ano_nasc)) == 4 and datetime.now().year >= ano_nasc >= datetime.now().year - 150:
                break
            else:
                print("Informe uma data válida!")
                input("Aperte ENTER para continuar... ")
        except Exception as erro:
            print(f"Erro: {erro}")
            print("Informe uma data válida!")
            input("Aperte ENTER para continuar... ")

    aluno = Aluno(nome, ano_nasc)
    lista_alunos.append(aluno)

    print(f"{aluno.nome}, {aluno.idade}, curso: {aluno.curso}")