# Cuenta Compartida
"""
Dos amigos te dicen cuánto gastó cada uno en una salida.
Mostrales cuánto gastaron entre los dos.
"""
nombre_amigo1 = input("Introduce el primer nombre: ")
nombre_amigo2 = input("Introduce el segundo nombre: ")
gasto_amigo1 = int(input(f"{nombre_amigo1}, introduce cuanto gastaste:"))
gasto_amigo2 = int(input(f"{nombre_amigo2}, Introduce cuanto gastaste:"))
total = gasto_amigo1 + gasto_amigo2

print(f"El Total Gastado es: $ {total}")