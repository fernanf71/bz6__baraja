import barajaC

#import baraja

palos = ['corazones', 'picas', 'diamantes', 'treboles']
numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
'''
ordenada = baraja.creaBaraja(palos, numeros)
print("Esta es la primera baraja: ",ordenada)

otraBaraja =  baraja.creaBaraja(palos, numeros)
print("Esta es la segunda baraja nada más crearla:", otraBaraja)
baraja.barajar(otraBaraja)
print("Y ahora la he barajado:", otraBaraja)
print("Para que fernando se lo crea, la baraja primera:", ordenada)
'''
miBaraja = barajaC.baraja(palos, numeros)

print(miBaraja.mazocote)
miBaraja.barajar()
print(miBaraja.mazacote)
