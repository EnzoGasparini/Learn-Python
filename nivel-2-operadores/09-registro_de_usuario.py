# Registro de usuario

"""
Un formulario de registro pide un nombre de usuario, una contraseña y una confirmación de contraseña (la misma contraseña escrita de nuevo).
Es válido si el usuario tiene al menos 4 caracteres, la contraseña tiene al menos 8 y la confirmación es igual a la contraseña.
Mostrá True o False.
"""

nombre = input("Ingrese su nombre: ")
contrasenia = input("Ingrese su contraseña: ")
confirmacion_contrasenia = input("Ingrese nuevamente su contraseña: ")

valido = len(nombre) >= 4 and len(contrasenia) >= 8 and contrasenia == confirmacion_contrasenia

print("Formulario valido: ", valido)