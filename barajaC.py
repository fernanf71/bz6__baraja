import baraja
class Baraja():

    def __init__(self, palos, numeros):
        self.palos = palos
        self.numeros = numeros
        self.mazocote = baraja.creaBaraja(palos, numeros)

    def barajar(self):
        baraja.barajar(self.mazocote)

    def repartir(self, num_jugadores, num_cartas):
        jugadores = []
        for i in range(num_jugadores):
            jugadores.append([])

        for carta in range(num_cartas):
            for jugador in range(num_jugadores):
                jugadores[jugador].append(self.mazocote.pop(0))

        return jugadores
