import random

class NoHayMonedasParaPremioException(Exception):
    pass
class NoHayMonedaException(Exception):
    pass

class Tragamonedas:

    def __init__(self):
        self.monedas = int
        self.monedas_tirada = 0
        self.tirada = [1,1,1]

    def insertar_moneda(self):
        if self.monedas < (self.monedas_tirada+1)*10:
            raise NoHayMonedasParaPremioException()
        self.monedas += 1
        self.monedas_tirada += 1

    def tirar(self):
#        self.tirada[0] = random.randint(1,10)
#        self.tirada[1] = random.randint(1,10)
#        self.tirada[2] = random.randint(1,10)
        premio = 0
        if self.monedas_tirada == 0:
            raise NoHayMonedaException()
        if self.tirada[0] == self.tirada[1] == self.tirada[2]:
            premio = self.monedas_tirada * self.tirada[0]
            self.monedas -= premio
        self.monedas_tirada = 0
        return premio