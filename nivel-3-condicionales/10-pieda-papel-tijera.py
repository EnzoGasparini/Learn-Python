# Piedra, Papel y Tijera

"""
Ejercicio: Piedra, papel o tijera
Pedí a dos jugadores que ingresen su elección: piedra, papel o tijera.

El programa debe indicar si ganó el jugador 1, ganó el jugador 2 o hubo un empate.
Si alguno ingresa una opción que no sea válida, debe mostrar un mensaje de error.
"""

jugador1 = input("Ingrese el nombre del jugador 1: ")
jugador2 = input("Ingrese el nombre del jugador 2: ")
eleccion_jugador1 = int(input(f"{jugador1} selecciona tu jugada:\n1.Piedra\n2.Papel\n3.Tijera\n"))
eleccion_jugador2 = int(input(f"{jugador2} selecciona tu jugada:\n1.Piedra\n2.Papel\n3.Tijera\n"))
resultado = ""

if eleccion_jugador1 in (1, 2, 3) and eleccion_jugador2 in (1, 2, 3):

    if eleccion_jugador1 == eleccion_jugador2:
        resultado = "Empate"
    elif eleccion_jugador1 == 1 and eleccion_jugador2 != 2:
        resultado = f"{jugador1} es el ganador."
    elif eleccion_jugador1 == 2 and eleccion_jugador2 != 3:
        resultado = f"{jugador1} es el ganador."
    elif eleccion_jugador1 == 3 and eleccion_jugador2 != 1:
        resultado = f"{jugador1} es el ganador."
    else:
        resultado = f"{jugador2} es el ganador."
else:
    print("Debe ingresar una jugada válida")
    exit()

print("El resultado es: ", resultado)
