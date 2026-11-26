# Contraseña nueva

"""
Una app le pide a la persona que cree una contraseña. Si tiene menos de 8 caracteres, le avisa y
se la vuelve a pedir, hasta que sea válida. Al final muestra cuántos intentos necesitó.
"""

contrasenia = (input("Introduce tu contraseña: "))
contador_intentos = 1
while len(contrasenia) < 8:
    print("Por favor ingrese una contraseña con al menos 8 caracteres")
    contador_intentos += 1
    contrasenia = (input("Introduce tu contraseña: "))

print(f"Su contraseña fue guardada exitosamente en {contador_intentos} intentos")
