import sqlite3
from datetime import date

busca = str(input("Quem você está procurando? ")).strip()

try:
    with sqlite3.connect("meuBanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("select * from amigos where nome LIKE ?", (f"%{busca}%",))

        total = 0

        for total, amigo in enumerate(cur, start=1):

            txt_nasc = amigo['nascimento']
            info_nasc = ""
            info_idade = ""

            if not txt_nasc:
                info_nasc = "sem data de nascimento."
                info_idade = "não foi possível calcular idade."
            else:
                try:
                    data = date.fromisoformat(str(txt_nasc))
                    info_nasc = f"nasceu em {data:%d/%m/%Y}"
                    nascimento = data
                    hoje = date.today()

                    idade = hoje.year - nascimento.year
                    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day): # tem que ser nessa ordem mm/dd
                        idade -= 1

                    info_idade = f"e tem {idade} anos."

                except (ValueError, TypeError):
                    info_nasc = f"Data inválida '{amigo["nascimento"]}'"
                    info_idade = "não foi possível calcular idade."

            print(f"{amigo['nome']} {info_nasc} {info_idade}.")

        print("-=" * 40)

        if total == 0:
            print(f"Não encontrei nenhum registro com: '{busca}'")
        elif total == 1:
            print(f"Encontrei apenas {total} resultado com '{busca}'")
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




