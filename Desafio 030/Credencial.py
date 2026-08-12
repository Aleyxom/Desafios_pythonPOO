import hashlib

class Credencial:
    def __init__(self):
        self.__hash = ""

    @property
    def senha(self):
            return self.__hash

    @senha.setter
    def senha(self, nova_senha):
        if self.__hash == "":
               self.__hash = hashlib.sha256(nova_senha.encode()).hexdigest()
        else:
            print("Não é possível criar outra senha!")

    def validar(self, chave):
        if hashlib.sha256(chave.encode()).hexdigest() == self.__hash:
            print("Acesso Liberado!")
        else:
            print("Acesso negado!")