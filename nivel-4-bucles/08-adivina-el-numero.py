# Adivina el número

"""
Un juego guarda un número secreto del 1 al 100 (lo escribís vos en el código). La persona va
probando y en cada intento le avisas si el secreto es mayor o menor. Cuando acierta, muestra en
cuántos intentos lo logró.
"""

contador_intentos = 0
numero_secreto = 65

while True:
    numero_usuario = int(input("Bienvenido a adivina el numero secreto, debes elegir un numero entre 1 y 100: "))
    if numero_secreto == numero_usuario and numero_usuario <= 100 and numero_usuario > 0:
        contador_intentos += 1
        print(f"Acertaste! el numero secreto era {numero_secreto}, lo lograste en {contador_intentos} intentos ")
        exit()
    elif numero_secreto > numero_usuario and numero_usuario <= 100 and numero_usuario > 0:
        contador_intentos += 1
        print(f"Mala suerte el numero secreto es mas grande que {numero_usuario}, intentalo de nuevo")

    elif numero_secreto < numero_usuario and numero_usuario <= 100 and numero_usuario > 0:
        contador_intentos += 1
        print(f"Mala suerte el numero secreto es menor que {numero_usuario}, intentalo de nuevo")
    else:
        print("Haz ingresado un numero invalido, por favor ingresa un numero entre 1 y 100")
