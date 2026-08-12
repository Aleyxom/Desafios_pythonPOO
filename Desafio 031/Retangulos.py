from rich import print, inspect

class Retangulo:
    def __init__(self):
        self._base = 0
        self._altura = 0
        self._area = self._base * self._altura

    @property
    def base(self):
        return self._base
    @base.setter
    def base(self, valor):
        try:
            if valor >= 0:
                self._base = valor
                self._area = self._base * self._altura
            else:
                print("Insira apenas números positivos!")
        except Exception as a:
            print(f"Erro: {a}")

    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, valor):
        self._altura = valor
        self._area = self._base * self._altura

    @property
    def area(self):
        return self._area
    @area.setter
    def area(self, algo):
        raise PermissionError("Você não pode manipular esse valor!")

    @property
    def medidas(self):
        msg = ""
        msg += f"Base: {self._base}\n"
        msg += f"Altura: {self._altura}\n"
        msg += f"Area: {self._area}"
        return msg
    @medidas.setter
    def medidas(self, valores):
        self._base = valores[0]
        self._altura = valores[1]
        self._area = self._base * self._altura
