import sqlite3
from datetime import datetime

busca = str(input("Quem você está procurando? ")).strip()

try:
    with sqlite3.connect("meuBanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("select * from amigos where nome LIKE ?", (f"%{busca}%",))

        total = 0

        for total, amigo in enumerate(cur, start=1):
            try:
                data_formatada = datetime.strptime(amigo["nascimento"], "%Y-%m-%d")
                data = str(amigo['nascimento']).split('-')
                dataBrasil = f"{data[2]}-{data[1]}-{data[0]}"

                nascimento = data_formatada.date()
                hoje = datetime.today()

                idade = hoje.year - nascimento.year
                if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
                    idade -= 1

            except (ValueError, TypeError):
                dataBrasil = f"Data inválida '{amigo["nascimento"]}'"
                idade = "erro"

            print(f"{amigo['nome']} nasceu em {dataBrasil} e tem {idade} anos de idade.")

        if total == 0:
            print(f"Não encontrei nenhum registro com: '{busca}'")
        else:
            print(f"Encontrei {total} resultados com '{busca}'")

except sqlite3 as erro:
    print(f"Falha no banco: {erro}")

except Exception as erro:

    print(f"Algo deu errado! {erro}")

# DESAFIO #
# Adapte o código do exercício para que a saída do script:

# mostre uma msg caso não seja achado nenhum registro. FEITO
# trate as datas inválidas e vazias. FEITO
# mostre a data formatada corretamente. FEITO
# mostre a idade real da pessoa. FEITO




