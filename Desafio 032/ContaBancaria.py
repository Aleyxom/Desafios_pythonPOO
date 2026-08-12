from rich import print
import hashlib
from getpass import getpass

class ContaBancaria:
    def __init__(self, id, titular, senha = None):
        self._id = id
        self._titular = titular
        self.__saldo = 0
        if senha is None:
            self.__hash = senha
        else:
            self.__hash = hashlib.sha256(senha.encode()).hexdigest()
        self.nome = titular

        # INICIALIZANDO CONTA --------------------------------------------------
        self.pede_senha()
        #print("Senha criada!")

    # Atributos validáveis -----------------------------------------------------
    @property
    def id_conta(self):
        return self._id


    @property
    def saldo(self):
        return f"R${self.__saldo:.2f}"
    @saldo.setter
    def saldo(self, valor):
        pass

    @property
    def hash(self):
        return self.__hash
    @hash.setter
    def hash(self, senha):
        pass

    # Métodos ------------------------------------------------------------------
    def validar_senha(self, chave):
        if self.__hash == hashlib.sha256(chave.encode()).hexdigest():
            return True
        else:
            return False

    def pede_senha(self):
        try:
            if self.__hash is None:
                self.__hash = hashlib.sha256(getpass("Crie uma senha: ", echo_char="*").encode()).hexdigest()
                print("Senha criada!")
        except Exception as erro:
            print(erro)

    def sacar(self, valor, chave = None):
        if chave is None:
            chave = getpass("Informe a senha: ", echo_char="*")
        if self.validar_senha(chave):
            try:
                if valor >= 0 and valor <= self.__saldo:
                    self.__saldo -= valor
                    print(f"Saque no valor de R${valor:.2f} realizado!")
                    return True
                else:
                    print("Valor de saque inserido é inválido!")
                    return False
            except Exception as erro:
                print(f"Saque não realizado! Erro: {erro}")
                return False
        else:
            print("Senha incorreta! Saque não autorizado!")
            return False

    def depositar(self, valor):
        try:
            if valor >= 0:
                self.__saldo += valor
                print(f"Depósito de R${valor:.2f} realizado!")
        except Exception as erro:
            print(f"Deposito não realizado. Erro: {erro}")

    def transferir(self, valor, destinatario):
        chave = getpass("Informe a senha: ", echo_char="*")
        if self.validar_senha(chave):
            if valor <= self.__saldo:
                self.__saldo -= valor
                destinatario.depositar(valor)
            else:
                print("[red]Valor insuficiente. Tente novamente mais tarde![/]")
        else:
            print("[red]Senha inválida! Tente novamente mais tarde![/]")