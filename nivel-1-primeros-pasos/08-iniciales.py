# Iniciales

"""
Una persona te da su nombre y su apellido.
Mostrá sus iniciales en mayúscula y su nombre completo en una frase.
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print(nombre[0].upper(), apellido[0].upper())
print(f"Tu nombre completo es: {nombre.title()} {apellido.title()}")
