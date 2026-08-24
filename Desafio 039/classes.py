from abc import ABC, abstractmethod
import re

class Validador(ABC):
    @abstractmethod
    def validar(self, dado):
        pass

class Usuario(Validador):
    def validar(self, dado):
        padrao = r"[A-Za-z0-9]"
        if (5 <= len(dado) <= 20) and (not re.search(r"\s", dado)) and (not re.search(r"[^\w]", dado)):
            return True
        else:
            return False

class Email(Validador):
    def validar(self, dado):
        padrao = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if re.fullmatch(padrao, dado):
            return True
        else:
            return False

class Senha(Validador):
    def validar(self, dado):
        if (len(dado) >= 8) and (re.search(r"[^\w]", dado)) and (re.search(r"[A-Z]", dado )):
            return True
        else:
            return False

# DUCK TYPING -----------------------------------------
def validar_dado(objeto, dado):
    try:
        resultado = objeto.validar(dado)
        print(f"O dado informado '{dado}' passou pela validação e retornou: {resultado}")
    except Exception as erro:
        print(f"Erro: {erro}")
# -----------------------------------------------------
