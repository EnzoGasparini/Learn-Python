# Intentos de login

"""
Un login tiene una contraseña guardada y permite 3 intentos. Si la persona acierta, muestra
"Bienvenido" y termina. Si falla las 3 veces, muestra "Cuenta bloqueada". Después de cada error,
dile cuántos intentos le quedan.
"""
contrasenia_interna = "Admin1234"

contador_intentos = 0

while contador_intentos < 3:
    contrasenia_usuario = input("Introduce la contraseña: ")
    if contrasenia_interna == contrasenia_usuario:
        print("Bienvenido!")
        exit()
    else:
        contador_intentos += 1
        intentos_restantes = 3 - contador_intentos

        print(f"Contraseña inválida, le quedan {intentos_restantes} intentos")

print("Cuenta bloqueada")
