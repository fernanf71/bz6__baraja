import baraja
class Baraja():

    def __init__(self, palos, numeros):
        self.palos = palos
        self.numeros = numeros
        self.mazocote = baraja.creaBaraja(palos, numeros)

    def barajar(self):
        baraja.barajar(self.mazocote)    
