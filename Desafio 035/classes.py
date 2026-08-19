from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome:str, tamanho_em_bytes:float|int):
        self.nome = nome
        self._extensao = self.__class__.__name__.lower()
        self.tamanho = f"{tamanho_em_bytes / 1000000:.1f}MB"
        self.nome_completo = f"{self.nome}.{self._extensao.lower()} ({self.tamanho})"

    @abstractmethod
    def abrir(self):
        print(f"Abrindo arquivo {self.nome_completo}")

class PDF(Arquivo):
    def __init__(self, nome, tamanho_em_bytes):
        super().__init__(nome, tamanho_em_bytes)

    def abrir(self):
        print(f"Abrindo arquivo {self.nome_completo} no Adobe Reader.")

class DOC(Arquivo):
    def __init__(self, nome, tamanho_em_bytes):
        super().__init__(nome, tamanho_em_bytes)

    def abrir(self):
        print(f"Abrindo arquivo {self.nome_completo} no Microsoft Word.")

# DUCKT TYPING ---------------------------
def abrir_arquivo(objeto):
    try:
        objeto.abrir()
    except Exception as erro:
        print(f"Não foi possível abrir. Erro: {erro}")