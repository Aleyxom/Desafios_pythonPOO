from abc import ABC
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    # manipulando variável nascimento ------------------------------------------------------------
    @property
    def nascimento(self):
        return self._nascimento
    @nascimento.setter
    def nascimento(self, novo_nascimento):
        self._nascimento = novo_nascimento
    # ---------------------------------------------------------------------------------------------

    # manipulando idade ---------------------------------------------------------------------------
    @property
    def idade(self):
        hoje = datetime.now()
        idade = int(hoje.year) - int(self._nascimento)
        return f"{idade} anos"
    @idade.setter
    def idade(self, ano=None):
        print("Não é possível mudar sua idade por aqui.")
    # ---------------------------------------------------------------------------------------------

class Aluno(Pessoa):
    def __init__(self, nome, nascimento):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ["ADM", "TSI", "ADS", "MKT", "ABD"]
        # função para o curso ----------------------------------------------------
        self._curso = self.add_curso()
        # ------------------------------------------------------------------------

    # manipulando curso ---------------------------------------------------------------------------
    @property
    def curso(self):
        return self._curso
    @curso.setter
    def curso(self, curso_inserido):
        self._curso = curso_inserido
    # ---------------------------------------------------------------------------------------------

    # MÉTODOS DA CLASSE ALUNO ---------------------------------------------------------------------
    def add_curso(self):
        curso = ""
        while True:
            curso = input("Informe seu curso: ").strip().upper()
            for c in self.cursos_oficiais:
                if curso == c:
                    return curso
            if len(curso) >= 3:
                while True:
                    resposta = input("Curso inválido. Deseja acrescentá-lo a lista de Curso Oficiais? [S/N] ").strip().upper()[0]
                    if resposta == "S":
                        return curso
                    else:
                        break
            else:
                print("Curso inválido! Informe novamente!")
                input("Aperte ENTER para continuar...")



    # ---------------------------------------------------------------------------------------------