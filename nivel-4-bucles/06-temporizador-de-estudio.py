# Temporizador de estudio

"""
Temporizador de estudio

Una app de estudio muestra una cuenta regresiva de minutos.

Datos que pedís: cuántos minutos dura la sesión (un número entero).

Qué muestra: una línea por cada minuto que falta, desde el total hasta 1, con el texto Faltan N min. Al terminar, el mensaje ¡Sesión terminada!.
"""

minutos_sesion = int(input("Ingrese los minutos de la sesión: "))

for i in range(minutos_sesion, 0, -1):
    print(f"Faltan {i} minutos")

print("¡Sesión terminada!")