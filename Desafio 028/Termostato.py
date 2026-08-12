class Termostato:
    def __init__(self, temperatura = 24):
        self.__temperatura = temperatura
        self.ftemperatura = f"{temperatura:.1f} °C"

    #Criando atributo validável
    @property
    def temperatura(self): #GETTER
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temp): #SETTER
        if temp % 0.5 != 0:
            print("Valor de temperatudo inválido!")
        else:
            if temp > 30:
                valor = 30
            elif temp < 16:
                valor = 16
            else:
                valor = temp
            self.__temperatura = valor
            self.ftemperatura = f"{valor:.1f}ºC"
