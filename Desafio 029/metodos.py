from rich import print
from rich.panel import Panel

lado1 = []
lado2 = []

def mostrar_diario(mensagens):
    dividir_caderno(mensagens)
    montar_caderno()

def dividir_caderno(mensagens):
    for c in range(0,10):
        try:
            lado1.append(mensagens[c])
        except Exception:
            lado1.append("." * 30)

    for c in range(10, 20):
        try:
            lado2.append(mensagens[c])
        except Exception:
            lado2.append("." * 30)

def montar_caderno():
    conteudo = ""
    for cont in range(0,10):
        conteudo += f"{lado1[cont]:<30} | {lado2[cont]:<30}"
        conteudo += "\n"
    caderno = Panel(conteudo, title="Meu Diário", width=70)
    print(caderno)