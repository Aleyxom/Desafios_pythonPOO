from abc import ABC, abstractmethod
import re

class Validador(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def validar(self, dado):
        pass

class Usuario(Validador):
    def __init__(self):
        super().__init__()

    def validar(self, dado):
        if (5 <= len(dado) <= 20) and (not re.search(r"\s", dado)) and (not re.search(r"[^\w]", dado)):
            return True
        else:
            return False

class Email(Validador):
    def __init__(self):
        super().__init__()
        pass
    def validar(self, dado):
        pass

class Senha(Validador):
    def __init__(self):
        super().__init__()
        pass
    def validar(self, dado):
        pass

# DUCK TYPING -----------------------------------------
def validar_dado(objeto, dado):
    try:
        resultado = objeto.validar(dado)
        print(f"O dado informado '{dado}' passou pela validação e retornou: {resultado}")
    except Exception as erro:
        print(f"Erro: {erro}")
# -----------------------------------------------------
