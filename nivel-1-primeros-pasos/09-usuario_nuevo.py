# Usuario nuevo

"""
Una persona se registra con su nombre.
Mostrale en mayusculas, en minusculas y deciles cuantas letras tiene.
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print(f"Su nombre en mayusculas es: {nombre.upper()} {apellido.upper()}")
print(f"Su nombre en minusculas es: {nombre.lower()} {apellido.lower()}")
print(f"Su nombre tiene: {len(nombre) + len(apellido)} letras")
