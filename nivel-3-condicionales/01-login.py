# Login

"""
Una app tiene registrados un usuario y una contraseña. La persona ingresa sus credenciales.
Muestra un mensaje si el usuario no existe, si la contraseña es incorrecta o si el acceso es correcto.
"""

usuario_admin = "Admin"
contrasenia_admin = "1234"

usuario1 = input("Ingrese su usuario: ")
contrasenia1 = (input("Ingrese su contraseña: "))

if usuario_admin != usuario1:
    print(f"El usuario {usuario1} no existe")

elif contrasenia_admin != contrasenia1:
    print(f"La contraseña es incorrecta")
else:
    print(f"Bienvenido {usuario1}!, acceso completado")